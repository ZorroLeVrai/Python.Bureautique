import psycopg2
from psycopg2 import Error

def fetch_users():
    """Impression de tous les utilisateurs de la table public.utilisateurs."""
    try:
        # Paramètres de la connexion
        db_user = 'postgres'
        db_password = 'pass123'
        db_host = '127.0.0.1'
        db_port = '5432'
        db_name = 'postgres'

        # Connect to the PostgreSQL database using a context manager
        with psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name
        ) as connection:

            # Création d'un objet curseur
            with connection.cursor() as cursor:
                select_query = "SELECT * FROM public.utilisateurs;"
                # Exécution de la requête
                cursor.execute(select_query)

                # Récupération de toutes les données
                records = cursor.fetchall()

                # Impression des données de chaque utilisateur
                for row in records:
                    print(row)

    except (Exception, Error) as error:
        print(f"Erreur lors de la connexion à PostgreSQL: {error}")


if __name__ == "__main__":
    fetch_users()
