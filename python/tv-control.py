import paho.mqtt.client as mqtt
import ssl as ssl
import time
# For calling commands
import subprocess
# Custom module for lirc functions
import lirc
import command_controller

# Variables
cafile="/etc/ssl/certs/ca-certificates.crt"
topic="Samsung" #Remote name

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # Turn message into command and remote
    payload_str = str(msg.payload)
    remote = str(msg.topic)

    command_controller.run(remote, payload_str)

try:
    # Connect
    client = mqtt.Client()
    client.username_pw_set("matt","fuckthis")
    # Confire SSL connection
    client.tls_set(cafile, tls_version=ssl.PROTOCOL_TLSv1_2)
    #client.tls_insecure_set(True)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.mattlong.la", 8883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
except (KeyboardInterrupt, SystemExit):
    raise

