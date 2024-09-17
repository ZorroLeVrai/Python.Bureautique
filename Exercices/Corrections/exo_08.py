def afficher_prenom_nom(prenom, nom):
    return f"{prenom} {nom}"

prenom = input("Entrez votre prénom: ")
nom = input("Entrez votre nom: ")
print(afficher_prenom_nom(prenom, nom))