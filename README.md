# pokemon

************************************************************les dependaces************************************************

1 - le module Requests :
celle ci permet d'executer des requettes HTTP, elle nous a servie pour la recuperation des images des pockemones via leurs adresse 

2 - le module IO:
celle ci nous a permis de lire la reponse obtenue du requete HTTP, une resultat qui etais encoder 

3 - le module PIL:
le module PIL (PILLOW) nous a servi pour l'affichage des images des pockemones

4 - le module Tkinter:
celle ci est le module qui prends en charge toute les interfaces.

5 - le module Json:
celle ci nous à permis de manipuler le contenue des fichiers json se trouvant dans le dossier db

6 - le module Random
il s'agit du module qui nous apermis de choisir aleatoirement le type d'attaque et le type de defence du pockemone ordinateur

******************************************************comprehenssion generale du jeux:*************************************************************

Au debut du jeu l'utilisateur choisie l'un des pockemones dans la liste de tous les pockemones, l'utilisateur attaque le pockemone 2 en cliquant sur un type d'attaque et l'ordinateur choisie un type pour contre attaque si bien sur il est pas encore mort 

le calcule des point de vie s'effectue comme suit:
    si le type d'attaque et le type de defence se trouve dans le fichier type.json le calcule s'effectue exactement comme s'est indiquer dans le consigne du jeu mais si les types ne corresponds pas alors le calcule ce fais d'une autre façon en prenant compte de l'attaque et de la defence.