epaisseur_feuille = 0.1
epaisseur_cible = 400*1000
pli = 0

while epaisseur_feuille <= epaisseur_cible:
    epaisseur_feuille = epaisseur_feuille * 2
    pli = pli + 1

print(pli)