class Module:
    def __init__(self, name: str, type: str, capacity: int, volume: float, energyConsumption: float, status: str, crewPresent: int, ressources: dict):
        self.__name = name
        self.__type = type
        self.__capacity = capacity
        self.__volume = volume
        self.__energyConsumption = energyConsumption
        self.__status = status
        self.__crewPresent = crewPresent
        self.__ressources = ressources

    def addCrew(self, n):
        if(self.__crewPresent+n > self.__crewPresent):
            print(f"Il est impossible d'affecter {n} membre(s) du personnel à ce module. Il n'a pas la capacité nécessaire.")
        else:
            self.__crewPresent += n

    def removeCrew(self, n):
        pass