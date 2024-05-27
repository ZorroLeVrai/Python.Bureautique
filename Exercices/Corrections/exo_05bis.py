NB_PADDING_CHARS = 5
MAX_FACTOR = 10

print("Affichage d'une table de multiplication de 1 à N")
max_number = int(input("Saisir N: "))

chaine_resultat = ""

# imprimer l'entête
for num in range(1, MAX_FACTOR + 1):
    chaine_resultat += f"{num:{NB_PADDING_CHARS}}"

chaine_resultat += "\n"
# imprimer une ligne de séparation
chaine_resultat += "-"*MAX_FACTOR*NB_PADDING_CHARS
chaine_resultat += "\n"

# imprimer la table de multiplication
for i in range(1, max_number + 1):
    for j in range(1, MAX_FACTOR + 1):
        chaine_resultat +=f"{i*j:{NB_PADDING_CHARS}}"
    chaine_resultat += "\n"

print(chaine_resultat)