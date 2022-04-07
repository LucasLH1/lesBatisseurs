from ressource import Ressource


class Batiment:
    def __init__(self, nom: str, gain: int, ptVictoire: int, ressourcesNecessaires: dict[Ressource, int]):
        self.__nom = nom
        self.__gain = gain
        self.__ptVictoire = ptVictoire
        self.__ressourcesNecessaires = ressourcesNecessaires

    def getNom(self):
        return self.__nom

    def getGain(self):
        return self.__gain

    def ptVictoire(self):
        return self.__ptVictoire

    def getRessources(self):
        return self.__ressourcesNecessaires

    def __str__(self):
        affichage = "Bâtiment : " + str(self.__nom) + "\nGain d'argent : " + str(self.__gain) + "\nGain en point de victoire : " + str(self.__ptVictoire) + "\nCout en ressources : \n"
        for ressource, nombre in self.__ressourcesNecessaires.items():
            affichage+=  "- " + str(ressource) + " : " + str(nombre) + "\n"
        return  affichage