class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        #Le livre est disponible par défaut
        self.disponible = True
    
    def afficher_informations(self):
        print(f"Titre : {self.titre}")
        print(f"Auteur : {self.auteur}")
        if self.disponible:
            print("Statut : Disponible")
        else:
            print("Statut : Emprunté")
        print()
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.titre}' est déjà emprunté.")
    
    def rendre(self):
        if not self.disponible:
            self.disponible = True
            print(f"Le livre '{self.titre}' a été rendu.")
        else:
            print(f"Le livre '{self.titre}' est déjà disponible.")



# Créer des objets (des livres)
livre1 = Livre("1984", "George Orwell")
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
livre3 = Livre("L'Alchimiste", "Paulo Coelho")

# Emprunter des livres
livre1.emprunter()
livre2.emprunter()

# Essayer d'emprunter un livre déjà emprunté
livre1.emprunter()

# Rendre un livre
livre1.rendre()

# Essayer de rendre un livre déjà disponible
livre1.rendre()

# Afficher à nouveau les informations après les modifications
livre1.afficher_informations()
livre2.afficher_informations()
