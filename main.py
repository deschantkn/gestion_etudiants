"""Gestion des étudiants."""

etudiants = []


def ajouter_etudiant(nom):
    etudiants.append(nom)


def rechercher_etudiant(terme):
    """Retourne les étudiants dont le nom contient `terme` (insensible à la casse)."""
    terme = terme.lower()
    return [e for e in etudiants if terme in e.lower()]


if __name__ == "__main__":
    ajouter_etudiant("Alice")
    ajouter_etudiant("Bob")
    print(etudiants)
    print(rechercher_etudiant("ali"))
