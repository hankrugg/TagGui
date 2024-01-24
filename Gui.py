'''
 Hank Rugg, Jan 23

 GUI Controller for Hide and Seek Tag, gui based version.This class controls the game.

'''
import tkinter as tk
from pynput import keyboard
import sys
from random import randint
from Enemy import Enemy
from Map import Map
from Player import Player
from Game import Game


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App")
        self.geometry('700x500')
        self.rows = 6
        self.columns = 10
        self.canvas = tk.Canvas(self, width=550, height=450)
        self.canvas.pack()
        self.game = Game()


        ######## Extra Code ##########
        # self.canvas.create_line(10,10,400,10, fill='black', width=5)
        # self.canvas.create_line(10,10,10,400, fill='black', width=5)
        # for i in range(1,self.rows):
        #     self.canvas.pack()
        #     self.canvas.create_line(10 ,50*i,410,50*i, fill='black', width=5)
        # for j in range(1,self.columns):
        #     self.canvas.create_line(50*j,10,50*j,410, fill='black', width=5)



    def drawMapOutline(self):
        for i in range(self.columns):
            for j in range(self.rows):
                if self.game.map.array[j][i] == 'x':
                    self.canvas.create_rectangle((50*i), (j*50), 50 +(50*i), 50 + (j*50), fill='black')

    def drawCharacters(self):
        self.game.placePlayer()
        self.game.placeEnemies()
        self.renderMap()


    def renderMap(self):
        self.canvas.delete('all')
        self.canvas.pack()
        self.game.renderMap()
        self.drawMapOutline()
        for i in range(self.columns):
            for j in range(self.rows):
                if self.game.map.array[j][i] == 'O':
                    self.canvas.create_rectangle((50*i), (j*50), 50 +(50*i), 50 + (j*50), fill='green')
                if self.game.map.array[j][i] == 'P':
                    self.canvas.create_rectangle((50*i), (j*50), 50 +(50*i), 50 + (j*50), fill='red')

    def startGame(self):
        self.game.placePlayer()
        self.game.placeEnemies()
        self.renderMap()

    def makeMove(self, direction):
        if direction == 'w':
            self.game.player.move('w')
            self.renderMap()
        elif direction == 'a':
            self.game.player.move('a')
            self.renderMap()
        elif direction == 's':
            self.game.player.move('s')
            self.renderMap()
        elif direction == 'd':
            self.game.player.move('d')
            self.renderMap()
        else:
            print('Invalid')
        self.game.enemyMove()


# got help from https://pynput.readthedocs.io/en/latest/keyboard.html
    def onPress(self, key):
        try:
            self.makeMove(key.char)
        except AttributeError:
            print('special key {0} pressed'.format(
                key))



if __name__ == '__main__':
    app = Gui()
    # app.submitMove()
    app.startGame()
    for i in range(1):
        listener = keyboard.Listener(
            on_press=app.onPress,)
        listener.start()

    app.mainloop()