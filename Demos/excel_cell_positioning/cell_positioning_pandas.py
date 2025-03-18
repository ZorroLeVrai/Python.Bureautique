import pandas as pd

#Ecriture de la valeur "Hello" dans la cellule C3

# Créez un DataFrame contenant 3 lignes et 3 colonnes
df = pd.DataFrame([["", "", ""], ["", "", ""], ["", "", "Hello"]])

# Save the DataFrame to an Excel file
excel_path = "output.xlsx"
df.to_excel(excel_path, index=False, header=False)

print(f"Le fichier Excel '{excel_path}' a été généré avec succès avec 'Hello' dans C3!")
