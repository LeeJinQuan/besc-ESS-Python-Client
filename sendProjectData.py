import API
from project_data import ProjectData
from device import Device
import keypair as keyPair
import datetime
import time
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests
import json
import urllib
import pprint


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)


keypair = keyPair.KeyPair("STUD001", "gS5pBilMCBS91z0go3LO6iqLUfZCU0DH")

def sendProjectData():

    while (True):
        result = instance.read()   
        if result.is_valid():

            projectData = ProjectData(
                "Testing",
                datetime.datetime.now(),
                [
                    Device("AABC1", result.temperature),
                    Device("AABC2", result.humidity)
                ],
                110.6,
                80.4,
                "Selangor"
                )
        
        else:
            pass
        
        try:
            print(API.sendProjectData(keypair, projectData))
            time.sleep(10)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    sendProjectData()

