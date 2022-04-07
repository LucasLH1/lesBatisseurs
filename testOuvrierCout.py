import unittest

from affranchi import Affranchi
from categorie import Categorie
from outil import Outil
from ouvrier import Ouvrier
from ressource import Ressource


class testOuvrierCout(unittest.TestCase):
    def setUp(self) -> None:
        self.pierre = Ressource("pierre")
        self.bois = Ressource("bois")
        self.architecture = Ressource("architecture")
        self.decoration = Ressource("decoration")

        self.categorieMaitre = Categorie("Maître", 5.0)
        self.categorieCompagnon = Categorie("Compagnon", 4.0)
        self.categorieManoeuvre = Categorie("Manoeuvre", 3.0)
        self.categorieApprenti = Categorie("Apprenti", 2.0)

        self.outil1 = Outil("Scie", self.bois, 1)

        self.ouvrier1 = Ouvrier("Ouahibrê")
        self.ouvrier2 = Affranchi("Ptahâa", self.categorieApprenti)
        self.ouvrier3 = Affranchi("Amenemheb", self.categorieManoeuvre)

    def testOuvrierCout(self):
        self.assertEqual(self.ouvrier1.getCout(),0,"Un ouvrier est supposé coûter 0.")

    def testAffranchiCout(self):
        self.assertEqual(self.ouvrier2.getCout(),2.0,"Un affranchi apprenti est supposé coûter 2 sesterces.")
        self.assertEqual(self.ouvrier3.getCout(),3.0,"Un affranchi manoeuvre est supposé coûter 3 sesterces.")


if __name__ == '__main__':
    unittest.main()
