import unittest

from categorie import Categorie
from ressource import Ressource


class testOuvrierCout(unittest.TestCase):
    def setUp(self) -> None:
        self.pierre = Ressource("pierre")
        self.pierre = Ressource("bois")

        self.categorieManoeuvre = Categorie("Manoeuvre", 3.0)
        self.categorieApprenti = Categorie("Apprenti", 2.0)

if __name__ == '__main__':
    unittest.main()
