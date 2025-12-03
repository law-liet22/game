import time
import os
from Config import Logging

class Terminal:
    def clearTerminal():
        os.system("clear")

    def afficherAvecPoints(msg):
        try:
            if type(msg) == str:
                print(msg, end="")
                for i in range(3):
                    print(".", end="", flush=True)
                    time.sleep(1)
                Terminal.clearTerminal()
            else:
                raise Exception("Le message entré n'était pas de type str.")
        except Exception as e:
            print("Erreur lors de l'affichage de ce message.")
            Logging._logging.error(f"Erreur lors de l'affichage du message : {e}")