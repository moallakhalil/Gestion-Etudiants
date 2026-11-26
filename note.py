class Note:
    def __init__(self, matiere, valeur):
        self.matiere = matiere
        self.valeur = valeur

    def afficher(self):
        return f"Matiere: {self.matiere}, Note: {self.valeur}"