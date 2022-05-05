from typing import List

from batiment import Batiment
from ouvrier import Ouvrier
from ressource import Ressource


class Chantier():
    def __init__(self, batiment : Batiment):
        self.__batiment = batiment
        self.__listeOuvriers = []
        self.__ressourcesByEquipe = {Ressource("pierre"): 0, Ressource("bois"): 0, Ressource("architecture"): 0, Ressource("decoration"): 0}
        self.__termine = False

    def getBatiment(self):
        return self.__batiment

    def getOuvriers(self):
        return self.__listeOuvriers

    def estTermine(self) -> bool:
        return self.__termine

    def setTermine(self, termine : bool):
        self.__termine = termine

    def getListeOuvriers(self):
        return self.__listeOuvriers

    def quantiteByRessourceEquipe(self, uneRessource : Ressource):
        quantite=0
        for ouvrier in self.__listeOuvriers:
            quantite+= ouvrier.quantiteByRessource(uneRessource)
        return quantite

    def envoyerTravaillerOuvrier(self, unOuvrier: Ouvrier):
        self.__listeOuvriers.append(unOuvrier)
        ressources=list(self.getBatiment().getRessources().keys())
        ressourcesNecessaires = True
        i=0
        while ressourcesNecessaires and i < len(ressources):
            if self.quantiteByRessourceEquipe(ressources[i]) < self.getBatiment().quantiteByRessourceBatiment(ressources[i]):
                ressourcesNecessaires = False
            i+=1
        return ressourcesNecessaires

    def __str__(self):
        affichage="Le chantier du batiment " + self.getBatiment().getLibelle() + "\nRessources nécessaires : \n"
        for ressource, nombre in self.getBatiment().getRessources().items():
            affichage+="- " + ressource.getNom() + " : Quantité : " + str(nombre)+ "\n"
        affichage+="Vous gagnerez en le construisant : \n" + "- " + str(self.getBatiment().getGainSesterces()) + " sesterces\n- " + str(self.getBatiment().pointsVictoire() + "points de Victoire")
        affichage+="\nChantier terminé : "
        if self.estTermine():
            affichage+= "oui\n"
        else:
            affichage+="non\n"
        return affichage

