temperature = float(input("Entrez la température de l'eau: "))

if temperature < 0:
    etat_eau = "solide"
elif temperature <= 100:
    etat_eau = "liquide"
else:
    etat_eau = "gazeux"

print("Etat", etat_eau)
