from etudiant import Etudiant
from note import Note

def afficher_message():
    print("Bienvenue")

# Creation des objets
etudiant1 = Etudiant(1, "Moalla", "Khalil")
note1 = Note("DevOps", 16)

# Affichage
afficher_message()
print(etudiant1.afficher())
print(note1.afficher())