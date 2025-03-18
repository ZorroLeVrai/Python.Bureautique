from openpyxl import Workbook

#Créez un nouveau workbook et sélectionnez la feuille de calcul active
wb = Workbook()
ws = wb.active

#Ecriture de la valeur "Hello" dans la cellule C3
ws["C3"] = "Hello"

#Enregistrez le workbook dans un fichier Excel
excel_path = "output.xlsx"
wb.save(excel_path)

print(f"Le fichier Excel '{excel_path}' a été généré avec succès avec 'Hello' dans C3!")
