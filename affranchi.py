from categorie import Categorie
from outil import Outil
from ouvrier import Ouvrier
from ressource import Ressource


class Affranchi(Ouvrier):
    def __init__(self, nom:str, categorie: Categorie):
        super().__init__(nom)
        self.__categorie = categorie
        self.__outil = None

    def getCout(self):
        return self.getCategorie().getSalaire()

    def getCategorie(self) -> Categorie:
        return self.__categorie

    def setCategorie(self, valeur : Categorie):
        self.__categorie = valeur

    def getOutil(self):
        return self.__outil

    def equiperOutil(self, outil : Outil):
        self.__outil = outil

    def quantiteByRessource(self, uneRessource: Ressource) -> int:
        qte = super().quantiteByRessource(uneRessource)
        if self.__outil is not None:
            if uneRessource==self.getOutil().getRessource():
                qte+=self.getOutil().getQuantite()
        return qte


    def __str__(self):
        res = super().__str__(0)
        res+="Coût de mise sur chantier : " + str(self.getCout()) + " sesterces\n"
        res+=str(self.getOutil())
        return res
