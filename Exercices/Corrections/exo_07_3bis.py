salaires = [15000, 17500, 12000, 27000, 19500]

AUGMENTATION_TAUX = 0.05  #5%
SEUIL_SALAIRE = 20000

salaires_resultats = []
for salaire in salaires:
    # Augmentation de 5%
    salaire = (1+AUGMENTATION_TAUX)*salaire
    if salaire < SEUIL_SALAIRE:
        salaires_resultats.append(salaire)

print(salaires_resultats)