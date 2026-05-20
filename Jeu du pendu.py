#Fabien Koch - KOCF83320301
#Jeu du pendu
#MGA802
#Ce projet est une version en Python du jeu du pendu. Le joueur doit deviner un mot lettre par lettre avant de perdre ses 6 vies. Une fonction d'indice est disponible à la dernière vie.

import random

#on commence par définir toutes les fonctions

def enlever_accents(texte):         #pour enlever tout les accents
    accents = {'a': ['à','â','æ','ä'],        #dictionnaire crée avec la page internet suivante : https://french.stackexchange.com/questions/32589/les-lettres-accentu%C3%A9es-de-la-langue-fran%C3%A7aise
               'e': ['é','è','ê','ë'],
               'i': ['î','ï','ì'],
               'o': ['ô','œ','ò'],
               'u': ['ù','û','ü'],
               'c': ['ç']}
    for sans_accent, avec_accent in accents.items():
        for lettre in avec_accent:
            texte = texte.replace(lettre, sans_accent)        #remplacement des lettres par celles sans accents
    return texte

def charger_mots():
    fichier = input("Veuillez entrer le path de votre fichier de mots, OU appuyez sur 'Entrée' pour utiliser le fichier de mots par défaut : ").strip()     #le .strip() permet d'enlever les espaces au cas ou l'utilisateur appuis sur espace avant d'entrer, pour que la condition du programme après fonctionne toujours
    if fichier == "":           # s'il n'y a rien, on utilise le fichier par défaut d'après
        fichier = "mots_pendu.txt"    #on utilise le fichier par défaut
    try:
        with open(fichier, "r", encoding="utf-8") as file:     #création d'une liste avec les mots du fichier.txt (utf8 par sécurité)
            return file.read().splitlines()                   #on associe chaque ligne (grace au splitlines()) du fichier à un mot
    except FileNotFoundError:                     #si le fichier avec le path de l'utilisateur est introuvable
        print("Votre fichier est introuvable, le fichier par défaut va être utilisé")
        with open("mots_pendu.txt", "r", encoding="utf-8") as file:
            return file.read().splitlines()

mots_pendu = charger_mots()   #on est obliger d'appeler la fonction pour charger la liste de mots

def choix_mot(mots_pendu):   #fonction pour choisir un mot aléatoire dans la liste de mots
    z = random.choice(mots_pendu)     #on choisi un mot aléatoire dans la liste
    return enlever_accents(z).lower()          #le lower permet d'avoir que des minuscules

def demander_lettre():      #fonction pour demande une lettre à l'utilisateur
    while True:
        lettre= input("Choisir une lettre: ")
        lettre = enlever_accents(lettre)                #appel à la fonction pour enlever les accents
        if len(lettre) != 1:                         #vérifie si l'utrilisateur ne met que un unique charactère
            print("Veuillez entrer une seule lettre")
        elif not lettre.isalpha():                       #vérifie que l'utilisateur choisi bien une lette (et pas un chiffre ou charactère spécial)
            print("Entrez des lettres seulement")
        else:
            return lettre.lower()      #le lower permet d'avoir que des minuscules comme dans le fichier.txt, si jamais le jouer choisi une lettre majuscule

def affichage_mot(mot_aleatoire, lettre_trouvees):    #fonction qui affiche le mot avec les underscores _ _ _ _ ...
    affichage = ""             #on commence avec rien
    for lettre in mot_aleatoire:        #on circule entre les lettres du mot
        if lettre in lettre_trouvees:          #si c'est une lettre du mot, on l'affiche à la place de son _
            affichage += lettre + " "      #on place la lettre avec un espace après pour améliorer la lisibilité
        else:
            affichage += "_ "               #tant que la lettre n0est pas encore toruvée on laisse le _
    print(affichage)

def victoire(mot_aleatoire, lettre_trouvees):     #pour dire si le joueur a gagné ou pas
    for lettre in mot_aleatoire:
        if lettre not in lettre_trouvees:                  #tant que toutes les lettres ne sont pas trouvées, le jeu n'est pas gagné
            return False
    return True

def rejouer():
    while True:
        choix = input("Voulez-vous recommencer ou quitter ? (répondre r ou q)")
        if choix == "r":
            return jeu_pendu() and True       #permet de continuer le jeu
        elif choix == "q":
            return False               #arrête le jeu
        else:
            print("Veuillez entrer r ou q")

def indice(mot_aleatoire, lettre_deja_choisies):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")                           #on liste toutes les lettres de l'alphabet
    for lettre in mot_aleatoire:                                      #on enlève toutes les lettres du mot à notre alphabet
        if lettre in alphabet:
            alphabet.remove(lettre)   #on va enlever toutes les lettres du mots des options de lettre de l'indice
    for lettre in lettre_deja_choisies:
        if lettre in alphabet:
            alphabet.remove(lettre)     #ici on enlève les lettres deja choisi par l'utilisateur des options d'indice
    if alphabet:
        indice = random.choice(alphabet)       #ainsi, on ne peut que donner un indice d'une lettre qui n'est pas deja choisi ou qui n'est pas dans le mot
        print("Indice : la lettre", indice, "ne fait pas partie du mot")
    return alphabet

def jeu_pendu():
    print(" --- Bienvenue sur le Jeu du pendu --- ")
    print("\n")
    print("ATTENTION : Le mot à trouver ne comporte aucun accent ou cédille")
    mot_aleatoire = choix_mot(mots_pendu)  # sélection du mot aléatoire et assigner ce mot a une variable
    chances = 6                  #variable du nombre de vies
    lettre_trouvees = []        #liste qui contiendra les lettres sélectionées pas l'utilisateur
    lettre_deja_choisies = []     #liste les lettres deja selectionées par le joueur

    while chances > 0:                  #boucle principale du jeu
        print("\n")               #saut de ligne
        print("Mot à trouver : ")
        affichage_mot(mot_aleatoire, lettre_trouvees)         #on affiche l'état du mot à trouver avec les lettres deja trouvées

        print("Vie restantes : ", chances)                         #affichage des vies restantes
        print("Lettre déjà testées : ", lettre_deja_choisies)          #affichage de la liste de lettres restantes à trouver

        lettre = demander_lettre()                       #on demande une nouvelle lettre

        if lettre in lettre_deja_choisies:                 #test si la lettre est déjà choisi
            print("Cette lettre à déjà été testée")
            continue

        lettre_deja_choisies.append(lettre)   #ajoute la nouvelle lettre choisi à la liste des lettre deja testées

        if lettre in mot_aleatoire:
            print("Bonne lettre !")
            lettre_trouvees.append(lettre)          #on ajoute la lettre au mot avec les _ pour l'affichage
        else:
            print("Mauvaise lettre !")
            chances -= 1                 #perte d'une vie si lettre fausse

        if victoire(mot_aleatoire,lettre_trouvees):     #en cas de victoire !!!
            print("Victoire !")
            print("Le bon mot était : ", mot_aleatoire)
            return rejouer()
        if chances == 1:                  #cas particulier de la dernière vie avec indice possible
            while True:
                choix = input("Voulez-vous in indice ? (répondre oui ou non)")      #demande à l'utilisateur
                if choix == "oui":
                    indice(mot_aleatoire, lettre_deja_choisies)          #donne une lettre qui n'est pas dans le mot avec appel à la fonction indice
                    break                                              #permet de sortir de là sous boucle
                elif choix == "non":
                    break
                else:
                    print("Veuillez entrer oui ou non")                #si l'utilisateur ne répond pas oui ou non

    print("Défaite... Vous avez perdu !")          #en cas de défaite...
    print("Le bon mot était : ",mot_aleatoire)
    return rejouer()    #ramène à la fonction rejouer pour permettre de rejouer ou quitter

jeu_pendu()   #on lance le jeu complet
