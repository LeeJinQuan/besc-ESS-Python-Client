import besc_host as Host
import requests
import json
import hashlib

def sendProjectData(keyPair, projectData):
    client = Host.BESC_ESS_Host(("http://carboapi.besc.online/besc-data"))
    client.setProjectId(keyPair.projectId)
    client.setEndPoint(Host.endpoints.get("project"))

    jsonData = json.dumps(serialize(projectData).get("data"), indent=2)
    print(jsonData)

    options = {
        "method": "POST",
        "uri": client.buildUrl(),
        "headers": {
            "apikey": keyPair.apiKey,
            "Content-Type": "application/json",
            "checksum": serialize(projectData).get("checksum")
        },
        "body": serialize(projectData).get("data"),
        "json": True
    }

    try:
        r = requests.post(options.get("uri"), headers=options.get("headers"), data=jsonData)
        print(r.json())
        print(r.text)
    except:
        print(r.status_code)

#Serialization
def serialize(projectData):
    dataToSend = {
        "Project": projectData.project,
        "DateTime": projectData.datetime,
        "Devices": projectData.serializeDevices(),
        "TotalEnergyUsage": projectData.totalEnergyUsage,
        "AverageRT": projectData.averageRT,
        "Geolocation": projectData.geolocation
    }

    #NOT SURE
    hashdata = hashlib.sha1(json.dumps(dataToSend).encode()).hexdigest()
    print(hashdata)
    serialized = {
        "data": dataToSend,
        "checksum": hashdata
    }

    return serialized
