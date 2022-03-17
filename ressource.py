from __future__ import annotations

class Ressource:

    def __init__(self, nom : str):
        self.setNom(nom)

    def getNom(self) -> str:
        """
        :return: str
        """
        return self.__nom

    def setNom(self, valeur : str):
        """
        Permet de valoriser l'attribut salaire
        :param valeur: float
        """
        self.__nom = valeur

    # def __eq__(self, autreRessource : Ressource) -> bool:
    #     return self.getNom() == autreRessource.getNom()

    def __hash__(self) -> int:
        affichage = ""
        for nom in self.getNom():
            affichage+=str(ord(nom))
        return int(affichage)

    def __str__(self):
        pass
