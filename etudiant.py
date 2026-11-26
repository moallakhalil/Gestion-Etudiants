class Etudiant:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def afficher(self):
        return f"Etudiant: {self.nom} {self.prenom}, ID: {self.id}"