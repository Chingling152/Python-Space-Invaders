import turtle

class Character:

    speed: int
    alive: bool
    body: turtle.Turtle

    def __init__(self,x,y,speed,color,sprite):
        self.alive = True
        self.body = turtle.Turtle()
        self.speed = speed
        # criando o corpo
        self.body.color(cor)
        self.body.shape(sprite)
        self.body.penup()
        self.body.speed(0)
        self.body.setposition(x,y)
        self.body.setheading(90)

    def move(self,direction):
        self.body.setheading(direction)
        self.body.forward(self.speed)


class Player(Character):

    lifes : int
    score : int

    def __init__(self,x,y,speed,color,sprite):
        self.lifes = 3
        self.score = 0
        Character.__init__(self,x,y,speed,color,sprite)


