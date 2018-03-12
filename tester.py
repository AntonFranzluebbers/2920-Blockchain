from flask import request
import json
import requests
import random

def insert_random_data():
    url = "http://localhost:8000/"

    # create the data
    data = {
        "device_id": "abcd1234",
        "time": "2018-01-01",
        "temp": random.randrange(0,40),
        "humid": random.randrange(0,100),
        "moist1": random.randrange(0,100),
        "moist2": random.randrange(0,100)
    }

    # get the response with nonce and hash
    response = requests.post(url + "construct", data=data)
    # add the nonce and hash to the data
    combined = data.update(response.json())
    # send the data to the server
    insert_response = requests.post(url + "insert", data=data)

insert_random_data()
