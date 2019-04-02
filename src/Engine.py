import turtle
from pip._vendor.distlib.compat import raw_input
from src import GameObjects as Game , Characters as Cha

GameOn: bool = True
class Screen:
    screen: turtle.Screen()
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.delay(10)
        self.screen.bgcolor("black")
        self.screen.title("Space invaders")


class Menu(Screen):
    def __init__(self):
        Screen.__init__(self)

    #def assign_keys(self):


class Room(Screen):

    world: Game.World
    player: Cha.Player
    enemy: Cha.Enemy
    wave: Cha.EnemyWave

    def __init__(self):
        Screen.__init__(self)
        self.start()
        self.assign_keys()


    def assign_keys(self):
        self.screen.listen()
        self.screen.onkey(self.player.move_left, "Left")
        self.screen.onkey(self.player.move_right, "Right")
        self.screen.onkey(self.player.shoot, "space")

    def start(self):
        self.world = Game.World()
        self.player = Cha.Player(
            x=-0, y=-300, speed=10,
            color="green", sprite="triangle",
            limit_x=self.world.world_border.limit_x, limit_y=self.world.world_border.limit_y
        )

        Cha.EnemyWave.Wave += 1
        self.wave = Cha.EnemyWave(quantity=Cha.EnemyWave.Wave, limit_x=self.world.world_border.limit_x,
                                  limit_y=self.world.world_border.limit_y)

    def mainloop(self):
        while True:
            for enemy in self.wave.enemies:
                enemy.move()

            if (len(self.player.bullets) > 0):
                for i in self.player.bullets:
                    if(i.body.isvisible()):
                        i.move()
                        for j in self.wave.enemies:
                            i.collision(j)
                    else:
                        self.player.bullets.remove(i)

            if (self.player.fire < self.player.fire_rate):
                self.player.fire += 0.1

            if (not self.player.alive):
                break


while GameOn:
    room = Room()
    room.mainloop()
    room.screen.bye()
    break

raw_input("Game over!!")
