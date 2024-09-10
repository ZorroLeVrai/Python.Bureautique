class Piece:
    def __init__(self, nom, largeur, longueur):
        self.nom = nom
        self.largeur = largeur
        self.longueur = longueur

    def surface(self):
        return self.largeur * self.longueur;

    def dimension(self):
        return f"largeur={self.largeur}, longeur:{self.longueur}"


chambre = Piece("chambre 1", 2.9, 3.1)
salon = Piece("salon", 3, 5)

print(chambre.nom)
print(chambre.surface())
print(chambre.dimension())

print(salon.nom)
print(salon.surface())
print(salon.dimension())
