from Player import *
from Grid import Grid
from Window import Window
import curses

class Game:
    def __init__(self):
        self.Game = 1
        self.Turn = 1
        self.Game_Over = False
        self.Difficulty = "Easy"

    def take_turn(self, Player, Enemy, Window):
        #Draw Grid
        loop = True
        while loop == True:
            window.screen.clear()
            Window.get_grid(self, Player, Enemy, 0)
            self.Turn += 1

    def setup(self, Player1, Player2):
        for ship in Player1.Ships.keys():
            Player1.auto_deploy(Player1.Ships[ship])
        for ship in Player2.Ships.keys():
            Player2.auto_deploy(Player2.Ships[ship])

game = Game()
player = Player("Daniel", game, 1)
enemy = Player("Madhu", game, 2)
window = Window()

game.setup(player, enemy)
game.take_turn(player, enemy, window)