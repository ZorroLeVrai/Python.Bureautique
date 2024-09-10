nb_max = int(input("Entrez un nombre: "))

lst = []
nb_courant = 1

while nb_courant <= nb_max:
    lst.append(nb_courant)
    nb_courant += 2

print(lst)
