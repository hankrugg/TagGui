'''
 Hank Rugg, Jan 23

 GUI Controller for Hide and Seek Tag, gui based version.This class controls the game.

'''
import tkinter as tk
from tkinter import messagebox
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
        self.listener = keyboard.Listener(on_press=self.onPress, )
        self.listener.start()


    def setListener(self):
        self.listener = keyboard.Listener(on_press=self.onPress)

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
        self.game.map.resetMap()
        self.game.placePlayer()
        self.game.placeEnemies()
        self.renderMap()

    def makeMove(self, direction):
        if direction == 'w' or direction == 's' or direction == 'd' or direction == 'a':

            if self.game.player.checkValidMove(self.game.player.simulateMove(direction)[0],
                                          self.game.player.simulateMove(direction)[1],
                                          self.game.map.array):
                if direction == 'w':
                    self.game.player.move('w')
                    self.game.enemyMove()
                    self.renderMap()

                elif direction == 'a':
                    self.game.player.move('a')
                    self.game.enemyMove()
                    self.renderMap()


                elif direction == 's':
                    self.game.player.move('s')
                    self.game.enemyMove()
                    self.renderMap()

                elif direction == 'd':
                    self.game.player.move('d')
                    self.game.enemyMove()
                    self.renderMap()
                else:
                    print('Invalid')



# got help from https://pynput.readthedocs.io/en/latest/keyboard.html
    def onPress(self, key):
        try:
            self.makeMove(key.char)
            self.game.checkKill()
            if self.game.isOver:
                self.game.resetGame()
                self.startGame()
        except AttributeError:
            print('Invalid')



if __name__ == '__main__':
    app = Gui()
    # app.submitMove()
    app.startGame()
    app.mainloop()