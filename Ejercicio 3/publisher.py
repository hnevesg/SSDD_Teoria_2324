#!/usr/bin/python3

import json
import paho.mqtt.client as mqtt


def callback(client, userdata, message):
    uuid = message.payload.decode()
    print(f"topic: {message.topic}, uuid: {uuid}")
    client.publish('students', json.dumps(take_reading(uuid)))
    client.loop_stop()

def take_reading(token):
    return {
        'token': token,
        'fullname': 'Nombre Apellido',
        'identifier': '12345678Z'
    }

publisher = mqtt.Client()
publisher.connect('93.189.90.58')
publisher.subscribe('tokens')
publisher.on_message = callback

try:
    while True:
        publisher.loop_start()
except KeyboardInterrupt:
    publisher.disconnect()
    

