temperature = float(input("Entrez la température de l'eau: "))

if temperature < 0:
    etat_eau = "SOLIDE"
elif temperature <= 100:
    etat_eau = "LIQUIDE"
else:
    etat_eau = "GAZEUX"

print("Etat de l'eau:", etat_eau)
