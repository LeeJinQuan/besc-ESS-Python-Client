import validate

class Device:

    #Constructor
    def __init__(self, deviceID, energyUsage):
        self.deviceID = deviceID
        self.energyUsage = energyUsage

     #   self.validate()

    #Serialization
    def serialize(self):
        return {
            "DeviceId": self.deviceID,
            "EnergyUsage": self.energyUsage
        }

    #Validating
    def validate(self):
        validate.string(self.deviceID, "DeviceId")
        validate.number(self.energyUsage, "EnergyUsage")
