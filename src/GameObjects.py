import turtle

class WorldBorder:

    limit_x : float
    limit_y : float

    def __init__(self,sizex,sizey):
        self.size_x = sizex
        self.size_y = sizey
        self.limit_x = sizex /2 - 20
        self.limit_y = sizey / 2 - 20

        border = turtle.Turtle()
        border.speed(0)  # 0 = velocidade mais rapida da caneta
        border.color("white")
        border.penup()
        # seta posição inicial para a caneta
        border.setpos(-400, -350)  # posição 0,0 é o meio da tela
        border.pendown()  # abaixa a caneta para que possa desenhar o quadrado
        border.pensize(4)

        # move a caneta ao redor da tela
        for i in range(4):
            if (i % 2 == 0):
                border.fd(sizex)
            else:
                border.fd(sizey)

            border.lt(90)

        border.hideturtle()


class World:

    world_border: WorldBorder

    def __init__(self):
        self.world_border = WorldBorder(800,700)

    def get_border_x(self):
        return self.world_border.size_x /2

