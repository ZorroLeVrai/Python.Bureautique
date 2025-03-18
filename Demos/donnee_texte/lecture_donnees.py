import pandas as pd

# Chargement du fichier texte en DataFrame
df = pd.read_csv("personnes.txt", sep="\t")

# Affichage du DataFrame
print(df)
