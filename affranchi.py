from categorie import Categorie
from outil import Outil
from ouvrier import Ouvrier
from ressource import Ressource


class Affranchi(Ouvrier):
    def __init__(self, nom:str, categorie: Categorie):
        super().__init__(nom)
        self.__categorie = categorie
        self.__outil = Outil
        self.__equiperOutil = False
        self.__lesRessources = {Ressource("pierre"): 0, Ressource("bois"): 0, Ressource("architecture"): 0,
                                Ressource("decoration"): 0}

    def getCout(self):
        return self.getCategorie().getSalaire()

    def getCategorie(self) -> Categorie:
        return self.__categorie

    def setCategorie(self, valeur : Categorie):
        self.__categorie = valeur

    def equiperOutil(self, outil : Outil):
        self.__outil = outil
        self.__equiperOutil = True

    def quantiteByRessource(self, uneRessource: Ressource) -> int:
        for ressource in self.__lesRessources.keys():
            if ressource == uneRessource:
                return self.__lesRessources[ressource]


    def __str__(self):
        res = super().__str__(0)
        res+="Coût de mise sur chantier : " + str(self.getCout()) + " sesterces\n"
        return res
