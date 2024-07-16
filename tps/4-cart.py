def Menu():
    print("""Choisissez parmi les 5 options suivantes: 

1- Ajouter un article dans le panier
2- Supprimer un article du panier
3- Afficher tous les articles 
4- Vider le panier
5- Quitter""")

while True:
    Menu()
    choix = input("Quel est votre choix? ")
    if choix.isdigit() and int(choix) in range(1, 6):
        C = int(choix)    
        if C == 1:
            print("**L'article a été bien ajouté dans votre panier**")
        elif C == 2:
            print("**L'article a été bien supprimé de votre panier**")
        elif C == 3:
            print("**Voici la liste des articles dans votre panier**")
        elif C == 4:
            print("**Votre panier a bien été supprimé**")
        elif C == 5:
            print("**Merci pour votre visite!!!**")
            break
        else:
            print("Mauvaise entrée, veuillez entrer une valeur entre 1 et 5.")

