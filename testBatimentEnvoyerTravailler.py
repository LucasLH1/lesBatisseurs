import unittest

from affranchi import Affranchi
from ressource import Ressource
from categorie import Categorie
from ouvrier import Ouvrier
from batiment import Batiment
from chantier import Chantier


class testBatimentEnvoyerTravaillerOuvrier(unittest.TestCase):

    def setUp(self) -> None:


        self.catManoeuvre = Categorie("Manoeuvre",3)
        self.catApprenti = Categorie("Apprenti",2)
        self.catMaitre = Categorie("Maitre",5)
        self.catCompagnon = Categorie("Compagnon",4)

        self.resBois = Ressource("bois")
        self.resDecoration = Ressource("decoration")
        self.resPierre = Ressource("pierre")
        self.resArchitecture = Ressource("architecture")

        self.mano1 = Affranchi("Hamosis",self.catManoeuvre)
        self.mano1.ajouterRessource(self.resBois,1)
        self.mano1.ajouterRessource(self.resDecoration,2)

        self.compa1 = Affranchi("Djersis",self.catCompagnon)
        self.compa1.ajouterRessource(self.resPierre,1)
        self.compa1.ajouterRessource(self.resArchitecture,3)

        self.ouv1 = Ouvrier("Ahmès")
        self.ouv1.ajouterRessource(self.resPierre,2)
        self.ouv1.ajouterRessource(self.resArchitecture,2)

        self.lePalaisDAssur= Batiment("Le Palais d'Assur", 5, 14)
        self.chantierlePalaisDAssur = Chantier(self.lePalaisDAssur)
        self.lePalaisDAssur.ajouterRessource(self.resPierre,3)
        self.lePalaisDAssur.ajouterRessource(self.resBois,1)
        self.lePalaisDAssur.ajouterRessource(self.resArchitecture,4)
        self.lePalaisDAssur.ajouterRessource(self.resDecoration,2)


    def testBatimentEnvoyerTravaillerOuvrierInSuffisant(self):

        self.chantierlePalaisDAssur.envoyerTravaillerOuvrier(self.mano1)
        self.assertFalse(self.chantierlePalaisDAssur.envoyerTravaillerOuvrier(self.compa1), "Erreur équipe insuffisante")


    def testChantierEnvoyerTravaillerOuvrierSuffisant(self):

        self.chantierlePalaisDAssur.envoyerTravaillerOuvrier(self.mano1)
        self.chantierlePalaisDAssur.envoyerTravaillerOuvrier(self.compa1)
        self.assertTrue(self.chantierlePalaisDAssur.envoyerTravaillerOuvrier(self.ouv1), "Erreur équipe suffisante")



if __name__ == '__main__':
    unittest.main()
