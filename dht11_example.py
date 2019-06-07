import RPi.GPIO as GPIO
import dht11
import time
import datetime
from pub import pub_msg
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pub_msg("hello")
# read data using pin 14
instance = dht11.DHT11(pin=17)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
	print("Temperature: %d F" % ((result.temperature * 9/5)+32))
        print("Humidity: %d %%" % result.humidity)
	
    time.sleep(1)
