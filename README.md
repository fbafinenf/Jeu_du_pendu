# Jeu du Pendu
 
**Fabien Koch - KOCF83320301**
MGA802 - Sujets spéciaux I en aéronautique (É2026)
 
## Objectif
 
Ce projet est une version en Python du jeu du pendu. Le joueur doit deviner un mot lettre par lettre avant de perdre ses 6 vies. Une fonction d'indice est disponible à la dernière vie.
 
## Utilisation
 
1. Lancer `Jeu du pendu.py` avec Python 
2. Fournir le chemin (path) vers votre propre fichier `.txt` de mots, **ou** appuyer sur `Entrée` pour utiliser le fichier par défaut (`mots_pendu.txt`)
3. Suivre les instructions affichées dans le terminal pour jouer
4. Note : Le mot à deviner ne comporte aucun accent ni cédille.
 
## Structure du code
 
Le programme est organisé en fonctions indépendantes appelées séquentiellement par `jeu_pendu()` :
 
| Fonction | Rôle |
|---|---|
| `enlever_accents(texte)` | Normalise les caractères accentués |
| `charger_mots()` | Charge la liste de mots depuis un fichier `.txt` |
| `choix_mot(mots_pendu)` | Sélectionne un mot aléatoire |
| `demander_lettre()` | Valide et récupère la saisie du joueur |
| `affichage_mot(...)` | Affiche le mot avec `_` pour les lettres non trouvées |
| `victoire(...)` | Vérifie si toutes les lettres ont été trouvées |
| `indice(...)` | Suggère une lettre absente du mot |
| `rejouer()` | Propose de rejouer ou quitter en fin de partie |
| `jeu_pendu()` | Boucle principale du jeu |
 
## Contenu du dépôt
 
- `Jeu du pendu.py` — Code principal du jeu
- `mots_pendu.txt` — Liste de mots utilisée par défaut
- `README.md` — Ce fichier
## Références
 
- Liste des lettres accentuées françaises : [french.stackexchange.com](https://french.stackexchange.com/questions/32589/les-lettres-accentu%C3%A9es-de-la-langue-fran%C3%A7aise)

