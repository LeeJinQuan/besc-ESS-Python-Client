import besc_host as Host
import requests
import json
import hashlib
from collections import OrderedDict
import dashboard

def sendProjectData(keyPair, projectData):
    client = Host.BESC_ESS_Host(("http://carboapi.besc.online/besc-data"))
    client.setProjectId(keyPair.projectId)
    client.setEndPoint(Host.endpoints.get("project"))

    jsonData = serialize(projectData).get("data")
    jsonChecksum = serialize(projectData).get("checksum")

    headersDict = OrderedDict([
            ("apikey", keyPair.apiKey),
            ("Content-Type", "application/json"),
            ("checksum", jsonChecksum)
        ])

    options = OrderedDict([
        ("method", "POST"),
        ("uri", client.buildUrl()),
        ("headers", headersDict),
        ("body", jsonData),
        ("json", True)
    ])
    
    try:
        r = requests.post(options.get("uri"), headers=options.get("headers"), data=jsonData)
        return r.text

    except:
        print(r.status_code)

#Serialization
def serialize(projectData):
    dataToSend = json.dumps(OrderedDict([("Project", projectData.project),
                                         ("DateTime", projectData.datetime),
                                         ("Devices", projectData.serializeDevices()),
                                         ("TotalEnergyUsage", projectData.totalEnergyUsage),
                                         ("AverageRT", projectData.averageRT),
                                         ("Geolocation", projectData.geolocation)]),
                            separators=(',', ':'))

    hashdata = hashlib.sha1((dataToSend).encode('UTF-8')).hexdigest()
    serialized = OrderedDict([
        ("data", dataToSend),
        ("checksum", hashdata)
    ])

    return serialized
