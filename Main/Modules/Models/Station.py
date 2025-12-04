import json

donneesInitialesJSON = open("Main/Config/station.json", "r")
donneesInitiales = json.load(donneesInitialesJSON)

class Station:
    def __init__(self, name = donneesInitiales["name"], initialAltitude = donneesInitiales['initialAltitude'], 
                 initialVelocity = donneesInitiales['initialVelocity'], initialFuel = donneesInitiales['initialFuel'],
                 maxFuel = donneesInitiales['maxFuel'], initialEnergy = donneesInitiales['initialEnergy'],
                 maxEnergy = donneesInitiales['maxEnergy'], initialOxygen = donneesInitiales['initialOxygen'], 
                 maxOxygen = donneesInitiales['maxOxygen'], initialWater = donneesInitiales['initialWater'], 
                 maxWater = donneesInitiales['maxWater'], initialTemperature = donneesInitiales['initialTemperature'], 
                 initialIntegrity = donneesInitiales['initialIntegrity'], initialAlertLevel = donneesInitiales['initialAlertLevel'],
                 initialCrewCount = donneesInitiales['initialCrewCount'], maxCrewCount = donneesInitiales['maxCrewCount'],
                 hourComsuption = donneesInitiales['hourComsuption']):
        
        self.__name = name
        self.__altitude = initialAltitude
        self.__velocity = initialVelocity
        self.__fuel = initialFuel
        self.__maxFuel = maxFuel
        self.__energy = initialEnergy
        self.__maxEnergy = maxEnergy
        self.__oxygen = initialOxygen
        self.__maxOxygen = maxOxygen
        self.__water = initialWater
        self.__maxWater = maxWater
        self.__temperature = initialTemperature
        self.__integrity = initialIntegrity
        self.__alertLevel = initialAlertLevel
        self.__crewCount = initialCrewCount
        self.__maxCrewCount = maxCrewCount
        self.__hourComsuption = hourComsuption
    
    def descrireStation(self):
        print(f"""\nNom de la station : {self.getName()}
Altitude actuelle : {self.getAltitude()} km
Vitesse actuelle : {self.getVelocity()} km/s\nCarburant : {self.getFuel()} L
Carburant maximal : {self.getMaxFuel()} L\nEnergie : {self.getEnergy()} kWh
Energie maximale : {self.getMaxEnergy()} kWh\nOxygène : {self.getOxygen()} u
Oxygène maximal : {self.getMaxOxygen()} u\nEau : {self.getWater()} L
Eau maximal : {self.getMaxWater()} L\nTempérature : {self.getTemperature()} °C
Intégrité : {self.getIntegrity()}%\nNiveau d'alerte : {self.getAlertLevel()}
Nombre de personnel : {self.getCrewCount()}\nNombre de personnel max : {self.getMaxCrewCount()}
Consommation horaire : {self.getHourComsuption()} L/h""")

    def getName(self):
        return self.__name
    
    def getAltitude(self):
        return self.__altitude
    
    def getVelocity(self):
        return self.__velocity
    
    def getFuel(self):
        return self.__fuel
    
    def getMaxFuel(self):
        return self.__maxFuel
    
    def getEnergy(self):
        return self.__energy
    
    def getMaxEnergy(self):
        return self.__maxEnergy
    
    def getOxygen(self):
        return self.__oxygen
    
    def getMaxOxygen(self):
        return self.__maxOxygen
    
    def getWater(self):
        return self.__water
    
    def getMaxWater(self):
        return self.__maxWater
    
    def getTemperature(self):
        return self.__temperature
    
    def getIntegrity(self):
        return self.__integrity
    
    def getAlertLevel(self):
        return self.__alertLevel
    
    def getCrewCount(self):
        return self.__crewCount
    
    def getMaxCrewCount(self):
        return self.__maxCrewCount
    
    def getHourComsuption(self):
        return self.__hourComsuption
    