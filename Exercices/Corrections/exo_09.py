def compter_lettre_a(texte):
    nb_lettres = 0
    texte_majuscule = texte.upper()  #ABBA
    for lettre in texte_majuscule:
        if lettre == "A":
            nb_lettres += 1  # nb_lettres = nb_lettres + 1
    return nb_lettres

print(compter_lettre_a("Abba"))
print(compter_lettre_a("mixer"))