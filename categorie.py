from __future__ import annotations
from typing import List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ouvrier import Ouvrier

class Categorie:

    def __init__(self, salaire : float, libelle : str):
        self.setSalaire(salaire)
        self.setLibelle(libelle)
        self.__listeOuvrier = []

    def getSalaire(self) -> float:
        """
        :return: float
        """
        return self.__salaire

    def getLibelle(self) -> str:
        """
        :return: str
        """
        return self.__libelle

    def setSalaire(self, valeur : float):
        """
        Permet de valoriser l'attribut salaire
        :param valeur: float
        """
        self.__salaire = valeur

    def setLibelle(self, valeur : str):
        """
        Permet de valoriser l'attribut libelle
        :param valeur: str
        """
        self.__libelle = valeur

    def getLesOuvriers(self) -> List[Ouvrier]:
        return self.__listeOuvrier

    def setLesOuvriers(self, valeur : Ouvrier):
        self.__listeOuvrier = valeur

    def ajouterOuvrier(self, ouvrier : Ouvrier):
        self.__listeOuvrier.append(ouvrier)

    def __str__(self):
        return self.getLibelle() + ", son salaire est de " + str(self.getSalaire()) + " pièces."
