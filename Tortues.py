import random
import turtle


# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)






# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
turtles = []

michelangelo = turtle.Turtle()
michelangelo.color('orange')
michelangelo.shape('turtle')
michelangelo.up()
michelangelo.goto(-650, 320)
michelangelo.down()
michelangelo.speed(10)
turtles.append(michelangelo)

leonardo = turtle.Turtle()
leonardo.color('deep sky blue')
leonardo.shape('turtle')
leonardo.up()
leonardo.goto(-650, 165)
leonardo.down()
leonardo.speed(10)
turtles.append(leonardo)

raphael = turtle.Turtle()
raphael.color('red')
raphael.shape('turtle')
raphael.up()
raphael.goto(-650, 0)
raphael.down()
raphael.speed(10)
turtles.append(raphael)

splinter = turtle.Turtle()
splinter.color('dark slate gray')
splinter.shape('turtle')
splinter.up()
splinter.goto(-650, -145)
splinter.down()
splinter.speed(10)
turtles.append(splinter)

osef = turtle.Turtle()
osef.color('green')
osef.shape('turtle')
osef.up()
osef.goto(-650, -300)
osef.down()
osef.speed(10)
turtles.append(osef)

# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
# A IMPLEMENTER
joueur1 = input("Prédiction joueur 1: ")
joueur2 = input("Prédiction joueur 2: ")



# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite
# A IMPLEMENTER

end = False
results = []

while not end:
    for t in turtles:
        pos = t.position()
        x = pos[0]
        if (x + 650) < 1300:
            n = random.randint(0, 5)
            t.fd(n)
            if t.position()[0] + 650 >= 1300:
                results.append(turtles.index(t))

    if len(results) == 5:
        end = True



# Comparer les rÃ©sultats de la course avec les pronostics des joueurs
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("La tortue " + str(results[0] + 1) + " a gagné", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()


