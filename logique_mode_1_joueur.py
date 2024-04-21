 from random import *

choix_couleur = ["white", "blue", "green", "yellow", "pink", "purple", "orange", "black"] 
code_secret = []

for i in range(4):
    indice_couleur = randint(0, len(choix_couleur) - 1) #correspond au indices des couleurs dans la liste
    couleur_choisie = choix_couleur[indice_couleur]
    code_secret.append(couleur_choisie)
    
print("Code secret :XXXX" )


#joueur 2 décode
proposition = []

for i in range(4):

    J2 = (input("joueur2 décodez  : "))
    proposition.append(J2)
    

#INDICE:    
    

#Compte le nombre de lettres étrangères dans une proposition par rapport au code secret.
def couleur_etrangees(code_secret, proposition):
    
    couleur_etrangees = 0
    for lettre in proposition:
        if lettre not in code_secret:
            couleur_etrangees += 1
    return couleur_etrangees


def couleur_mal_placees(code_secret, proposition):
    mal_placees = 0
    couleur_utilisees = []  # Liste pour stocker les couleurs déjà vérifiées
    for i in range(len(code_secret)):
        if proposition[i] != code_secret[i] and proposition[i] in code_secret and proposition[i] not in couleur_utilisees:
            mal_placees += 1
            couleur_utilisees.append(proposition[i])  # Ajouter la couleur vérifiée à la liste
    return mal_placees




def compare(code_secret, proposition):
    couleurs_bien_placees = 0
    for i in range(len(code_secret)):
        if code_secret[i] == proposition[i]:
            couleurs_bien_placees += 1  
    print(couleurs_bien_placees, "couleurs bien placées.")
    
    mal_placees = couleur_mal_placees(code_secret, proposition)
   
    print(mal_placees, "couleurs mal placées.")

compare(code_secret, proposition)

if proposition == code_secret:
     print("BRAVO!!! vous avez décodé")
else:
     print("Vous avez perdu.")            

print("Le code secret est :", code_secret)
    

   
