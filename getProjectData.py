import API
from project_data import ProjectData
import besc_host as Host
import keypair as keyPair

keypair = keyPair.KeyPair("1", "gS5pBilMCBS91z0go3LO6iqLUfZCU0DH")

host_client = Host.BESC_ESS_Host("http://carboapi.besc.online/besc-data")

def getProjectData():

    options = ProjectData.options
    options["limit"] = 5

    try:
        response = API.sendProjectData(keypair, options)

    except Exception as e:
        raise (response)
        print(e)

if __name__ == "__main__":
    getProjectData()
