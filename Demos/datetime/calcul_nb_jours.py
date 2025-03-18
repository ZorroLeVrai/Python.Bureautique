from datetime import datetime

FORMAT_DATE = "%d/%m/%Y"  # Format attendu (DD/MM/YYYY)

# Fonction pour calculer la différence entre deux dates
def calculer_nb_jours(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, FORMAT_DATE)
    date2 = datetime.strptime(date_str2, FORMAT_DATE)
    return abs((date2 - date1).days)  # Renvoie la différence en jours (valeur absolue)

# Demande à l'utilisateur de saisir les dates
date1 = input("Entrez la première date (JJ/MM/AAAA) : ")
date2 = input("Entrez la deuxième date (JJ/MM/AAAA) : ")

# Calcul et affichage du résultat
jours = calculer_nb_jours(date1, date2)
print(f"Le nombre de jours entre {date1} et {date2} est de {jours} jours.")
