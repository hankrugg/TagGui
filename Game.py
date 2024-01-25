'''
 Hank Rugg, Jan 18

 Game Class for Hide and Seek Tag, console based version.This class controls the game.

'''

import sys
from random import randint
from Enemy import Enemy
from Map import Map
from Player import Player


class Game:
    def __init__(self):
        self.map = Map()
        self.player = None
        self.enemies = []
        self.isOver = False
        self.playing = True
        self.numEnemies = 2

    def readyGame(self):
        self.map.drawMap()

    def placePlayer(self):
        # randomly place the player
        x = randint(1, 4)
        y = randint(1, 8)
        self.player = Player(x, y)
        # if the player is not in a valid spot on the map, they need to move
        while not self.player.checkValidMove(x, y, self.map.array):
            x = randint(1, 4)
            y = randint(1, 8)
            self.player = Player(x,y)
        self.renderMap()

    def renderMap(self):
        self.map.resetMap()
        # reset the map to its original state
        for i in range(self.map.rows):
            for j in range(self.map.columns):
                if i == self.player.xcoord and j == self.player.ycoord:
                    # place the player on the map
                    self.map.array[i][j] = 'O'
                for k in range(len(self.enemies)):
                    # place the enemies on the map
                    if i == self.enemies[k].xcoord and j == self.enemies[k].ycoord:
                        self.map.array[i][j] = 'P'


    def makeMove(self):
        self.renderMap()
        self.map.drawMap()
        # get input from the user for where they want to go
        direction = input("Where would you like to go?")
        # validation for only accepting allowable moves
        if direction == 'w' or direction == 's' or direction == 'd' or direction == 'a':
            # first check that they made a valid move
            if self.player.checkValidMove(self.player.simulateMove(direction)[0],
                                          self.player.simulateMove(direction)[1],
                                          self.map.array):
                # then move the player
                self.player.move(direction)
                self.enemyMove()
                self.renderMap()

            else:
                print("Invalid move")
        else:
            print("Invalid direction")

    def placeEnemies(self):
        # hard coded 3 enemies, this is where you could reduce or add enemies
        # clear the enemies list for when the game is restarted
        if len(self.enemies) > 1:
            self.enemies.clear()
        for i in range(self.numEnemies):
            x = randint(1, 4)
            y = randint(1, 8)
            # check if its a valid move
            if not self.player.checkValidMove(x,y,self.map.array):
                while not self.player.checkValidMove(x, y, self.map.array):
                    x = randint(1, 4)
                    y = randint(1, 8)
                self.enemies.append(Enemy(x,y))
                self.renderMap()
            else:
                self.enemies.append(Enemy(x,y))
                self.renderMap()



    def enemyMove(self):
        for enemy in self.enemies:
            # each enemy searches for the player and moves if they can
            direction = enemy.search(self.player.xcoord, self.player.ycoord)
            if enemy.checkValidMove(enemy.simulateMove(direction)[0],
                                          enemy.simulateMove(direction)[1],
                                          self.map.array):
                enemy.move(direction)
                self.renderMap()


    def checkKill(self):
        for enemy in self.enemies:
            # check if each enemy is on the player which indicates a "kill"
            if enemy.xcoord == self.player.xcoord and enemy.ycoord == self.player.ycoord:
                # draw the map a final time so the player knows where they died
                self.isOver = True
                self.map.resetMap()

    def playGame(self):
        # game play flow
        self.placePlayer()
        self.placeEnemies()
        # keep playing until the game is over
        while not self.isOver:
            self.makeMove()
            self.checkKill()
        # reset the game when it is over
        self.resetGame()
        print("___________________________________________________")
        print("Game Over!")
        print("___________________________________________________")



    def resetGame(self):
        self.isOver = False
        self.enemies.clear()

    def showMenu(self):
        print("___________________________________________________")
        print("Welcome to Hide and Seek Tag!")
        print("Options:")
        print("1: Instructions")
        print("2: Play")
        print("3: Quit")
        print("___________________________________________________")



    def showInstructions(self):
        print("___________________________________________________")
        print("Welcome to (virtual) Hide and Seek Tag")
        print("Controls:")
        print("w: Move up")
        print("s: Move down")
        print("a: Move right")
        print("d: Move left")
        print("The goal of the game is to last as long as you can,")
        print("there will be enemies that are trying to chase you,")
        print("your goal is to evade them for as long as you can.")
        print("___________________________________________________")



    def getChoice(self, option):
        # menu selector
        if option == "1":
            game.showInstructions()
        elif option == "2":
            game.playGame()
        elif option == "3":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Please make a valid choice!")



if __name__ == '__main__':
    game = Game()
    # start off showing the menu
    game.showMenu()
    option = input("Click the option you want and then press enter.")
    game.getChoice(option)
    # keep showing the menu after every choice is through
    while game.playing:
        game.showMenu()
        option = input("Click the option you want and then press enter.")
        game.getChoice(option)
