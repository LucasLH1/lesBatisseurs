from typing import List

from ressource import Ressource
from ouvrier import Ouvrier

class Batiment:
    def __init__(self, libelle: str, pointsVictoire: int, gainSesterces: int ):
        self.__libelle = libelle
        self.__gainSesterces = gainSesterces
        self.__pointsVictoire = pointsVictoire
        self.ressourcesNecessaires = {Ressource("pierre"): 0, Ressource("bois"): 0, Ressource("architecture"): 0,
                                Ressource("decoration"): 0}
        self.__listeOuvriers = List[Ouvrier]
    def getLibelle(self):
        return self.__libelle

    def getGainSesterces(self):
        return self.__gainSesterces

    def pointsVictoire(self):
        return self.__pointsVictoire

    def ajouterRessource(self, ressource: Ressource, quantite: int) -> None:
        for key in self.ressourcesNecessaires.keys():
            if ressource == key:
                self.ressourcesNecessaires[key] += quantite

    def getRessources(self):
        return self.ressourcesNecessaires

    def qteEquipeByRessource(self):

    def envoyerTravaillerOuvrier(self, unOuvrier : Ouvrier):
        self.__listeOuvriers.append(unOuvrier)


    def __str__(self):
        affichage = "Batiment : " + self.getLibelle() + "\nLe bâtiment requiert les ressources :\n"
        for ressource, nombre in self.ressourcesNecessaires.items():
            if nombre != 0:
                affichage += "- " + str(ressource.getNom()) + " : " + str(nombre) + "\n"
        return  affichage