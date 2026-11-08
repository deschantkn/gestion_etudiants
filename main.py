"""Gestion des étudiants."""

etudiants = []


def ajouter_etudiant(nom):
    etudiants.append(nom)


if __name__ == "__main__":
    ajouter_etudiant("Alice")
    print(etudiants)
