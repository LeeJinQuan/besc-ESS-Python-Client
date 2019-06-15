import API
from project_data import ProjectData
from device import Device
import besc_host as Host
import keypair as keyPair
import datetime

keypair = keyPair.KeyPair("STUD001", "gS5pBilMCBS91z0go3LO6iqLUfZCU0DH")

host_client = Host.BESC_ESS_Host("http://carboapi.besc.online/besc-data")

def sendProjectData():

    projectData = ProjectData(
        "Testing",
        datetime.datetime.now(),
        [
            Device("AABC1", 40),
            Device("AABC2", 70)
        ],
        110,
        80,
        "101.1212, 112.1133"
        )

    try:
        response = API.sendProjectData(keypair, projectData)

    except Exception as e:
        raise (response)
        print(e)

if __name__ == "__main__":
    sendProjectData()
