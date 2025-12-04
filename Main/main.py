import json, time
from Modules import *
from Config.keys import *
from Config import Logging
from Modules.Models.Menus import *
from Modules.Models.Terminal import *
from Modules.Models.Station import *
from Modules.Utils.randomInitialValues import *

def clearTerminal():
    Terminal.clearTerminal()

def afficherAvecPoints(msg):
    Terminal.afficherAvecPoints(msg)

logg = Logging._logging

def __main__():
    play = True


    while play:
        try:
            clearTerminal()
            logg.info("Programme lancé.")
            Menus.afficherMenuP()
            

            choice = input("\nChoisissez une option (0-4) : ")
            clearTerminal()

            if choice == '1':
                nom = input("Entrez un nom pour votre station : ")
                generateAndPushValues(nom)
                # afficherAvecPoints("Démarrage de la simulation")
                station = Station(nom)
                station.descrireStation()
                return

            elif choice == '2':
                pass

            elif choice == paramsKey:
                pass

            elif choice == exitKey:
                afficherAvecPoints("Arrêt du programme")
                play = False
                logg.info("Programme arrêté par l'utilisateur.")
                return
            
            else:
                afficherAvecPoints("Entrez un choix valide")

        except KeyboardInterrupt:
            logg.info("Arrêt forcé du programme par l'utilisateur.")
            play = False
            return

if __name__ == "__main__":
    __main__()