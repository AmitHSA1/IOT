import paho.mqtt.client as mqtt
from encrypt import AESCipher

def pub_msg(msg):
	broker_address = "localhost"
	broker_portno = 1883
	client = mqtt.Client()
	client.connect(broker_address, broker_portno)
	client.subscribe("TestingTopic")
	client.publish(topic = "TestingTopic", payload = AESCipher("a!m@12ith!s@i").encrypt(msg))
