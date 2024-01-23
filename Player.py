'''
 Hank Rugg, Jan 18

 Player Class for Hide and Seek Tag, console based version. This is the base class for players.

'''

class Player:
    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord

    def setYCoord(self, ycoord):
        self.ycoord = ycoord

    def setXCoord(self, xcoord):
        self.xcoord = xcoord

    def getYCoord(self):
        return self.ycoord

    def getXCoord(self):
        return self.xcoord

    def checkValidMove(self, i, j, array):
        # given an index in the array, check to see if that space is open
        if array[i][j] != " ":
            return False
        return True

    def simulateMove(self, direction):
        # calculating the future spot of the player
        if direction == "w":
            x = self.xcoord - 1
            return [x, self.ycoord]
        elif direction == "s":
            x = self.xcoord + 1
            return [x, self.ycoord]
        elif direction == "a":
            y = self.ycoord - 1
            return [self.xcoord, y]
        elif direction == "d":
            y = self.ycoord + 1
            return [self.xcoord, y]

    def move(self, direction):
        # actually move the player
        # wasd used for direction
        if direction == "w":
            self.xcoord -= 1
        elif direction == "s":
            self.xcoord += 1
        elif direction == "a":
            self.ycoord -= 1
        elif direction == "d":
            self.ycoord += 1
        else:
            print("Invalid direction")
