from ouvrier import Ouvrier
from categorie import Categorie
from ressource import Ressource

pierre = Ressource("pierre")
bois = Ressource("bois")
architecture = Ressource("architecture")
decoration = Ressource("decoration")

categorieMaitre = Categorie(5.0, "Maître")
categorieCompagnon = Categorie(4.0, "Compagnon")
categorieManoeuvre = Categorie(3.0, "Manoeuvre")
categorieApprenti = Categorie(2.0, "Apprenti")

ouvrier1 = Ouvrier(categorieMaitre)

if __name__ == '__main__':
    print("\nLes Batisseurs\n--------------\nBienvenue en Egypte , vous êtes un esclavagiste.")
    print(ouvrier1)
    ouvrier1.ajouterRessource(bois, 3)
    ouvrier1.ajouterRessource(pierre, 2)
    ouvrier1.ajouterRessource(architecture, 1)
    ouvrier1.ajouterRessource(decoration, 5)
    print(ouvrier1)