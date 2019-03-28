import turtle
from pip._vendor.distlib.compat import raw_input
from src.GameObjects import Characters , World

#valores iniciais para a tela
win = turtle.Screen()
win.bgcolor("black")
win.title("Space invaders")

# desenhos na tela
world = World.Map()
player = Characters.Player(x = 0,y =-300,speed=2,color = "green",sprite="triangle")

# Definindo teclas
win.onkey(player.move(0), 'Left')
win.onkey(player.move(180), 'Right')
win.listen()

win.mainloop()

raw_input("Game over!!")# impede a tela de fechar sozinha