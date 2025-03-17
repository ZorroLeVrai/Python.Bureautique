def concatener_prenom_nom(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.upper()}"

prenom = input("Entrez votre prénom: ")
nom = input("Entrez votre nom: ")
print(concatener_prenom_nom(prenom, nom))