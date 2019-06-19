import validate
from collections import OrderedDict

class Device:

    #Constructor
    def __init__(self, deviceID, energyUsage):
        self.deviceID = deviceID
        self.energyUsage = energyUsage

     #   self.validate()

    #Serialization
    def serialize(self):
        return OrderedDict([
            ("DeviceId", self.deviceID),
            ("EnergyUsage", self.energyUsage)]
        )

    #Validating
    def validate(self):
        validate.string(self.deviceID, "DeviceId")
        validate.number(self.energyUsage, "EnergyUsage")
