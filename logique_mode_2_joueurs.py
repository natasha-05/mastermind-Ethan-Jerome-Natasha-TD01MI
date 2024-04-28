

# Définition de la fonction pour compter les pions mal placés
def couleur_mal_placees(code_secret, proposition):
    mal_placees = 0
    code_copy = list(code_secret)  
    
    
    for pion in proposition:
        
        if pion in code_copy:
            mal_placees += 1  
            code_copy.remove(pion)  
    
    # Après avoir parcouru la proposition, nous ignorons les pions bien placés
    for i in range(len(proposition)):
        if proposition[i] == code_secret[i]:
            mal_placees -= 1
    
    return max(0, mal_placees)



# Définition de la fonction pour comparer la proposition avec le code secret
def compare(code_secret, proposition):
    couleurs_bien_placees = 0
    for i in range(len(code_secret)):
        if code_secret[i] == proposition[i]: 
            couleurs_bien_placees += 1  
    
    
    print(couleurs_bien_placees, "couleurs bien placées.")

    
    print(couleur_mal_placees(code_secret, proposition), "couleurs mal placées.")


choix_couleur = ["white", "blue", "green", "yellow", "pink", "purple", "orange", "black"] 
code_secret = []  # Liste pour stocker le code secret

# Fonction pour que le Joueur 1 entre le code secret
def J1():
    for i in range(4):
        J1 = input("Joueur 1, entrez le code secret : ")
        code_secret.append(J1) 
        
    print("Code secret : XXXX")  
    J2()  

# Fonction pour que le Joueur 2 décode le code secret
def J2():
   
    nombre_tentatives = 0
    
    # Boucle pour permettre au Joueur 2 de déchiffrer le code secret
    while nombre_tentatives < 10:  # Limite à 10 tentatives
        proposition = []  
        for i in range(4):
            J2 = input("Joueur 2, décodez : ")  
            proposition.append(J2) 
        print(proposition)  
        
        nombre_tentatives += 1  
        
        compare(code_secret, proposition)  
        
        # Vérifie si la proposition est correcte
        if proposition == code_secret:
            print("BRAVO !!! Vous avez décodé.")  
            return  
    

    print("Vous avez utilisé toutes vos tentatives. Le code secret était :", code_secret)


J1()
