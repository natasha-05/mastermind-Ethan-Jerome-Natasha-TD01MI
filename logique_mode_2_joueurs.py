

# Définition de la fonction pour compter les pions mal placés
def couleur_mal_placees(code_secret, proposition):
    mal_placees = 0
    code_copy = list(code_secret)  # Copie du code secret
    
    # Parcourez chaque pion de la proposition
    for pion in proposition:
        # Vérifiez si le pion est dans le code secret et mal placé
        if pion in code_copy:
            mal_placees += 1  # Incrémente le nombre de pions mal placés
            code_copy.remove(pion)  # Supprime le pion du code secret copié pour ne pas le compter à nouveau
    
    # Après avoir parcouru la proposition, nous ignorons les pions bien placés
    for i in range(len(proposition)):
        if proposition[i] == code_secret[i]:
            mal_placees -= 1
    
    return max(0, mal_placees)



# Définition de la fonction pour comparer la proposition avec le code secret
def compare(code_secret, proposition):
    couleurs_bien_placees = 0
    for i in range(len(code_secret)):
        if code_secret[i] == proposition[i]:  # Si la couleur est bien placée
            couleurs_bien_placees += 1  # Incrémente le nombre de couleurs bien placées
    
    # Affiche le nombre de couleurs bien placées
    print(couleurs_bien_placees, "couleurs bien placées.")

    # Appelle la fonction pour compter les couleurs mal placées et affiche le résultat
    print(couleur_mal_placees(code_secret, proposition), "couleurs mal placées.")

# Liste des couleurs disponibles
choix_couleur = ["white", "blue", "green", "yellow", "pink", "purple", "orange", "black"] 
code_secret = []  # Liste pour stocker le code secret

# Fonction pour que le Joueur 1 entre le code secret
def J1():
    for i in range(4):
        J1 = input("Joueur 1, entrez le code secret : ")
        code_secret.append(J1)  # Ajoute la couleur à la liste du code secret
        
    print("Code secret : XXXX")  # Affiche une indication pour le joueur 2
    J2()  # Appelle la fonction pour que le Joueur 2 décode le code secret

# Fonction pour que le Joueur 2 décode le code secret
def J2():
    # Compteur pour suivre le nombre de tentatives
    nombre_tentatives = 0
    
    # Boucle pour permettre au Joueur 2 de déchiffrer le code secret
    while nombre_tentatives < 10:  # Limite à 10 tentatives
        proposition = []  # Liste pour stocker la proposition du joueur 2
        for i in range(4):
            J2 = input("Joueur 2, décodez : ")  # Demande au joueur 2 de déchiffrer chaque couleur
            proposition.append(J2)  # Ajoute la couleur à la proposition
        print(proposition)  # Affiche la proposition
        
        nombre_tentatives += 1  # Incrémente le nombre de tentatives
        
        compare(code_secret, proposition)  # Appelle la fonction pour comparer la proposition avec le code secret
        
        # Vérifie si la proposition est correcte
        if proposition == code_secret:
            print("BRAVO !!! Vous avez décodé.")  # Affiche un message de réussite
            return  # Termine la fonction si le code est trouvé
    
    # Si le joueur a épuisé toutes les tentatives sans trouver le code secret
    print("Vous avez utilisé toutes vos tentatives. Le code secret était :", code_secret)

# Appelle la fonction pour que le Joueur 1 entre le code secret
J1()
