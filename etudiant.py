class Etudiant:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def afficher(self):
        return f"Etudiant: {self.nom} {self.prenom}, ID: {self.id}"


class GestionEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
        print("Etudiant ajoute avec succes.")