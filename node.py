from flask import request
import json
import requests
import random
import os
from datetime import datetime
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

url = "http://localhost:8000/"
device_id = "PI-123"
dht_sensor = DHT.DHT11

# pins
dht_pin = 4
moist1_pin = 14
moist2_pin = 15


# sets the pins to inputs
def setup_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dht_pin, GPIO.IN)
    GPIO.setup(moist1_pin, GPIO.IN)
    GPIO.setup(moist2_pin, GPIO.IN)

# actually sends the data to the server
def send_data(temp, humid, moist1, moist2):

    # create the data
    data = {
        "device_id": device_id,
        "time": datetime.now(),
        "temp": temp,
        "humid": humid,
        "moist1": moist1,
        "moist2": moist2
    }

    # get the response with nonce and hash
    response = requests.post(url + "construct", data=data)
    # add the nonce and hash to the data
    combined = data.update(response.json())
    # send the data to the server
    insert_response = requests.post(url + "insert", data=data)


def sensor_loop():
    inp = ""
    # loop on user input
    while(1):
        inp = input("Press 'q' to exit or any other key to log")
        sense()
        sleep(60)

def sense():
    setup_pins()
    h,t = DHT.read_retry(dht_sensor, dht_pin)
    # TODO read from moisture sensors
    send_data(t,h,0,0)
    GPIO.cleanup()

setup_pins()
sense()
