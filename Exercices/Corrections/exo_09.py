def compter_lettre_a(texte):
    nb_lettres = 0
    for lettre in texte.upper():
        if lettre == "A":
            nb_lettres += 1
    return nb_lettres

def compter_lettre_a2(texte):
    return texte.count('a')

print(compter_lettre_a("abba"))
print(compter_lettre_a("mixer"))