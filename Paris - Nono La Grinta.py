import sys
import time
from pygame import mixer  # pip install pygame
from rich import print
from time import sleep

start_time = time.time()

# === Paroles complètes avec timestamps approximatifs et char_delay pour l'effet karaoké ===
lyrics = [
    (0,"...",16.00),
    (0.0, "C'est bientôt la fin", 0.05),
    (2.0, "J'ai braqué la drill comme un assassin", 0.05),
    (4.0, "J'suis dans la ville, j'touche pas la SACEM", 0.05),
    (6.0, "J'ai mis les voiles, les condés, j'les sens", 0.05),
    (8.0, "Débouler à n'importe quel moment", 0.05),
    (10.0, "J'suis défoncé, j'ai bu toute la téquila", 0.05),
    (12.0, "Dégouté quand ça parle pas gros montants", 0.05),
    (14.0, "Casque Arai, tu sais pas, c'est qui là", 0.05),
    (16.0, "Elle aime les réputés pour la vente de crack", 0.05),
    (18.0, "Tu connais mon triangle, la zone a du crack", 0.05),
    (20.0, "J'visser un che-ri, puis j'visser un crack (puis j'visser un crack)", 0.05),
    (22.0, "A-a amitié gâchée par rapport au fric", 0.05),
    (24.0, "J'achète un pétard, j'le mets sous mon froc", 0.05),
    (26.0, "En espérant pas croiser les flics (croiser les flics)", 0.05),
    (28.0, "Y-y il m'faut du fric et une grosse villa", 0.05),
    (30.0, "La copilote recompte mes mapessas", 0.05),
    (32.0, "Parle pas avec eux, ils sont trop pressés (ils sont trop pressés)", 0.05),
    (34.0, "On est trop précis, on va t'filocher, puis on va procéder", 0.05),
    (36.0, "Les fans pensent que j'suis possédé, j'étais dans l'block", 0.05),
    (38.0, "Maintenant j'vends des CD's", 0.05),
    (40.0, "Paris, c'est magique, j'aime trop ma ville, ça bouge de tous les côtés", 0.05),
    (42.0, "Grosse bécane levée sur le périph'", 0.05),
    (44.0, "La bavette, elle est frottée", 0.05),
    (46.0, "J'me balade dans la caille, ta copine demande une photo", 0.05),
    (48.0, "J'm'en rappelle, elle faisait des manières", 0.05),
    (50.0, "La rue, c'est noire, c'est soit l'oseille ou la mort", 0.05),
    (52.0, "C'est soit l'oseille ou la mort", 0.05),
    (54.0, "J'suis parisien comme Mbappé", 0.05),
    (56.0, "Viens par ici y a c'qu'il faut pour se droguer", 0.05),
    (58.0, "Ici, t'es paresseux, tu restes chez toi", 0.05),
    (60.0, "Il m'faut un petit peu d'déter tous les soirs", 0.05),
    (62.0, "J'fume la frappe de Rotter' dans le square", 0.05),
    (64.0, "Faut venir me dead, pour que j'perde espoir", 0.05),
    (66.0, "J'suis def', j'l'ai démontée dans la baignoire", 0.05),
    (68.0, "J'ai perdu la boule, elle a enlevé son peignoir", 0.05),
    (70.0, "La-la, la daronne ne voulait pas que j'traîne le soir", 0.05),
    (72.0, "J'ai trop fait d'erreur, j'peux pas rater ma chance", 0.05),
    (74.0, "Le pilon me tabasse le crâne tous les soirs", 0.05),
    (76.0, "Où-où sont mes ennemis?", 0.05),
    (78.0, "Ramenez-les-moi, j'vais les boire", 0.05),
    (80.0, "Y-y il m'faut du fric et une grosse villa", 0.05),
    (82.0, "La copilote recompte mes mapessas", 0.05),
    (84.0, "Parle pas avec eux, ils sont trop pressés", 0.05),
    (86.0, "On est trop précis, on va te filocher, puis on va procéder", 0.05),
    (88.0, "Les fans pensent que j'suis possédé, j'étais dans l'block", 0.05),
    (90.0, "Maintenant j'vends des CD", 0.05),
    (92.0, "Paris, c'est magique, j'aime trop ma ville, ça bouge de tous les côtés", 0.05),
    (94.0, "Grosse bécane levée sur le périph'", 0.05),
    (96.0, "La bavette, elle est frottée", 0.05),
    (98.0, "J'me balade dans la caille, ta copine demande une photo", 0.05),
    (100.0, "J'm'en rappelle, elle faisait des manières", 0.05),
    (102.0, "La rue, c'est noire, c'est soit l'oseille ou la mort", 0.05),
    (104.0, "C'est soit l'oseille ou la mort", 0.05),
    (106.0, "Paris, c'est magique, j'aime trop ma ville, ça bouge de tous les côtés", 0.05),
    (108.0, "Grosse bécane levée sur le périph'", 0.05),
    (110.0, "La bavette, elle est frottée", 0.05),
    (112.0, "J'me balade dans la caille ta copine demande une photo", 0.05),
    (114.0, "J'm'en rappelle, elle faisait des manières", 0.05),
    (116.0, "La rue, c'est noire, c'est soit l'oseille ou la mort", 0.05),
    (118.0, "C'est soit l'oseille ou la mort", 0.05),
    (120.0, "C'est soit l'oseille ou la mort", 0.05),
    (122.0, "C'est soit l'oseille ou la mort", 0.05),
]

# === Affichage lettre par lettre ===
for timestamp, line, char_delay in lyrics:
    while time.time() - start_time < timestamp:
        sleep(0.01)
    for char in line:
        if char in "()":
            print(f"[orange4]{char}[/orange4]", end='')
        else:
            print(f"[bold][gold3]{char}[/gold3][/bold]", end='')
        sys.stdout.flush()
        sleep(char_delay)
    print()  # saut de ligne
