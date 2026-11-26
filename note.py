class Note:
    def __init__(self, matiere, valeur):
        self.matiere = matiere
        self.valeur = valeur

    def afficher(self):
        return f"Matiere: {self.matiere}, Note: {self.valeur}"


class GestionNotes:
    def __init__(self):
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)
        print("Note ajoutee avec succes.")
    def afficher_notes(self):
        for note in self.notes:
            print(note.afficher())
    def calculer_moyenne(self):
        if not self.notes:
            return 0

        total = sum(note.valeur for note in self.notes)
        return total / len(self.notes)