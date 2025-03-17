from datetime import datetime

date_saisie = input("Entrez une date (jj/mm/aaaa): ")
date = datetime.strptime(date_saisie, "%d/%m/%Y")

if date > datetime.now():
    print("La date saisie est dans le futur.")
elif date < datetime.now():
    print("La date saisie est dans le passé.")
else:
    print("La date saisie est aujourd'hui.")
