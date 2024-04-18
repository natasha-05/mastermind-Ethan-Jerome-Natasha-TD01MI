
from random import *

choix_couleur = ["white", "blue", "green", "yellow", "pink", "purple", "orange", "black", "v", "w", "x"] 
code_secret = []

for i in range(4):
    indice_couleur = randint(0, len(choix_couleur) - 1) #correspond au indices des couleurs dans la liste
    couleur_choisie = choix_couleur[indice_couleur]
    code_secret.append(couleur_choisie)
    
print("Code secret :", code_secret)


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