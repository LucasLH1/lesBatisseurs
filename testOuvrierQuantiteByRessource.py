import unittest
from ressource import Ressource
from ouvrier import Ouvrier
from categorie import Categorie

class testOuvrierQuantiteByRessource(unittest.TestCase):

    def setUp(self) -> None:

        self.resBois = Ressource("bois")
        self.resDecoration = Ressource("decoration")
        self.resPierre = Ressource("pierre")
        self.resArchitecture = Ressource("architecture")
        self.categA = Categorie("Apprenti", 2)

        self.app1 = Ouvrier(self.categA)
        self.app1.ajouterRessource(self.resBois,1)
        self.app1.ajouterRessource(self.resPierre,1)

    def testOuvrierQuantiteByRessourceProduite(self):
        self.assertEqual(self.app1.quantiteByRessource(self.resBois), 1, "Erreur quantite sur ressource produite")

    def testOuvrierQuantiteByRessourceNonProduite(self):
        self.assertEqual(self.app1.quantiteByRessource(self.resArchitecture), 0, "Erreur quantite sur ressource non produite")


if __name__ == '__main__':
    unittest.main()