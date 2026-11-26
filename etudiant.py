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
    def supprimer_etudiant(self, id):
        for etudiant in self.etudiants:
            if etudiant.id == id:
                self.etudiants.remove(etudiant)
                print("Etudiant supprime avec succes.")
                return

        print("Etudiant introuvable.")
    def afficher_etudiants(self):
        for etudiant in self.etudiants:
            print(etudiant.afficher())