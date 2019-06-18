import validate as validate
import device as Device
import dateConvert as dateUtil
import datetime

class ProjectData:

    '''
    * @param {string} project - Project Name
    * @param {string} datetime - DateTime in string
    * @param {[Device]} devices - Device object
    * @param {number} totalEnergyUsage - TotalEnergyUsage
    * @param {number} averageRT - AverageRT
    * @param {string} geolocation - Geolocation
    '''
    #Constructor
    def __init__(self, project_name, dateTime, devices, totalEnergyUsage, averageRT, geolocation):
        self.project = project_name
        self.datetime = dateTime
        self.devices = devices
        self.totalEnergyUsage = totalEnergyUsage
        self.averageRT = averageRT
        self.geolocation = geolocation

        self.validate()

        self.datetime = dateUtil.formatDatetimeString(self.datetime)

    '''
    * @param {string} project - Project Name
    * @param {string} datetime - DateTime in string
    * @param {[Device]} devices - Device object
    * @param {number} totalEnergyUsage - TotalEnergyUsage
    * @param {number} averageRT - AverageRT
    * @param {string} geolocation - Geolocation
    * @returns {ProjectData}
    '''
    #Return self with current time
    def creatWithCurrentTime(self, project_name, devices, totalEnergyUsage, averageRT, geolocation):
        dateNow = datetime.datetime.now()
        formattedDateTime = dateUtil.formatDatetimeString(dateNow)
        return ProjectData(project_name, formattedDateTime, devices, totalEnergyUsage, averageRT, geolocation)

    #Validating
    def validate(self):

        if(isinstance(self.devices, list) != True):
            raise Exception("Devices ID is not list")

        elif(len(self.devices) == 0):
            raise Exception("Devices cannot be empty")

        else:
            for device in self.devices:
                if (isinstance(device, Device.Device) != True):
                    raise Exception("Item of Devices must be instance of Device")

        validate.checkfloat(self.averageRT, "AverageRT")
        validate.checkfloat(self.totalEnergyUsage, "TotalEnergyUsage")
        validate.string(self.geolocation, "Geolocation")
        validate.string(self.project, "Project")
        validate.datetimeString(self.datetime, "DateTime")

    #Device Serialization
    def serializeDevices(self):
        serialized_Devices = []

        for device in self.devices:
            serialized_Devices.append(device.serialize())

        return serialized_Devices


    options = {
        "limit": 5,
        "offset": 0,
        "start_date": None,
        "end_date": None
    }
