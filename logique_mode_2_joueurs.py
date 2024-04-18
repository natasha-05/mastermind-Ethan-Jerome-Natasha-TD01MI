
 #le joueur1 forme son code secret
                 
choix_couleur = ["white", "blue", "green", "yellow", "pink", "purple", "orange", "black", "v","w","x"] 
code_secret = []


for i in range(4):
 
    J1 = (input("joueur1 Entrez le code secret : "))
    if J1 in choix_couleur:
        code_secret.append(J1)
    else:
        print("Couleur invalide. Veuillez entrer une couleur dans la palette proposée.")

print("Code secret :", code_secret)  # par la suite Affiche une chaîne de caractères à la place du code secret avec XXXX

#joueur 2 décode
decode = []

for i in range(4):
 
    J2 = (input("joueur2 décodez  : "))
    if J2  in choix_couleur:
        decode.append(J2)
    else:
        print("Couleur invalide. Veuillez entrer une couleur dans la palette proposée.")

#INDICE:    
    
#verifie si les couleurs sont bien placé
def compare(code_secret,decode):

    couleurs_bien_placees = 0
   

    for i in range(len(code_secret)):
        if code_secret[i] == decode[i]:
            couleurs_bien_placees += 1  
    print(couleurs_bien_placees, "couleurs bien placées.")
        
# somme des couleur mal placé
     
    couleur_mal_place = 0
    
    
    for i, element in enumerate(code_secret):
            if decode[i] != element :
                couleur_mal_place += 1

    print(couleur_mal_place," couleur mal placé ")
            
        
compare(code_secret,decode)