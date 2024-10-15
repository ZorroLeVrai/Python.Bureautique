from notes import Notes

message_saisie = "Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie): "

def saisir_une_note():
    while True:
        note_str = input(message_saisie)
        try:
            note = float(note_str)
            if note > 20:
                print("Veuillez saisir un nombre inférieur ou égal à 20")
            else:
                return note
        except ValueError:
            print("Veuillez saisir un nombre entier ou un nombre décimal")

notes = Notes()
while True:
    note = saisir_une_note()
    if note >= 0:
        notes.ajouter_note(note)
    else:
        break

print("Note minimale:", notes.min())
print("Note maximale:", notes.max())
print("Note moyenne:", notes.moyenne())