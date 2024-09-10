class Person:
    def __init__(self, prenom, nom, date_naissance):
        self.prenom = prenom
        self.nom = nom
        self.date_naissance = date_naissance
        

def afficher_informations(personne_data):
    print(f"Prénom: {personne_data.prenom}")
    print(f"Nom: {personne_data.nom}")
    print(f"Date de naissance: {personne_data.date_naissance}")
    print(type(personne_data.date_naissance))


personne = Person("John", "Doe", "01/01/2001")
personne2 = Person("Jane", "Doe", "22/22/2012")

print(int(personne))

# afficher_informations(personne)
# print()
# afficher_informations(personne2)
