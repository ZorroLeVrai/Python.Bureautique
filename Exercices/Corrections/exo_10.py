from os.path import exists

nom_fichier = "secret.txt"

def lire_secret():
    if not exists(nom_fichier):
        return ""
    
    with open(nom_fichier, "r") as fichier:
        return fichier.read()


def ecrire_secret(secret):
    with open(nom_fichier, "w") as fichier:
        fichier.write(secret)

secret = lire_secret()

while True:
    option = input("""Choisir une action
        1: Voir le secret
        2: Modifier le secret
        3: Quitter le programme
        """)

    match option:
        case "1":
            print(f"Le secret est: \"{secret}\"")
        case "2":
            secret = input("Saisir le secret: ")
        case "3":
            ecrire_secret(secret)
            print ("Au revoir")
            break

print("Fin du programme")