message_saisie = "Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie): "

def saisir_une_note():
    while True:
        note = float(input(message_saisie))
        if note > 20:
            print("Veuillez saisir un nombre inférieur ou égal à 20")
        else:
            return note


def saisir_notes():
    note_minimale = 20
    note_maximale = 0
    somme_notes = 0
    nb_notes = 0

    while True:
        note = saisir_une_note()
        if note < 0:
            break
        
        if note < note_minimale:
            note_minimale = note
        if note > note_maximale:
            note_maximale = note
        
        somme_notes += note
        nb_notes += 1

    moyenne = somme_notes / nb_notes if nb_notes > 0 else 0
    return (note_minimale, note_maximale, moyenne)


(note_min, note_max, moyenne) = saisir_notes()
print(f"La note minimale est de {note_min} / 20")
print(f"La note maximale est de {note_max} / 20")
print(f"La moyenne est de {moyenne} / 20")