import turtle # on importe la ilbliotheque turtle

turtle.colormode(255) # met le mode de couleur avec les chiffres
t = turtle.Turtle() # on cree une tortrue pour dessiner
# t.hideturtle() # rendre invisble la tortue "t"
e = turtle.Turtle() # on cree un tortue "e"
# e.hideturtle() # rendre invisble la tortue "e"
s = turtle.Screen() # on cree un fentre pour la modifier plus tard

""" On met un titre a la fenetre"""
s.title("BMW M4 GT3 RS - by Amine and Baptiste") # le titre de la fenetre

""" On crée le cadre """
t.penup() # on leve le stylo
t.goto(-260, -260) # aller a ces coordonées
for i in range(4):   # boucle for pour repeter 4 fois la boucle
    t.color("Brown") # on chage la couleur en marron
    t.speed(8) # on change la vitesse sinon c'est trop long
    t.pendown() # on met le stylo en position d'écriture
    t.pensize(18) # on change son epaisseur au stylo
    t.fd(520) # on avance de 520
    t.lt(90) # on tourne a droite de 90°

t.penup() # on leve le stylo
t.goto(-250, -250) # on part a ces coordonées
for i in range(4): # une boucle for pour repeter 4 fois la boucle
    t.speed(8) # on change la vitesse a 8
    t.color("Black") # on change la couleur en noir 
    t.pendown() # on pose le stylo
    t.pensize(5) # on change son épaisseur
    t.fd(500) # on avance de 500
    t.lt(90) # on tourne a droite de 90°
    

t.penup()
t.goto(-270, -270)
for i in range(4):
    t.speed(8)
    t.pendown()
    t.pensize(5)
    t.fd(540)
    t.lt(90)

t.speed(4)
t.goto(-270, -270)
t.pendown()
t.goto(-250, -250)
t.penup()

t.goto(270, -270)
t.pendown()
t.goto(250, -250)
t.penup()

t.goto(270, 270)
t.pendown()
t.goto(250, 250)
t.penup()

t.goto(-270, 270)
t.pendown()
t.goto(-250, 250)
t.penup()

""" On va créer la voiture // Modele : BMW M4 GT3 RS """

e.pensize(2)
t.pensize(2)
t.speed(3)
e.speed(3)
t.penup()
e.penup()
t.goto(0, -120)
e.goto(0, -120)
e.pendown()
t.pendown()
e.fd(200)
t.bk(200)
t.rt(90)
e.lt(90)
e.goto(198, 0)
t.goto(-198, 0)
t.circle(10, -80)
e.circle(10, 80)
t.lt(180)
t.fd(35)
e.fd(35)
t.circle(45, 45)
e.circle(-45, 45)
t.lt(5)
e.rt(5)
t.fd(60)
e.fd(60)
t.circle(-10, 60)
e.circle(10, 60)
t.fd(100)
e.fd(100)

def pare_brise():
    """ On va créer un pare-brise ! """
    t.begin_fill()
    t.fillcolor((31, 30, 30))
    e.begin_fill()
    e.fillcolor((31, 30, 30))
    e.penup()
    t.penup()
    e.goto(0, 23)
    t.goto(0, 23)
    e.pendown()
    t.pendown()
    e.bk(120)
    t.bk(120)
    e.circle(-3, -120)
    t.circle(3, -120)
    e.bk(60)
    t.bk(60)
    e.rt(120)
    t.lt(120)
    e.fd(95)
    t.fd(95)
    e.penup()
    t.penup()
    t.goto(0, 23)
    e.goto(0, 23)
    e.end_fill()
    t.end_fill()

pare_brise()

def g_phares_voiture():
    t.color("dimgrey")
    t.begin_fill()
    t.fillcolor("dimgrey")
    t.speed(10)
    t.penup()
    t.goto(-90, -50)
    t.pensize(3.5)
    t.fd(10)
    t.lt(110)
    t.pendown()
    t.fd(10)
    t.circle(20, 30)
    t.lt(27)
    t.fd(70)
    t.circle(10, 50)
    t.fd(5)
    t.circle(10, 60)
    t.fd(15)
    t.circle(10, 70)
    t.fd(10)
    t.circle(10, 15)
    t.fd(68)
    t.circle(10, 25)
    t.goto(-90, -50) 
    t.end_fill() 
    t.penup() # on leve le stylo

g_phares_voiture()

def d_phares_voiture():
    e.color("dimgrey")
    e.begin_fill()
    e.fillcolor("dimgrey")
    e.speed(10)
    e.penup()
    e.goto(90, -50)
    e.pensize(3.5)
    e.fd(10)
    e.rt(110)
    e.pendown()
    e.fd(10)
    e.circle(-20, 30)
    e.rt(27)
    e.fd(70)
    e.circle(-10, 50)
    e.fd(5)
    e.circle(-10, 60)
    e.fd(15)
    e.circle(-10, 70)
    e.fd(10)
    e.circle(-10, 15)
    e.fd(68)
    e.circle(-10, 25)
    e.goto(90, -50) 
    e.end_fill() 
    e.penup() # on leve le stylo

d_phares_voiture()

def graph():
    """ On va créer les axes """
    e.penup()
    e.color("Red")
    e.pensize(3)
    e.pendown()
    e.goto(0, 0)
    e.goto(0, 300)
    e.goto(0, -600)
    e.goto(0, 0)
    e.goto(300, 0)
    e.goto(-600, 0)
    e.goto(-150, 0)
    e.goto(-150, 10)

graph()

turtle.done()