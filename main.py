import turtle as trtl
import random
import time

class Shell():
    def __init__(self, location, size, speed, pearlTurtle, hasPearl = False, colour = 'green'):

        turtleShell = trtl.Turtle()
        turtleShell.color(colour)
        turtleShell.shape('turtle')
        turtleShell.turtlesize(size)
        turtleShell.penup()
        turtleShell.goto(location)
        turtleShell.setheading(90)

        self.hasPearl = hasPearl
        self.turtle = turtleShell
        self.location = location



    def showPearl(self, Turtle, x = None,y = None):
        print('test')
        if(self.hasPearl == True):

            pearlx, pearly = self.location

            Turtle.goto(pearlx, pearly)
            Turtle.showturtle()
            time.sleep(1)
            Turtle.hideturtle()



wn = trtl.Screen()
wn.screensize()
wn.screensize()
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor("black")


def startGame():

    pearlTurtle = trtl.Turtle()
    pearlTurtle.hideturtle()
    pearlTurtle.penup()
    pearlTurtle.color('palegoldenrod')
    pearlTurtle.shape('circle')
    pearlTurtle.turtlesize(5)

    print('What difficulty do you want to play on: \n 1) Easy \n 2) Medium \n 3) Hard \n 4) Insane')
    difficulty = int(input())
    print('Number of shells: \n 3 \n 4 \n 5')
    shells = int(input())

    if(difficulty > 4 or shells > 5 or shells < 3):
        return print('One of these numbers is not correct')

    space = (1600/(shells - 1))
    x = -800

    shellList = []
    for inter in range(shells):
        newShell = Shell( (x,-100), 10, 1, pearlTurtle)
        shellList.append(newShell)
        x += space

    pearl = random.choice(shellList)
    pearl.hasPearl = True

    pearl.showPearl(pearlTurtle)
    # pearl.turtle.onclick(print('OwO mama OwO'))
    shellList[0].turtle.onclick(lambda: print('OwO'))


startGame()
wn.mainloop()
