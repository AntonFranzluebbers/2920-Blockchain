from flask import request
import json
import requests

url = "http://localhost:8000/"

# create the data
data = {
    "device_id": "abcd1234",
    "time": "2018-01-01",
    "temp": 20,
    "humid": 50,
    "moist1": 20,
    "moist2": 10
}

# get the response with nonce and hash
response = requests.post(url + "construct", data=data)
combined = data.update(response.json())
insert_response = requests.post(url + "insert", data=data)
