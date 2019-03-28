import turtle

class Map:

    def create_border(self):
        '''
        Cria um objeto do tipo turtle e coloca suas definições padrão
        :return: Um objeto do tipo turtle ja desenhado na tela
        '''
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
                border.fd(800)
            else:
                border.fd(700)

            border.lt(90)

        border.hideturtle()
        return border

    def __init__(self):
        self.border = self.create_border()