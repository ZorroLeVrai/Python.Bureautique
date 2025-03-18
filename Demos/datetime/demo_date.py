from datetime import datetime

FORMAT_DATE = "%d/%m/%Y"  # Format attendu (DD/MM/YYYY)

date_saisie = input("Entrez une date (jj/mm/aaaa): ")
date_utilisateur = datetime.strptime(date_saisie, FORMAT_DATE).date()

date_du_jour = datetime.today().date()

if date_utilisateur > date_du_jour:
    print("La date saisie est dans le futur.")
elif date_utilisateur < date_du_jour:
    print("La date saisie est dans le passé.")
else:
    print("La date saisie est aujourd'hui.")
