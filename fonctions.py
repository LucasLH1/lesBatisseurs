from typing import List


def afficherListe(liste: List[object]) -> None:
    """
    Permet d'afficher le contenu d'une liste
    :param liste: liste d'objets
    """
    for i in range(len(liste)):
        print(str(liste[i]))