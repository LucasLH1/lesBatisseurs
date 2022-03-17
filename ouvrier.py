from __future__ import annotations
from categorie import Categorie
from ressource import Ressource


class Ouvrier:

    def __init__(self, categorie : Categorie):
        self.setCategorie(categorie)
        self.__lesRessources = {Ressource("pierre") : 0, Ressource("bois") : 0, Ressource("architecture") : 0, Ressource("decoration") : 0}

    def getCategorie(self) -> Categorie:
        """
        :return: float
        """
        return self.__categorie

    def setCategorie(self, valeur : Categorie):
        """
        Permet de valoriser l'attribut categorie
        :param valeur: Categorie
        """
        self.__categorie = valeur

    def ajouterRessource(self, ressource : Ressource, nombre : int) -> None:
        self.__lesRessources[ressource] = nombre

    def quantiteByRessource(self, uneRessource : Ressource) -> int:
        for ressource in self.__lesRessources.keys():
            if ressource == uneRessource:
                return self.__lesRessources[ressource]

    def __str__(self):
        affichage = "Vous possédez un " + str(self.getCategorie()) +"\nL'ouvrier possède ces ressources :\n"
        for ressource, nombre in self.__lesRessources.items():
            affichage+= ressource.getNom() + " : " +str(nombre)+ "\n"
        return affichage