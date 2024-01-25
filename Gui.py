'''
 Hank Rugg, Jan 23

 GUI Controller for Hide and Seek Tag, gui based version.This class controls the game.

'''
import time
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import sys
from Game import Game


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hide and Seek Tag")
        self.geometry('800x800')
        # so the window cannot change size
        self.minsize(width=800, height=800)
        self.maxsize(width=800, height=800)
        self.game = Game()
        self.rows = self.game.map.rows
        self.columns = self.game.map.columns
        self.canvas = tk.Canvas(self, width=550, height=650)
        self.canvas.pack()
        self.listener = keyboard.Listener(on_press=self.onPress, )
        self.listener.start()
        self.moves = 0

    def drawMapOutline(self):
        # drawing the map using i and j to do the math
        for i in range(self.columns):
            for j in range(self.rows):
                if self.game.map.array[j][i] == 'x':
                    self.canvas.create_rectangle((50 * i), (j * 50), 50 + (50 * i), 50 + (j * 50), fill='black')

    def drawCharacters(self):
        # draw all the characters on the map
        self.game.placePlayer()
        self.game.placeEnemies()
        self.renderMap()

    def renderMap(self):
        # delete everything from the canvas and then redraw it
        self.canvas.delete('all')
        self.canvas.pack()
        self.game.renderMap()
        self.canvas.create_text(250, 600, text="Moves:" + str(self.moves), fill="black", font=('Helvetica 25 bold'))
        self.drawMapOutline()
        # use i and j to do the math
        for i in range(self.columns):
            for j in range(self.rows):
                if self.game.map.array[j][i] == 'O':
                    self.canvas.create_rectangle((50 * i), (j * 50), 50 + (50 * i), 50 + (j * 50), fill='green')
                if self.game.map.array[j][i] == 'P':
                    self.canvas.create_rectangle((50 * i), (j * 50), 50 + (50 * i), 50 + (j * 50), fill='red')

    def startGame(self):
        self.game.map.resetMap()
        self.game.placePlayer()
        self.game.placeEnemies()
        self.renderMap()

    def makeMove(self, direction):
        # using the keys, w, s, d, and a to move your character
        if direction == 'w' or direction == 's' or direction == 'd' or direction == 'a':
            if self.game.player.checkValidMove(self.game.player.simulateMove(direction)[0],
                                               self.game.player.simulateMove(direction)[1],
                                               self.game.map.array):
                self.moves += 1

                # for each possible direction, move the player, move the enemies, then render the map
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
            # if the choice is invalid, show them the correct moves
            tk.messagebox.showerror("Bad Choice", 'Please select a valid moves are: a,s,w,d!')

    # got help from https://pynput.readthedocs.io/en/latest/keyboard.html for the keyboard listener
    def onPress(self, key):
        # try except to avoid the attribute error when the user clicks a special character
        try:
            # move based on key input and then check if the game is over
            self.makeMove(key.char)
            self.game.checkKill()
            if self.game.isOver:
                self.renderMap()
                # sleep so that the map has time to render before the message box is shown
                time.sleep(0.1)
                tk.messagebox.showinfo("Game Over", "You lost! Click restart to start a new game.")
        except AttributeError:
            # show a bad choice error if they choose a special key
            tk.messagebox.showerror("Bad Choice", 'Please select a valid move: a,s,w,d!')

    def restartGame(self):
        self.moves = 0
        self.game.resetGame()
        self.startGame()

    def showInstructions(self):
        # button that shows the directions of the game
        tk.messagebox.showinfo("Instructions", "Controls:w: Move up, s: Move down,"
                                               "a: Move right,d: Move left, "
                                               "The goal of the game is to last as long as you can,"
                                               "there will be enemies that are trying to chase you,"
                                               "your goal is to evade them for as long as you can.")

    def menu(self):
        # place all the buttons on the gui
        instructions = tk.Button(self, text='Instructions', command=self.showInstructions)
        instructions.place(x=400, y=700)

        quit = tk.Button(self, text='Quit', command=sys.exit)
        quit.place(x=300, y=700)

        restart = tk.Button(self, text='Restart', command=self.restartGame)
        restart.place(x=200, y=700)


if __name__ == '__main__':
    # run the game
    app = Gui()
    app.startGame()
    app.menu()
    app.mainloop()
