import turtle

class Character:

    speed: int
    alive: bool
    body: turtle.Turtle
    limit: float

    def __init__(self,x,y,speed,color,sprite,limit):
        self.alive = True
        self.body = turtle.Turtle()
        self.speed = speed
        self.limit = limit
        # criando o corpo
        self.body.color(color)
        self.body.shape(sprite)
        self.body.penup()
        self.body.speed(0)
        self.body.setposition(x,y)
        self.body.setheading(90)

    def move(self):
        x = self.body.xcor() + self.speed
        if(x < self.limit and x > -self.limit):
            self.body.setx(x)
        else:
            self.body.sety(self.body.ycor()-30);
            self.speed = -self.speed

class Enemy(Character):

    limit_y : float

    def __init__(self,x,y,speed,color,sprite,limit,limit_y):
        self.limit_y = limit_y
        Character.__init__(self, x, y, speed, color, sprite, limit)

class Player(Character):

    lifes : int
    score : int

    def __init__(self,x,y,speed,color,sprite,limit):
        self.lifes = 3
        self.score = 0
        Character.__init__(self,x,y,speed,color,sprite,limit)

    def move_left(self):
        x = self.body.xcor() - (2 * self.speed)
        if(x > -self.limit):
            self.body.setx(x)

    def move_right(self):
        x = self.body.xcor() + (2 * self.speed)
        if (x < self.limit):
            self.body.setx(x)
