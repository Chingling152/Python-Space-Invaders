import turtle
from pip._vendor.distlib.compat import raw_input
from src import GameObjects, Characters

#valores iniciais para a tela

win = turtle.Screen()
win.bgcolor("black")
win.title("Space invaders")

# desenhos na tela
world = GameObjects.World()
player = Characters.Player(
    x = 0, y =-300, speed=10,
    color ="green", sprite="triangle",
    limit = world.world_border.limit_x
)
enemy = Characters.Enemy(
    x=-300,y=300,speed=1,
    color="red",sprite="circle",
    limit = world.world_border.limit_x,limit_y =world.world_border.limit_y
)

# Definindo teclas
win.listen() # listen significa que está recebendo as teclas de atribuição (ouvindo)
win.onkey(player.move_left, "Left")
win.onkey(player.move_right, "Right")

while True:
    enemy.move()
    if(not player.alive):
        break

raw_input("Game over!!")# impede a tela de fechar sozinha