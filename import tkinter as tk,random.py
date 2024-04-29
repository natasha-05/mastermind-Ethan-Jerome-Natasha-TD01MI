import tkinter as tk,random
from tkinter.simpledialog import messagebox

fenetre = tk.Tk()
fenetre.title("Mastermind")
#fenetre.configure(bg = 'white')
boutons_affiches = [] #-->liste de tous les boutons affichés à l'écran pour pouvoir les effacer quand on change d'interface
compteur_2_joueur = 0 #--> permet de savoir quel mode le joueur choisi
position_x = 0 #--> pour connaitre l'abscisse du cercle
position_y = 0 #--> pour connaitre l'ordonnée du cercle
liste_essai = [] #--> prend les couleurs rentrées par le joueur
hauteur_cercle = 1 #--> pour placer les cercles noir et blanc en face du code_essai
cercles_code_secret = [] #--> permet que le mode 2 joueur n'augmente pas le compteur cercles_code
code_secret_2_joueur = [] #--> le code secret si l'on passe par 2 joueur
cercles_code = [] #--> Liste pour stocker les cercles de la proposition du joueur
code_secret_1_joueur = [] #--> le code secret si l'on passe par un joueur
code_secret = [] #--> le code secret général

nombre_indice = 0 #--> le nombre de fois où l'on clique sur le bouton indice


banque_couleur = ['red', 'blue', 'green', 'yellow','cyan','magenta','darkorange','purple','grey','brown'] #--> stock toutes les couleurs possibles du jeu

couleur = [] #--> Liste pour stocker les couleurs disponibles

fin = 0 #--> permet que si le jeu se termine alors on ne peu plus toucher a la grille




# permet de naviguer dans le menu, de changer les options et de choisir le mode de jeu
def afficher_menu(confirmation = True):
    """Affiche l'interface du menu
    confirmation : booléen déterminiant s'il faut afficher une boîte de dialogue pour confirmer le retour au menu"""
    global bouton_1j, bouton_2j, boutons_affiches, bouton_jouer, choix_nb_pions, choix_nb_couleurs, choix_nb_essais, instructions, instructions_params,texte_nb_pions, texte_nb_couleurs, texte_nb_essais,banque_couleur,couleur,compteur_2_joueur,position_x,position_y,nombre_indice,fin
    #Affiche une autre fenetre pour prévenir le joueur
    if confirmation and not messagebox.askokcancel("Mastermind", "Si vous retournez au menu,\nvotre partie en cours sera perdue.", icon = "warning", master = fenetre):
        return
    
    # Suppression de tous les widgets précédemment affichés
    [widg.grid_remove() for widg in boutons_affiches]


    #initialisation variable
    code_secret.clear()
    liste_essai.clear()
    couleur.clear()
    compteur_2_joueur = 0 
    position_x = 0
    position_y = 0
    nombre_indice = 0
    fin = 0

    # Texte 
    instructions = tk.Label(text = "Choisissez si vous voulez jouer seul (l'ordinateur choisit le code à trouver)\nou à 2 (l'un choisit le code et l'autre le devine)")
    instructions.grid(row = 0, column = 0, columnspan = 3, pady = 10) # Place le Texte

    #Bouton type radio pour le mode joueur 1
    nombre_joueurs = tk.IntVar(value = 1)
    bouton_1j = tk.Radiobutton(text = "1 joueur", variable = nombre_joueurs, value = 1)
    bouton_1j.grid(row = 1, column = 0, pady = 10) # Place le bouton sur la grille

    #Bouton type radio pour le mode joueur 2
    bouton_2j = tk.Radiobutton(text = "2 joueurs", variable = nombre_joueurs, value = 2)
    bouton_2j.grid(row = 1, column = 2, pady = 10) # Place le bouton sur la grille

    # Texte
    instructions_params = tk.Label(text = "Vous pouvez également configurer ces paramètres avant de lancer la partie")
    instructions_params.grid(row = 2, column = 0, columnspan = 3, pady = (50, 10)) # Place le Texte

    # Texte
    texte_nb_pions = tk.Label(text = "Nombre de pions du code")
    texte_nb_pions.grid(row = 3, column = 0, padx = 20) # Place le texte sur la grille

    # Texte
    texte_nb_couleurs = tk.Label(text = "Nombre de couleurs différentes")
    texte_nb_couleurs.grid(row = 3, column = 1, padx = 20) # Place le texte sur la grille

    # Texte
    texte_nb_essais = tk.Label(text = "Nombre d'essais maximum")
    texte_nb_essais.grid(row = 3, column = 2, padx = 20) # Place le texte sur la grille

    # Bouton type Scale pour choisir le nombre de point dans le code
    choix_nb_pions = tk.Scale(orient = "horizontal", cnf = {"from": 3}, to = 8, bg = 'maroon',fg = 'white')
    choix_nb_pions.grid(row = 4, column = 0) # Place le bouton sur la grille
    choix_nb_pions.set(5) # Initilie la valeur 



    # Bouton type Scale pour choisir le nombre de couleur disponible pour le code
    choix_nb_couleurs = tk.Scale(orient = "horizontal", cnf = {"from": 3}, to = 9,bg = 'maroon',fg = 'white')
    choix_nb_couleurs.grid(row = 4, column = 1) # Place le bouton sur la grille
    choix_nb_couleurs.set(6) # Initilie la valeur 

    # Bouton type Scale pour choisir le nombre d'essai pour résoudre le code
    choix_nb_essais = tk.Scale(orient = "horizontal", cnf = {"from": 6}, to = 12,bg = 'maroon',fg = 'white')
    choix_nb_essais.grid(row = 4, column = 2) # Place le bouton sur la grille
    choix_nb_essais.set(6) # Initilie la valeur 

    #Bouton pour lancer la partie
    bouton_jouer = tk.Button(text = "Jouer !", command = lambda: lancer_partie() if nombre_joueurs.get() == 1 else choisir_code())
    bouton_jouer.grid(row = 5, column = 1, pady = 50) # Place le bouton sur la grille

    #Liste des widgets affichés
    boutons_affiches = [bouton_1j, bouton_2j, bouton_jouer, choix_nb_pions, choix_nb_couleurs, choix_nb_essais, instructions, instructions_params, texte_nb_pions, texte_nb_couleurs, texte_nb_essais]


# choix du code secret pour mode 2 joueurs
def choisir_code():
    global boutons_affiches, canvas,instructions,cercles_code, couleur, cercles_code_secret,compteur_2_joueur
    [widg.grid_remove() for widg in boutons_affiches] # Supprime tous les widgets présent

    # Texte
    instructions = tk.Label(text = "Choisissez le code secret")
    instructions.grid(row = 0, column = 0, pady = 10) # Place le texte sur la grille

    # Création du canvas
    canvas = tk.Canvas(fenetre, width = 1000, height = 600, bg = 'burlywood', highlightbackground='saddlebrown')
    canvas.grid(row = 1, column = 0, columnspan = 5, padx = 25) # Place le canvas sur la grille

    compteur_2_joueur += 1 # --> permet que code_secret prenne la liste créée dans cette fonction

    for j in range(choix_nb_couleurs.get()): # permet que la liste couleur est le même nombre de couleur que nb_choix_couleur
        couleur.append(banque_couleur[j])

    canvas.create_rectangle(45,45,105,55 + choix_nb_couleurs.get() * 50, fill = 'maroon') # créer rectangle autour couleur

    canvas.create_rectangle(145,45,125 + choix_nb_pions.get() * 80 ,105, fill = 'maroon')  # créer rectangle autour des pions

    for i in range(choix_nb_couleurs.get()): # créer un nombre de cercle en fonction de la longueur du code
        y0 = 50 + i * 50
        y1 = 100 + i * 50
        cercle_couleur = canvas.create_oval(50, y0, 100, y1, fill=couleur[i])
        
        canvas.tag_bind(cercle_couleur, "<Button-1>", couleur_selectionnee_code_secret) # Lier l'événement de clic à chaque cercle de couleur

    ligne = [] #--> liste vide pour 

    for l in range(choix_nb_pions.get()): # créer les cerlce et les ajoute a une liste, ce qui permet et de changer leur couleur et de pouvoir comparer la liste à liste_essai
        cercle = canvas.create_oval(150 + l * 80, 50, 200 + l * 80, 100, fill='white')
        ligne.append(cercle)
    cercles_code_secret.append(ligne) 

    boutons_affiches = [canvas,instructions] # Widgets affichés
    


# sors du menu, et lance le mastermind
def lancer_partie():

    "Affiche l'interface de la partie"
    global boutons_affiches, bouton_annuler, bouton_charger, bouton_indice, bouton_menu, bouton_sauvegarder,cercles,ligne,canvas,instructions,code_secret,couleur,compteur_2_joueur,code_secret_2_joueur,cercles_code_secret,position_x,position_y,hauteur_cercle

    [widg.grid_remove() for widg in boutons_affiches] # Efface tous les widgets

    hauteur_cercle = 1 #--> au cas ou si joueur retourne au menu en pleine partie

    for i in range(choix_nb_couleurs.get()): # permet que la liste couleur est le même nombre de couleur que nb_choix_couleur
        couleur.append(banque_couleur[i])

    code_secret_1_joueur = random.choices(couleur, k = choix_nb_pions.get()) # créer le code secret pour mode 1 joueur

    if compteur_2_joueur == 1 : 
        code_secret = code_secret_2_joueur # si mode 2 joueur
        cercles = cercles_code_secret
    else :
        code_secret = code_secret_1_joueur # si mode 1 joueur

    # Texte
    instructions = tk.Label(text = "Trouvez le code secret en {} essais maximum !".format(choix_nb_essais.get()), bg = 'maroon', fg = 'white')
    instructions.grid(row = 0, column = 0, columnspan = 5, pady = 20) # Place le texte sur la grille

    # Bouton pour retourner au menu
    bouton_menu = tk.Button(text = "Retour au menu", command = afficher_menu,bg = 'maroon',fg = 'white')
    bouton_menu.grid(row = 3, column = 0) # Place le bouton sur la grille

    # Bouton pour sauvegarder la partie en cours
    bouton_sauvegarder = tk.Button(text = "Sauvegarder", bg = 'maroon',fg = 'white',command = save_jeu)
    bouton_sauvegarder.grid(row = 3, column = 1) # Place le bouton sur la grille

    # Bouton pour charger une partie
    bouton_charger = tk.Button(text = "Charger la partie", bg = 'maroon',fg = 'white',command = load_jeu)
    bouton_charger.grid(row = 3, column = 2) # Place le bouton sur la grille

    # Bouton pour donner une indice
    bouton_indice = tk.Button(text = "Indice", command = indice, bg = 'maroon',fg = 'white')
    bouton_indice.grid(row = 3, column = 3) # Place le bouton sur la grille

    # Bouton pour annuler le dernier coup
    bouton_annuler = tk.Button(text = "Annuler coup", command = annuler,bg = 'maroon',fg = 'white')
    bouton_annuler.grid(row = 3, column = 4) # Place le bouton sur la grille

    # Créer un canvas
    canvas = tk.Canvas(fenetre, width = 1560, height = 725,bg='burlywood', highlightbackground='saddlebrown')
    canvas.grid(row = 1, column = 0, columnspan = 5, padx = 25) # Place le canvas sur la grille


    canvas.create_rectangle(45,45,105,55 + choix_nb_couleurs.get() * 50, fill = 'maroon') # créer rectangle autour couleur

    canvas.create_rectangle(145,45,125 + choix_nb_pions.get() * 80 ,30 + choix_nb_essais.get() * 75, fill = 'maroon')  # créer rectangle autour des pions

    canvas.create_rectangle(95 + choix_nb_pions.get() * 128,45,155 + choix_nb_pions.get() * 128 + (choix_nb_pions.get() - 1) * 55,105, fill = 'maroon')  # créer rectangle autour indice

    canvas.create_text(187+ choix_nb_pions.get() * 128,25,text = 'Indice :',font=("Courier", 30),fill = 'black')

    canvas.create_text( 240,15,text = 'Noir : couleur correcte et bien placée',font=("Courier", 15),fill = 'black')

    canvas.create_text( 240,30,text = 'Blanc : couleur correcte et mal placée',font=("Courier", 15),fill = 'black')


    for i in range(choix_nb_couleurs.get()): # Créer les ronds de couleurs
        y0 = 50 + i * 50
        y1 = 100 + i * 50
        cercle_couleur = canvas.create_oval(50, y0, 100, y1, fill=couleur[i])
        
        canvas.tag_bind(cercle_couleur, "<Button-1>", couleur_selectionnee)# Lier l'événement de clic à chaque cercle de couleur

        cercles = [] # -->Création des cercles blancs pour les essais

    for k in range(choix_nb_essais.get()): # créer tous les ronds blancs, et les rentres dans une liste pour pouvoir les comparer
        ligne = []
        x0 = 150
        y0 = 50 + k * 75
        x1 = 200
        y1 = 100 + k * 75
        for l in range(choix_nb_pions.get()):
            cercle = canvas.create_oval(x0 + l * 80, y0, x1 + l * 80, y1, fill='white')
            ligne.append(cercle)
        cercles.append(ligne)

    # liste les widgets affichés
    boutons_affiches = [instructions, canvas, bouton_menu, bouton_sauvegarder, bouton_charger, bouton_indice, bouton_annuler]


# Fonction qui se passe lorsque l'on clique sur un cercle pour choisir le code
def couleur_selectionnee_code_secret(event):
    global position_x, position_y,hauteur_cercle, code_secret_2_joueur,cercles_code_secret

    couleur = canvas.itemcget(tk.CURRENT, "fill")  # --> Récupérer la couleur du cercle cliqué

    canvas.itemconfig(cercles_code_secret[position_y][position_x], fill=couleur)  # Mettre à jour la couleur du cercle sélectionné
    
    position_x += 1 # -->Passer à la position suivante

    code_secret_2_joueur.append(canvas.itemcget(tk.CURRENT, "fill")) # récupère les couleurs rentrées par le joueur

    if len(code_secret_2_joueur) == choix_nb_pions.get():  # lorsque tous les ronds ont été rempli
        position_x = 0 #--> réinitilialise postition_x car on y a touché
        lancer_partie() # appelle la fonction


# Compare les couleur mal placée avec le code secret
def couleur_mal_placees():
    global couleur_mal_place,code_secret,liste_essai

    couleur_mal_place = 0 # --> initialise la variable
    code_copy = list(code_secret)  # Copie du code secret
    
    # Parcourez chaque pion de la proposition
    for pion in liste_essai:
        # Vérifiez si le pion est dans le code secret et mal placé
        if pion in code_copy:
            couleur_mal_place += 1  # Incrémente le nombre de pions mal placés
            code_copy.remove(pion)  # Supprime le pion du code secret copié pour ne pas le compter à nouveau
    
    # Après avoir parcouru la proposition, nous ignorons les pions bien placés
    for i in range(len(liste_essai)):
        if liste_essai[i] == code_secret[i]:
            couleur_mal_place -= 1



# Définition de la fonction pour comparer la proposition avec le code secret
def compare():
    global couleur_bien_place, liste_essai, code_secret
    couleur_bien_place = 0 # --> initialise la variable
    for i in range(len(code_secret)):
        if code_secret[i] == liste_essai[i]:  # Si la couleur est bien placée
            couleur_bien_place += 1  # Incrémente le nombre de couleurs bien placées

    couleur_mal_placees()


# Fonction qui s'active lorsque l'on clique sur un cercle pour essayer de trouver code secret
def couleur_selectionnee(event):
    global position_x, position_y,hauteur_cercle, liste_essai,couleur_bien_place,couleur_mal_place,fin

    if fin == 1: # Lorsque le jeu est fini, pour ne plus pouvoir interagir avec le canva
        return
    
    #initialise les variables, au cas ou le joueur retourne au menu pendant que le code n'est pas complété entièrement
    couleur_bien_place = 0 
    couleur_mal_place = 0

    couleur = canvas.itemcget(tk.CURRENT, "fill")  # --> Récupérer la couleur du cercle cliqué

    canvas.itemconfig(cercles[position_y][position_x], fill=couleur)  # Mettre à jour la couleur du cercle sélectionné
    
    position_x += 1 # -->Passer à la position suivante

    liste_essai.append(canvas.itemcget(tk.CURRENT, "fill")) # liste_essai récupère la couleur du cercle

    if position_x == choix_nb_pions.get():  # Si nous avons atteint la fin de la ligne
        position_x = 0
        position_y += 1
        if position_y == choix_nb_essais.get():  # Si nous avons atteint la fin de la grille
            position_y = 0
            position_x = 0
   
    if len(liste_essai) == choix_nb_pions.get() : # si une ligne a été rempli entièrement

        compare() # compare code_secret et liste_essai

        cercle_noir(couleur_bien_place,hauteur_cercle) # trace les ronds noir

        cercle_blanc(couleur_mal_place,hauteur_cercle) # trace les ronds blanc

        hauteur_cercle += 1

        liste_essai.clear() # Réinitialise la liste_essai pour la ligne suivante

        if couleur_bien_place == choix_nb_pions.get() : # Si le code est bon
            fin_gagnant() # Appelle la fonction 

    if choix_nb_essais.get() == hauteur_cercle - 1: # Si le joueur n'a plus d'essai
        fin_perdant() # Appelle la fonction


# Foction qui s'active si le joueur trouve le code secret
def fin_gagnant(): 
    global fin
    x0 = 265 + choix_nb_pions.get() * 128
    y0 = 350
    canvas.create_text(x0,y0,text = 'Gagné !',font=("Courier", 60),fill = 'black') # Crée un texte de victoire
    fin += 1 # permet de ne plus pouvoir cliquer sur les ronds de couleur du canvas


# Foction qui s'active si le joueur ne trouve pas le code secret
def fin_perdant(): 
    global code_secret,fin
    x2 = 265 + choix_nb_pions.get() * 128
    y2 = 350
    canvas.create_text(x2,y2,text = 'Perdu !',font=("Courier", 60),fill = 'black') # Crée un texte de défaite 
    canvas.create_text(320+ choix_nb_pions.get() * 128,565,text = 'Le code a trouver était :',font=("Courier", 30),fill = 'black')
    canvas.create_rectangle(95 + choix_nb_pions.get() * 128,595,100 + choix_nb_pions.get() * 128 + choix_nb_pions.get() * 55,655, fill = 'maroon')
    for i in range(len(code_secret)):
        x0 = 100 + choix_nb_pions.get() * 128
        x1 = 150 + choix_nb_pions.get() * 128
        y0 = 600
        y1 = 650
        canvas.create_oval(x0 + i * 55,y0,x1+ i * 55,y1,fill = code_secret[i]) # Dessine le code secret
    fin += 1 # permet de ne plus pouvoir cliquer sur les ronds de couleur du canvas


# Trace le même nombre de cercle noir que de couleur bien placée
def cercle_noir(nb,hauteur): # Trace les ronds noir, une couleur bien placée
    x0 = 150 + choix_nb_pions.get() * 80
    x1 = 175 + choix_nb_pions.get() * 80
    y0 = hauteur * 75 - 30
    y1 = hauteur * 75 - 30
    for j in range(nb):
        canvas.create_oval(x0 + j * 25 , y0 + 25 , x1 + j * 25, y1 + 50, fill='black')


# Trace le même nombre de cercle blanc que de couleur mal placée mais correct
def cercle_blanc(nb2,hauteur): # Trace les ronds blanc, une couleur mal placée mais correct
    x0 = 150 + choix_nb_pions.get() * 80
    x1 = 175 + choix_nb_pions.get() * 80
    y0 = hauteur * 75 - 60
    y1 = hauteur * 75 - 60
    for j in range(nb2):
        canvas.create_oval(x0 + j * 25 , y0 + 25 , x1 + j * 25, y1 + 50, fill='white')    

def load_jeu():
    global choix_nb_couleurs, choix_nb_essais, choix_nb_pions, code_secret
    file = open("mastermind save.txt", "r", encoding="utf8")
    choix_nb_couleurs, choix_nb_essais, choix_nb_pions = [int(_) for _ in file.readline().split(",")]
    code_secret = file.readline().rstrip().split(",")
    liste_essai.clear()
    for line in file:
        liste_essai.append(line.rstrip().split(","))
    file.close()

def save_jeu():
    file = open("mastermind save.txt", "w", encoding="utf8")
    file.write(",".join((str(choix_nb_essais), str(choix_nb_pions), str(choix_nb_couleurs))))
    file.write("\n")
    file.write(",".join(code_secret))
    for tentative in liste_essai:
        file.write("\n")
        file.write(",".join(tentative))
    file.close()



def indice(): # Révèle la première couleur du code
    global nombre_indice
    x0 = 100 + choix_nb_pions.get() * 128
    x1 = 150 + choix_nb_pions.get() * 128
    y0 = 50
    y1 = 100
    canvas.create_oval(x0 + nombre_indice * 55, y0, x1 + nombre_indice * 55, y1,fill = code_secret[nombre_indice] )
    nombre_indice += 1



def annuler(): # Permet de revenir en arrière
    global position_y,choix_nb_pions,cercles,hauteur_cercle
    position_y_2 = position_y #permet de pouvoir remonter d'une ligne tout en blanchissant 
    position_x = 0
    for i in range(choix_nb_pions.get()): # change la couleur des cercles de la ligne en blanc
        position_x = i
        canvas.itemconfig(cercles[position_y_2-1][position_x], fill='white')
    x0 = 150 + choix_nb_pions.get() * 80
    x1 = 175 + choix_nb_pions.get() * 80
    y0 = hauteur_cercle * 75 - 110
    y1 = hauteur_cercle * 75 - 50
    canvas.create_rectangle(x0,y0,x1 + choix_nb_pions.get() * 25,y1,fill = 'burlywood',outline = 'burlywood') # Cache les cercles noir et blanc
    position_y -= 1
    hauteur_cercle -= 1





afficher_menu(False)
# Definition des fonction de sauvegarde et de chargement de la partie
# Fonction de chargement de la partie


fenetre.mainloop()