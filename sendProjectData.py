import API
from project_data import ProjectData
from device import Device
import keypair as keyPair
import datetime
import time

keypair = keyPair.KeyPair("STUD001", "gS5pBilMCBS91z0go3LO6iqLUfZCU0DH")

def sendProjectData():

    while (True):
        projectData = ProjectData(
            "Testing",
            datetime.datetime.now(),
            [
                Device("AABC1", 40.0),
                Device("AABC2", 70.0)
            ],
            110.0,
            80.0,
            "Selangor"
            )

        try:
            print(API.sendProjectData(keypair, projectData))
            time.sleep(10)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    sendProjectData()
