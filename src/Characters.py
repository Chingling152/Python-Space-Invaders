import turtle

class Entity:

    speed: int
    alive: bool
    body: turtle.Turtle

    limit_x: float
    limit_y: float

    def __init__(self,x,y,speed,color,sprite,limit_x,limit_y):
        self.alive = True
        self.body = turtle.Turtle()
        self.speed = speed
        self.limit_x = limit_x
        self.limit_y = limit_y
        # criando o corpo
        self.body.color(color)
        self.body.shape(sprite)
        self.body.penup()
        self.body.speed(0)
        self.body.setposition(x,y)
        self.body.setheading(90)

    def move(self):
        self.body.forward(self.speed)

class Enemy(Entity):

    def __init__(self,x,y,speed,color,sprite,limit_x,limit_y):
        Entity.__init__(self, x, y, speed, color, sprite, limit_x,limit_y)

    def move(self):
        x = self.body.xcor() + self.speed
        if(x < self.limit_x and x > -self.limit_x):
            self.body.setx(x)
        else:
            self.body.sety(self.body.ycor()-30)
            self.speed = -self.speed

class Player(Entity):

    lifes : int
    score : int

    def __init__(self,x,y,speed,color,sprite,limit_x,limit_y):
        self.lifes = 3
        self.score = 0
        Entity.__init__(self,x,y,speed,color,sprite,limit_x,limit_y)

    def move_left(self):
        x = self.body.xcor() - (2 * self.speed)
        if(x > -self.limit_x):
            self.body.setx(x)

    def move_right(self):
        x = self.body.xcor() + (2 * self.speed)
        if (x < self.limit_x):
            self.body.setx(x)

    def shoot(self):
        bullet = Bullet(self.body.xcor(),self.body.ycor(),self.limit_x,self.limit_y)

class Bullet(Entity):

    def __init__(self,x,y,limit_x,limit_y):
        self.body.shapesize(0.5,0.5)
        Entity.__init__(self,x=x,y=y,speed=5,color="yellow",sprite="triangle",limit_x=limit_x,limit_y= limit_y)

    def move(self):
        if(self.body.ycor() < self.limit_y):
            Entity.move()