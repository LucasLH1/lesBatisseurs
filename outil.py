from ressource import Ressource


class Outil:
    def __init__(self, nom:str, ressource : Ressource, quantite:int):
        self.__nom = nom
        self.__ressource = ressource
        self.__quantite=quantite

    def getNom(self) -> str:
        return self.__nom

    def getRessource(self) -> Ressource:
        return self.__ressource

    def getQuantite(self) -> int:
        return self.__quantite
