import API
from project_data import ProjectData
from device import Device
import keypair as keyPair
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import decimal
import random

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
        
            temp = float(decimal.Decimal(random.randrange(result.temperature - 1.01, result.temperature + 1.01)))
            humi = float(decimal.Decimal(random.randrange(result.humidity - 1.01, result.humidity + 1.01)))
            total = temp + humi
        
                projectData = ProjectData(
                    "Testing",
                    datetime.datetime.now(),
                    [
                        Device("AABC1", temp),
                        Device("AABC2", humi)
                    ],
                    float(decimal.Decimal(random.randrange(total - 1.01, total + 1.01))),
                    (result.temperature + result.humidity) * 0.28434517,
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
