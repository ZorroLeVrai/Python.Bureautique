MESSAGE_SAISIE = "Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie): "

def saisir_une_note():
    while True:
        note_str = input(MESSAGE_SAISIE)
        try:
            note = float(note_str)
            if note > 20:
                print("Veuillez saisir un nombre inférieur ou égal à 20")
            else:
                return note
        except ValueError:
            print("Veuillez saisir un nombre entier ou un nombre décimal")

def saisir_notes():
    notes = []
    note = 0
    while note >= 0:
        note = saisir_une_note()
        if note >= 0:
            notes.append(note)
    
    return notes


liste_notes = saisir_notes()
if len(liste_notes) == 0:
    print("Aucune note saisie")
    exit()

print("Note minimale:", min(liste_notes))
print("Note maximale:", max(liste_notes))
print("Note moyenne:", sum(liste_notes) / len(liste_notes))
