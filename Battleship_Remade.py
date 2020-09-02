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

    def end_game(self, Player, Enemy):
        end = False
        if Player.get_ships_alive() == 0 or Enemy.get_ships_alive() == 0:
            end = True
        return end

    def take_turn(self, Player, Enemy, Window):
        while self.end_game(Player, Enemy) == False:
            window.screen.clear()
            Window.get_grid(self, Player, Enemy, 0)
            Window.get_player_guess(Player, Enemy, Window.line)
            window.screen.clear()
            Window.get_grid(self, Player, Enemy, 0)
            if Enemy.Player == False:
                Window.get_AI_guess(Enemy, Player, Window.line)
            self.Turn += 1

    def setup(self, Player1, Player2):
        for ship in Player1.Ships.keys():
            Player1.auto_deploy(Player1.Ships[ship])
        for ship in Player2.Ships.keys():
            Player2.auto_deploy(Player2.Ships[ship])


if __name__ == '__main__':
    game = Game()
    window = Window()
    window.Main_Menu(game)
    player = Player("Daniel", game, 1)
    enemy = AI("Madhu", game, 2)
    game.setup(player, enemy)
    game.take_turn(player, enemy, window)