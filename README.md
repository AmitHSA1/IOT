# Cryptography For IOT
The aim of this project is to help secure iot devices so that data can be transfered securely between devices.

# Usage

1. Import the pub_msg function fro pub.py file.
2. Call `pub_msg()` to publish the message.

Run the `sub.py` script to first Subscribe to the topic and the run `pub.py` script to publish the message on the topic

For example:

```python
import RPi.GPIO as GPIO
import dht11
import time
import datetime
from pub import pub_msg
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=17)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
	print("Temperature: %d F" % ((result.temperature * 9/5)+32))
	pub_msg(((result.temperature * 9/5)+32))
        print("Humidity: %d %%" % result.humidity)
	
    time.sleep(1)

```

For working example, see `temp.py` (you would probably need to adjust pin for your configuration)


