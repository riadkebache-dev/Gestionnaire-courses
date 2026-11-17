def lancer_liste_courses():
    # Notre dictionnaire pour stocker les courses : { "aliment": quantité }
    liste_courses = {}

    print("--- Bienvenue dans votre gestionnaire de courses ---")

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Afficher la liste")
        print("2. Ajouter ou modifier un aliment")
        print("3. Supprimer un aliment")
        print("4. Quitter")

        choix = input("Votre choix (1-4) : ")

        if choix == "1":
            # Affichage de la liste
            if not liste_courses:
                print("\nVotre liste est actuellement vide.")
            else:
                print("\n--- Votre liste de courses ---")
                for aliment, quantite in liste_courses.items():
                    print(f"- {aliment} : {quantite}")

        elif choix == "2":
            # Ajouter ou rectifier un aliment
            aliment = input("Nom de l'aliment (ex: pommes) : ").strip().lower()
            try:
                quantite = int(input(f"Quantité pour '{aliment}' : "))
                liste_courses[aliment] = quantite
                print(f"-> Succès : {quantite} {aliment} enregistré(s).")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide pour la quantité.")

        elif choix == "3":
            # Supprimer un aliment
            aliment = input("Nom de l'aliment à supprimer : ").strip().lower()
            if aliment in liste_courses:
                del liste_courses[aliment]
                print(f"-> '{aliment}' a été retiré de la liste.")
            else:
                print(f"-> '{aliment}' n'est pas dans la liste.")

        elif choix == "4":
            print("\nÀ bientôt et bon shopping !")
            break
        else:
            print("Choix invalide, veuillez choisir entre 1 et 4.")

# Lancer le programme
lancer_liste_courses()
