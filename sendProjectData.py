import API
from project_data import ProjectData
from device import Device
import keypair as keyPair
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import random

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)
keypair = keyPair.KeyPair("", "")

def sendProjectData():
        result = instance.read()
        
        while result is None:
            pass
        
        temp = round((random.uniform(result.temperature + 0.1, result.temperature + 0.9)), 1)
        humi = round((random.uniform(result.humidity + 0.1, result.humidity + 0.9)), 1)
        
        total = str(round((temp + humi), 1))
        if (".0" in total):
            total = round(total) + 0.1
        else:
            total = round(float(total), 1)
        
        projectData = ProjectData(
            "Testing",
            datetime.datetime.today(),
            [
                Device("AABC1", temp),
                Device("AABC2", humi)
            ],
            total,
            round((total * 0.28434517), 1),
            "Selangor"
        )
            

        try:
            print(API.sendProjectData(keypair, projectData))
            time.sleep(60)
            sendProjectData()

        except Exception as e:
            print(e)

if __name__ == "__main__":

    sendProjectData()
