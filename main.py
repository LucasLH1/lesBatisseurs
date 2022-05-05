from fonctions import afficherListe
from outil import Outil
from ouvrier import Ouvrier
from categorie import Categorie
from ressource import Ressource
from batiment import Batiment
from affranchi import Affranchi
from chantier import Chantier

pierre = Ressource("pierre")
bois = Ressource("bois")
architecture = Ressource("architecture")
decoration = Ressource("decoration")

la_pyramide = Batiment("La Pyramide", 18, 8)
chantier1 = Chantier(la_pyramide)

categorieMaitre = Categorie("Maître", 5.0)
categorieCompagnon = Categorie("Compagnon", 4.0)
categorieManoeuvre = Categorie("Manoeuvre",3.0)
categorieApprenti = Categorie("Apprenti",2.0)

outil1 = Outil("Scie",bois)


ouvrier1 = Ouvrier("Ouahibrê")
ouvrier2 = Affranchi("Ptahâa",categorieApprenti)
ouvrier3 = Affranchi("Amenemheb",categorieManoeuvre)
listeOuvriers = [ouvrier1, ouvrier2, ouvrier3]

if __name__ == '__main__':
    print("Bienvenue dans le jeu des Batisseurs.\n")
    listeOuvriers[0].ajouterRessource(pierre,1)
    listeOuvriers[0].ajouterRessource(bois,1)
    listeOuvriers[1].ajouterRessource(pierre,1)
    listeOuvriers[1].ajouterRessource(bois,1)

    listeOuvriers[2].ajouterRessource(pierre,1)
    listeOuvriers[2].ajouterRessource(bois,2)
    listeOuvriers[2].ajouterRessource(architecture,2)
    ouvrier3.equiperOutil(outil1)

    la_pyramide.ajouterRessource(pierre, 4)
    la_pyramide.ajouterRessource(bois, 4)
    la_pyramide.ajouterRessource(architecture, 4)
    la_pyramide.ajouterRessource(decoration, 4)
    print(la_pyramide)

    chantier1.envoyerTravaillerOuvrier(listeOuvriers[0])
    print(chantier1.getListeOuvriers())