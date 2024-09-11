class Piece:
    def __init__(self, nom, largeur, longueur):
        self.nom = nom
        self.largeur = largeur
        self.longueur = longueur

    def surface(self):
        return self.largeur * self.longueur;

    def dimension(self):
        return f"largeur={self.largeur}, longeur:{self.longueur}"
    
    def __repr__(self) -> str:
        return f"[{self.nom} ({self.largeur} X {self.longueur})]"
    

class Appartement:
    def __init__(self, nom):
        self.nom = nom
        self.pieces = dict()

    def ajouter_piece(self, piece):
        self.pieces[piece.nom] = piece

    def supprimer_piece(self, nom_piece):
        del self.pieces[nom_piece]

    def surface(self):
        return sum(map(lambda piece:piece.surface(), self.pieces.values()))
    

appart1 = Appartement("Appart 1")

appart1.ajouter_piece(Piece("Salon", 3, 5))
appart1.ajouter_piece(Piece("Chambre", 2.5, 3.5))

print(appart1.pieces)
print(appart1.surface())
