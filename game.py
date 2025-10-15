from random import randint
import pygame

pygame.init()

HAUTEUR_FENETRE = 600
LARGEUR_FENETRE = 1000

COULEUR_FENETRE = (255, 255, 255)
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))

ARRET_JEU = False

while not ARRET_JEU:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ARRET_JEU = True
                break

# Variables FUSEE
XX_FUSEE = 210
YY_FUSEE = 300
LARGEUR_FUSEE = 88
HAUTEUR_FUSEE = 175
MOUVEMENT_XX_FUSEE = 0

# Variables PLANETES
XX_PLANETE = randint(30, 130)
YY_PLANETE = 20
LARGEUR_PLANETE = 111
HAUTEUR_PLANETE = 80
XX_ENTRE_PLANETES = 350
YY_ENTRE_PLANETE = 125
VITESSE_PLANETES = 3

# Points et divers 
POINTS = 0 
FONT = pygame.font.Font(None, 24)
SCORE = FONT.render("0 points", 1, (255,0,0))

# Images



