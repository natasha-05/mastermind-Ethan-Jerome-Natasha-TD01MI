

from random import randint

# Fonction pour compter les pions mal placés
def couleur_mal_placees(code_secret, proposition):
    mal_placees = 0
    code_copy = list(code_secret)  
    
    
    for pion in proposition:
        # Vérifiez si le pion est dans le code secret et mal placé
        if pion in code_copy:
            mal_placees += 1 
            code_copy.remove(pion)  
    
    # Après avoir parcouru la proposition, nous ignorons les pions bien placés
    for i in range(len(proposition)):
        if proposition[i] == code_secret[i]:
            mal_placees -= 1
    
    return max(0, mal_placees)

# Fonction pour comparer la proposition avec le code secret
def compare(code_secret, proposition):
    couleurs_bien_placees = 0
    for i in range(len(code_secret)):
        if code_secret[i] == proposition[i]:  
            couleurs_bien_placees += 1  
    
    
    print(couleurs_bien_placees, "couleurs bien placées.")
    
    
    print(couleur_mal_placees(code_secret, proposition), "couleurs mal placées.")

# Liste des couleurs disponibles
choix_couleur = ["white", "blue", "green", "yellow", "pink", "purple", "orange", "black"] 
code_secret = []  # Liste pour stocker le code secret

# Fonction pour que le Joueur 1 entre le code secret
def J1():
    for i in range(4):
        indice_couleur = randint(0, len(choix_couleur) - 1)  
        couleur_choisie = choix_couleur[indice_couleur]  
        code_secret.append(couleur_choisie)  
    print("Code secret : XXXX")  
    J2()  

# Fonction pour que le Joueur 2 décode le code secret
def J2():
    nombre_tentatives = 0  
    
    # Boucle pour permettre au Joueur 2 de déchiffrer le code secret
    while nombre_tentatives < 10:  
        proposition = []  
        for i in range(4):
            proposition.append(input("Joueur 2, décodez : "))  
            
        print(proposition)  
        
        nombre_tentatives += 1  
        
        compare(code_secret, proposition)  
        

        if proposition == code_secret:
            print("BRAVO !!! Vous avez décodé.")  
            return  
    
    
    print("Vous avez utilisé toutes vos tentatives. Le code secret était :", code_secret)


J1()
