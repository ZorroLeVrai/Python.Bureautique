from exemple_classe_2 import Piece

class Appartement:
    def __init__(self, nom):
        self.nom = nom
        self.pieces_dico = dict()

    def ajouter_piece(self, piece):
        self.pieces_dico[piece.nom] = piece

    def supprimer_piece(self, nom_piece):
        del self.pieces_dico[nom_piece]

    def surface(self):
        return sum(map(lambda piece:piece.surface(), self.pieces_dico.values()))
    

appart1 = Appartement("Appart 1")

appart1.ajouter_piece(Piece("Salon", 3, 5))
appart1.ajouter_piece(Piece("Chambre", 2.5, 3.5))

print(appart1.pieces_dico)
print(appart1.surface())
