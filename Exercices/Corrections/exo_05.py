NB_PADDING_CHARS = 5
MAX_FACTOR = 10

print("Affichage d'une table de multiplication de 1 à N")
max_number = int(input("Saisir N: "))

# imprimer l'entête
for num in range(1, MAX_FACTOR + 1):
    print(f"{num:{NB_PADDING_CHARS}}", end='')

print()
# imprimer une ligne de séparation
print("-"*MAX_FACTOR*NB_PADDING_CHARS)

# imprimer la table de multiplication
for i in range(1, max_number + 1):
    for j in range(1, MAX_FACTOR + 1):
        print(f"{i*j:{NB_PADDING_CHARS}}", end='')
    print()