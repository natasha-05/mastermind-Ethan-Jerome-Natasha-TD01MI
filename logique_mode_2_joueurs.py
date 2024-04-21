# Le joueur1 forme son code secret
choix_couleur = ["white", "blue", "green", "yellow", "pink", "purple", "orange", "black"] 
code_secret = []

for i in range(4):
    J1 = input("Joueur 1, entrez le code secret : ")
    code_secret.append(J1)
    
print("Code secret :", code_secret)  

# Boucle pour les tentatives du joueur 2
for tentative in range(1, 11):
    print("\nTentative", tentative)
    proposition = []  # Initialise la proposition pour chaque tentative

    # Joueur 2 décode
    for i in range(4):
        J2 = input("Joueur 2, décodez : ")
        proposition.append(J2)

    # Fonction pour compter le nombre de lettres étrangères dans la proposition
    def couleur_etrangees(code_secret, proposition):
        couleur_etrangees = 0
        for lettre in proposition:
            if lettre not in code_secret:
                couleur_etrangees += 1
        return couleur_etrangees

    # Fonction pour compter le nombre de couleurs mal placées dans la proposition
    def couleur_mal_placees(code_secret, proposition):
        mal_placees = 0
        couleur_utilisees = []  # Liste pour stocker les couleurs déjà vérifiées
        for i in range(len(code_secret)):
            if proposition[i] != code_secret[i] and proposition[i] in code_secret and proposition[i] not in couleur_utilisees:
                mal_placees += 1
                couleur_utilisees.append(proposition[i])  # Ajouter la couleur vérifiée à la liste
        return mal_placees

    # Fonction pour comparer la proposition avec le code secret
    def compare(code_secret, proposition):
        couleurs_bien_placees = 0
        for i in range(len(code_secret)):
            if code_secret[i] == proposition[i]:  # Si la couleur est bien placée
                couleurs_bien_placees += 1  # Incrémente le nombre de couleurs bien placées
        print(couleurs_bien_placees, "couleurs bien placées.")

        mal_placees = couleur_mal_placees(code_secret, proposition)  # Appel de la fonction pour compter les couleurs mal placées
        print(mal_placees, "couleurs mal placées.")

    # Appel de la fonction pour comparer la proposition avec le code secret
    compare(code_secret, proposition)

    # Vérification si la proposition est égale au code secret
    if proposition == code_secret:
        print("BRAVO !!! Vous avez décodé.")
        break
else:
    print("Vous avez utilisé toutes vos tentatives. Le code secret était :", code_secret)
