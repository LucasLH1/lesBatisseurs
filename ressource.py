from __future__ import annotations

class Ressource:

    def __init__(self, nom : str):
        self.setNom(nom)

    def getNom(self) -> str:
        return self.__nom

    def setNom(self, valeur : str):
        self.__nom = valeur

    def __eq__(self, autreRessource : Ressource) -> bool:
        return self.getNom() == autreRessource.getNom()

    def __hash__(self) -> int:
        affichage = ""
        for nom in self.getNom():
            affichage+=str(ord(nom))
        return int(affichage)

    def __repr__(self):
        return self.__nom
