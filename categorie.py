from __future__ import annotations
from typing import List


class Categorie:

    def __init__(self, libelle : str, salaire : float):
        self.setSalaire(salaire)
        self.setLibelle(libelle)

    def getSalaire(self) -> float:
        return self.__salaire

    def getLibelle(self) -> str:
        return self.__libelle

    def setSalaire(self, valeur : float):

        self.__salaire = valeur

    def setLibelle(self, valeur : str):
        self.__libelle = valeur

    def __str__(self):
        return str(self.getLibelle()) + ", son salaire est de " + str(self.getSalaire()) + " pièces."
