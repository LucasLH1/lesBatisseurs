from fonctions import afficherListe
from outil import Outil
from ouvrier import Ouvrier
from categorie import Categorie
from ressource import Ressource
from batiment import Batiment
from affranchi import Affranchi

pierre = Ressource("pierre")
bois = Ressource("bois")
architecture = Ressource("architecture")
decoration = Ressource("decoration")

ziggourat = Batiment("Le Ziggourat", 14, 5, {pierre : 1, bois : 2, architecture : 3, decoration : 4})

categorieMaitre = Categorie("Maître", 5.0)
categorieCompagnon = Categorie("Compagnon", 4.0)
categorieManoeuvre = Categorie("Manoeuvre",3.0)
categorieApprenti = Categorie("Apprenti",2.0)

outil1 = Outil("Scie",bois,1)

listeOuvriers = [Ouvrier("Ouahibrê"),Affranchi("Ptahâa",categorieApprenti),Affranchi("Amenemheb",categorieManoeuvre)]

if __name__ == '__main__':
    print("Bienvenue dans le jeu des Batisseurs.\nListe des ouvriers : \n")
    listeOuvriers[0].ajouterRessource(pierre,1)
    listeOuvriers[0].ajouterRessource(bois,1)
    listeOuvriers[1].ajouterRessource(pierre,1)
    listeOuvriers[1].ajouterRessource(bois,1)
    listeOuvriers[2].ajouterRessource(pierre,1)
    listeOuvriers[2].ajouterRessource(bois,2)
    listeOuvriers[2].ajouterRessource(architecture,2)
    listeOuvriers[2].equiperOutil(outil1)
    print(afficherListe(listeOuvriers))
    print(listeOuvriers[2].quantiteByRessource(architecture))
    #print(ziggourat)
