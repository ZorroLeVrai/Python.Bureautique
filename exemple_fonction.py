def afficher_message(message, nb_etoiles = 10):
    print("*"*nb_etoiles, end="")  # Affiche 10 étoiles
    print(f" {message} ", end="")    # Affiche bonjour
    print("*"*nb_etoiles, end="")   # Affiche 10 étoiles
    print() # Retourner à la ligne


afficher_message("Bonjour")
print("Action 1")
afficher_message("Hello", 8)
print("Action 2")
afficher_message("Hallo", 6)
