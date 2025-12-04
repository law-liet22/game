import json
import random

jsonPath = "Main/Config/station.json"

def generateAndPushValues(name):
    """Genere et envoie les valeurs générées dans le fichier json de configuration initiale."""
    initialAltitude = round(random.uniform(300, 900), 2)
    initialVelocity = round(random.uniform(6.8, 8.2), 2)
    initialFuel = round(random.uniform(150, 1000), 2)
    maxFuel = round(random.uniform(1000, 5000), 2)
    initialEnergy = round(random.uniform(150, 500), 2)
    maxEnergy = round(random.uniform(500, 750), 2)
    initialOxygen = round(random.uniform(450, 750), 2)
    maxOxygen = round(random.uniform(750, 1500), 2)
    initialWater = round(random.uniform(50, 100), 2)
    maxWater = round(random.uniform(100, 300))
    temperature = round(random.uniform(15, 25), 2)
    integrity = round(random.uniform(0.95, 1), 1)
    alertLevel = 0
    maxCrewCount = random.randint(3, 7)
    crewCount = random.randint(0, maxCrewCount)
    hourComsumption = round(random.uniform(0.05, 0.15), 2)

    values = {
    "name": name,
    "initialAltitude": initialAltitude,
    "initialVelocity": initialVelocity,
    "initialFuel": initialFuel,
    "maxFuel": maxFuel,
    "initialEnergy": initialEnergy,
    "maxEnergy": maxEnergy,
    "initialOxygen": initialOxygen,
    "maxOxygen": maxOxygen,
    "initialWater": initialWater,
    "maxWater": maxWater,
    "initialTemperature": temperature,
    "initialIntegrity": integrity,
    "initialAlertLevel": alertLevel,
    "initialCrewCount": crewCount,
    "maxCrewCount": maxCrewCount,
    "hourComsuption": hourComsumption
    }

    f = open(jsonPath, 'w')
    f.write(json.dumps(values))