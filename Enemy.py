'''
 Hank Rugg, Jan 20

 Enemy Class for Hide and Seek Tag, console based version. This class inherits from player.

'''

from Player import Player
from random import randint


class Enemy(Player):
    def __init__(self, xcoord, ycoord):
        super().__init__(xcoord, ycoord)

    def search(self, i, j):
        # search component that is used to decide where the enemy will go
        x = randint(0, 1)
        # half of the time it will move its x component and half the time it will
        # move its y component
        if x == 0:
            if self.xcoord <= i:
                return "s"
            else:
                return "w"
        if x == 1:
            if self.ycoord <= j:
                return "d"
            else:
                return "a"
