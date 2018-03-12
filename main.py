# MIT License
# Copyright (c) 2017 Adam K.C. Chin
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sqlite3
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from json import dumps, loads
from flask_jsonpify import jsonpify
import json
import requests


def call_hash(data):
    url = 'http://127.0.0.1:8002/hash/'
    try:
        del data['hash']
    except:
        pass
    data2 = {}
    data2['data'] = json.dumps(data)
    # print data2
    response = requests.post(url, data=data2, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['hash']


def call_nonce():
    nonce_url = 'http://127.0.0.1:8001/nonce'
    response = requests.get(nonce_url)
    if response.status_code == 200:
        return response.json()['nonce']


def get_pre_hash(cursor):
    cursor.execute('select * from blockchain order by id desc limit 1')
    results = cursor.fetchall()
    if results:
        return results[0]['hash']
    else:
        return ""


def database_connect():
    conn = sqlite3.connect('blockchain.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    return conn, cursor


def add_hashing_entries(data1):
    nonce = {"nonce": u""}
    hash = {"hash": u""}
    pre_hash = {"pre_hash": u""}
    data1.update(nonce)
    data1.update(hash)
    data1.update(pre_hash)
    return data1


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


app = Flask(__name__)


@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        data = request.form
        data1 = data.to_dict()
        conn, cursor = database_connect()
        try:
            cursor.execute(
                "INSERT INTO blockchain(device_id, time, temp, humid, moist1, moist2, nonce, hash) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)",
                [data1['device_id'], data1['time'], data1['temp'], data1['humid'],
                 data1['moist1'], data1['moist2'], data1['nonce'], data1['hash']])
            conn.commit()
            print("Success")
            return "Success"
        except:
            print("Failed")
            return "Failed"
            conn.close()
    else:
        return ""


@app.route("/verify", methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        try:
            id = request.args.get('id', default=2, type=int)
            conn, cursor = database_connect()
            cursor.execute('SELECT * FROM blockchain WHERE id <= ? ORDER BY id DESC LIMIT 2', [id, ])
            results = cursor.fetchall()
            records_verify = results[0]
            hash_now = results[0]['hash']
            pre_hash = {u"pre_hash": u""}
            records_verify.update(pre_hash)
            records_verify['pre_hash'] = results[1]['hash']
            del records_verify['id']
            hash_value = call_hash(records_verify)
            conn.close()
            print("HI")
            if hash_value == hash_now:
                return "Verified"
            else:
                return "Failed"
        except:
            return "Error"
        conn.close()
    else:
        return ""

@app.route("/display", methods=['GET', 'POST'])
def display():
    if request.method == 'GET':
        try:
            conn, cursor = database_connect()
            cursor.execute('SELECT * FROM blockchain;')
            results = cursor.fetchall()
            out = render_template("data.html", data=results)
            return out
        except:
            return "Error displaying data"
            conn.close()
    else:
        return ""

@app.route("/display_all", methods=['GET', 'POST'])
def display_all():
    if request.method == 'GET':
        try:
            conn, cursor = database_connect()
            cursor.execute('SELECT * FROM blockchain;')
            results = cursor.fetchall()
            out = render_template("data_all.html", data=results)
            return out
        except:
            return "Error displaying data"
            conn.close()
    else:
        return ""


@app.route("/construct", methods=['GET', 'POST'])
def construct():
    if request.method == 'POST':
        data = request.form  # .get("data")
        data1 = data.to_dict()
        print(data1)
        conn, cursor = database_connect()
        data1 = add_hashing_entries(data1)
        print(data1)
        data1['pre_hash'] = get_pre_hash(cursor)
        data1['nonce'] = call_nonce()
        data1['hash'] = call_hash(data1)
        conn.close()
        return jsonpify(data1)
    else:
        print("NOPE")
        return ""

def create_db():
    conn,cursor = database_connect()
    if conn is not None:
        sql_create_projects_table = """CREATE TABLE IF NOT EXISTS blockchain (id INTEGER PRIMARY KEY, device_id text,time DATE NOT NULL,temp NUMBER,humid NUMBER,moist1 NUMBER,moist2 NUMBER, nonce text, hash text); """
        try:
            c = conn.cursor()
            c.execute(sql_create_projects_table)
        except sqlite3.Error as e:
            print(e)
    else:
        print ("Failed to create db table.")
    return

if __name__ == "__main__":
    create_db()
    app.run(host='127.0.0.1', port=8000)

