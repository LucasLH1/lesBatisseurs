from __future__ import annotations
from categorie import Categorie
from ressource import Ressource


class Ouvrier:
    def __init__(self, nom: str):
        self.__nom = nom
        self.__cout = 0
        self.__lesRessources = {Ressource("pierre"): 0, Ressource("bois"): 0, Ressource("architecture"): 0,
                                Ressource("decoration"): 0}

    def getCout(self):
        return self.__cout

    def getNom(self) -> str:
        return self.__nom

    def setNom(self, valeur: str):
        self.__nom = valeur

    def ajouterRessource(self, ressource: Ressource, quantite: int) -> None:
        for key in self.__lesRessources.keys():
            if ressource == key:
                self.__lesRessources[key] += quantite

    def quantiteByRessource(self, uneRessource: Ressource) -> int:
        for ressource in self.__lesRessources.keys():
            if ressource == uneRessource:
                return self.__lesRessources[ressource]

    def __str__(self, version=1):
        affichage = "Ouvrier : " + self.getNom() + "\nL'ouvrier possède ces ressources :\n"
        for ressource, nombre in self.__lesRessources.items():
            if nombre != 0:
                affichage += "- " + str(ressource.getNom()) + " : " + str(nombre) + "\n"
        if version==1:
            affichage+="Coût de mise sur chantier : gratuit.\n"

        return affichage
