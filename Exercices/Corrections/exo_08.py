def concatener_prenom_nom(prenom, nom):
    return f"{prenom.capitalize()} {nom.upper()}"

prenom = input("Entrez votre prénom: ")
nom = input("Entrez votre nom: ")
print(concatener_prenom_nom(prenom, nom))