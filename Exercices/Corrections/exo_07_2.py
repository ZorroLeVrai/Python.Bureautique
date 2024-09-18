nb_max = int(input("Entrez le nombre maximal: "))

ma_liste = []
nombre_courant = 1

while nombre_courant <= nb_max:
    ma_liste.append(nombre_courant)
    nombre_courant += 2

print(ma_liste)