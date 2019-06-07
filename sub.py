import paho.mqtt.client as mqtt
from encrypt import AESCipher


#the callback function
def on_connect(client, userdata, flags, rc):
     print("Connected With Result Code {}".format(rc))
     client.subscribe("TestingTopic")

def on_disconnect(client, userdata, rc):
	print("Disconnected From Broker")

def on_message(client, userdata, message):
	print(AESCipher("a!m@12ith!s@i").decrypt(message.payload))
	print(message.topic)

broker_address = "192.168.43.190"
broker_portno = 1883
client = mqtt.Client()

#Assigning the object attribute to the Callback Function
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect(broker_address, broker_portno)

client.loop_forever()

