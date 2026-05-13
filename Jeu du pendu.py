import random

#on commence par définir toutes les fonctions

with open("mots_pendu.txt", "r") as file:     #création d'une liste avec les mots du fichier.txt
    mots_pendu = file.read().splitlines()

def choix_mot(mots_pendu):   #fonction pour choisir un mot aléatoire dans la liste de mots
    return random.choice(mots_pendu)

def demander_lettre():      #fonction pour demande une lettre à l'utilisateur
    while True:
        lettre= input("Choisir une lettre: ")
        if len(lettre) != 1:                         #vérifie si l'utrilisateur ne met que un unique charactère
            print("Veuillez entrer une seule lettre")
        elif not lettre.isalpha():                       #vérifie que l'utilisateur choisi bien une lette (et pas un chiffre ou charactère spécial)
            print("Entrez des lettres seulement")
        else:
            return lettre.lower()      #le lower permet d'avoir que des minuscules comme dans le fichier.txt, si jamais le jouer choisi une lettre majuscule

def affichage_mot(mot_aleatoire, lettre_trouvees):    #fonction qui affiche le mot avec les underscores _ _ _ _ ...
    affichage = ""
    for lettre in mot_aleatoire:        #on circule entre les lettres du mot
        if lettre in lettre_trouvees:          #si c'est une lettre du mot, on l'affiche à la place de son _
            affichage += lettre + " "      #on place la lettre
        else:
            affichage += "_ "               #tant que la lettre n0est pas encore toruvée on laisse le _
    print(affichage)

def victoire(mot_aleatoire, lettre_trouvees):     #pour dire si le joueur a gagné ou pas
    for lettre in mot_aleatoire:
        if lettre not in lettre_trouvees:
            return False
    return True


print(" --- Bienvenue sur le Jeu du pendu --- ")

def jeu_pendu():
    mot_aleatoire = choix_mot(mots_pendu)  # sélection du mot aléatoire et assigner ce mot a une variable
    chances = 6                  #variable du nombre de vies
    lettre_trouvees = []        #liste qui contiendra les lettres sélectionées pas l'utilisateur
    lettre_deja_choisies = []     #liste les lettres deja selectionées par le joueur


    while chances > 0:                  #boucle principale du jeu
        print("\n")               #saut de ligne
        print("Mot à trouver : ")
        affichage_mot(mot_aleatoire, lettre_trouvees)

        print("Vie restantes : ", chances)                         #affichage
        print("Lettre déjà testées : ", lettre_deja_choisies)

        lettre = demander_lettre()                       #on demande une nouvelle lettre

        if lettre in lettre_deja_choisies:                 #test si la lettre est déjà choisi
            print("Cette lettre à déjà été testée")
            continue

        lettre_deja_choisies.append(lettre)   #ajoute la nouvelle lettre choisi à la liste des lettre deja testées

        if lettre in mot_aleatoire:
            print("Bonne lettre !")
            lettre_trouvees.append(lettre)
        else:
            print("Mauvaise lettre !")
            chances -= 1

        if victoire(mot_aleatoire,lettre_trouvees):     #en cas de victoire !!!
            print("Victoire !")
            print("Le bon mot était : ", mot_aleatoire)

            return


    print("Défaite... Vouc avez perdu !")          #en cas de défaite...
    print("Le bon mot était : ", mot_aleatoire)

jeu_pendu()   #on lance le jeu
