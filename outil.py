from ressource import Ressource


class Outil:
    def __init__(self, nom:str, ressource : Ressource, cout = 2, quantite = 1):
        self.__nom = nom
        self.__ressource = ressource
        self.__cout = cout
        self.__quantite=quantite

    def getNom(self) -> str:
        return self.__nom

    def getCout(self) -> int:
        return self.__cout

    def getRessource(self) -> Ressource:
        return self.__ressource

    def getQuantite(self) -> int:
        return self.__quantite

    def __str__(self):
        return f"Ressource produite par un outil ({self.getNom()}) : {self.getRessource()} - Quantité : {self.getQuantite()}"
