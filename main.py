import turtle as trtl
import random
import time

wn = trtl.Screen()
wn.bgcolor('black')
wn.screensize()
wn.setup(width = 1.0, height = 1.0)

class Shell():
    def __init__(self, location, turtle, hasPearl = False):
        turtle.goto(location)

        self.hasPearl = hasPearl
        self.location = location
        self.turtle = turtle

def showPearl(shell, pearlTurtle):
    if(shell.hasPearl == True):
        pearlTurtle.goto(shell.location)
        pearlTurtle.showturtle()
        time.sleep(1)
        pearlTurtle.hideturtle()

def startGame():
    print('What difficulty do you want to play on: \n 1) Easy \n 2) Medium \n 3) Hard \n 4) Insane')
    difficulty = int(input())
    print('Number of shells: \n 3 \n 4 \n 5')
    shells = int(input())

    pearlTurtle = trtl.Turtle()
    pearlTurtle.hideturtle()
    pearlTurtle.penup()
    pearlTurtle.color('palegoldenrod')
    pearlTurtle.shape('circle')
    pearlTurtle.turtlesize(5)


    space = (1600/(shells - 1))
    x = -800

    shellList = []
    for _ in range(shells):

        turtle = trtl.Turtle()
        turtle.color('green')
        turtle.shape('turtle')
        turtle.turtlesize(10)
        turtle.penup()
        turtle.setheading(90)

        newShell = Shell( (x, -100), turtle, pearlTurtle)
        shellList.append(newShell)
        x += space


    pearl = random.choice(shellList)
    pearl.hasPearl = True

    shellList[0].turtle.onclick(lambda x,y: showPearl(shellList[0], pearlTurtle))
    shellList[1].turtle.onclick(lambda x,y: showPearl(shellList[1], pearlTurtle))
    shellList[2].turtle.onclick(lambda x,y: showPearl(shellList[2], pearlTurtle))

    showPearl(pearl, pearlTurtle)

startGame()
wn.mainloop()
