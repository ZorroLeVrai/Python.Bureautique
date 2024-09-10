def entrer_2_entiers():
    try:
        entier1 = int(input("Entrez entier 1: "))
        entier2 = int(input("Entrez entier 2: "))
        return (entier1, entier2)
    except Exception as err:
        print("Erreur de saisie")
        print(err)
        return None


entiers = entrer_2_entiers()
if entiers:
    val1, val2 = entiers
    print(val1)
    print(val2)
else:
    print("Pas de valeurs")
