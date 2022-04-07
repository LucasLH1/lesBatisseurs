import unittest

from affranchi import Affranchi
from outil import Outil
from ressource import Ressource
from categorie import Categorie

class testOuvrierQuantiteByRessource(unittest.TestCase):

    def setUp(self) -> None:

        self.resBois = Ressource("bois")
        self.resDecoration = Ressource("decoration")
        self.resPierre = Ressource("pierre")
        self.resArchitecture = Ressource("architecture")
        self.categA = Categorie("Apprenti", 2)

        self.app1 = Affranchi("ouvrier", self.categA)

        self.outil1 = Outil("Scie",self.resBois)

        self.app1.equiperOutil(self.outil1)
        self.app1.ajouterRessource(self.resBois,1)
        self.app1.ajouterRessource(self.resPierre,1)

    def testOuvrierQuantiteByRessourceProduite(self):
        self.assertEqual(self.app1.quantiteByRessource(self.resBois), 2, "Erreur quantite sur ressource produite")

    def testOuvrierQuantiteByRessourceNonProduite(self):
        self.assertEqual(self.app1.quantiteByRessource(self.resArchitecture), 0, "Erreur quantite sur ressource non produite")


if __name__ == '__main__':
    unittest.main()