# Analyse des données du temps passé par utilisateur sur les réseaux sociaux

1. Récupérez les données des fichiers `utilisateurs.csv` et `reseaux_sociaux.csv` respectivement dans des dataframes `df_utilisateurs` et `df_donnees`.  
     Utilisez l'encodage 'latin-1' pour bien gérer les accents.

2. Renommez la colonne `id` du dataframe df_utilisateurs en `id_utilisateur`.

3. Renommez la colonne `id` du dataframe df_donnees en `id_data`.

4. Mergez les 2 dataframes en 1 seul dataframe `df_merge` en utilisant la colonne "adresse IP" pour joindre les 2 dataframes.

5. Calculez le nombre d'heures total passé par utilisateur (utilisez l'id utilisateur).

6. Calculez le nombre d'heures total passé par utilisateur (utilisez le nom et prénom de l'utilisateur).

7. Calculez le nombre d'heures total passé sur chaque réseau social.

8. Au dataframe obtenu précédement, ajoutez le pourcentage de temps passé pour chaque réseau social.

9. Au dataframe `df_merge`, ajoutez une colonne `année de naissance` qui contiendra l'année de naissance de chaque utilisateur (au format int).

10. Créez un tableau croisé dynamique dans lequel on veut afficher le temps passé en moyenne sur chaque réseau social en fonction de l'année de naissance de l'utilisateur.
