salaires = [15000, 17500, 12000, 27000, 19500]

AUGMENTATION_TAUX = 0.05
SEUIL_SALAIRE = 20000

salaires_augmente = map(lambda salaire:(1+AUGMENTATION_TAUX)*salaire, salaires)
salaires_inferieur = filter(lambda salaire:salaire<SEUIL_SALAIRE, salaires_augmente)

print(list(salaires_inferieur))