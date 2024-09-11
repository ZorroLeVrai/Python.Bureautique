import os

repertoire = r"C:\Users\Amine"
fichier = "text.txt"

chemin_complet = os.path.join(repertoire, fichier)
print(chemin_complet)