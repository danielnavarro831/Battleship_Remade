from Player import *
from Grid import Grid
from Window import Window
from Save_File import Save_File
import curses

class Game:
    def __init__(self):
        self.Game = 0
        self.Turn = 1
        self.P1_Wins = 0
        self.P2_Wins = 0
        self.PvP = False
        self.Online = False
        self.Version = 1.02
        self.Active_Player = 1
        self.P1_Passcode = ""
        self.P2_Passcode = ""

    def end_game(self, Player, Enemy):
        end = False
        if Player.get_ships_alive() == 0 or Enemy.get_ships_alive() == 0:
            end = True
        return end

    def take_turn(self, Player, Enemy, Window):
        while self.end_game(Player, Enemy) == False:
            if self.Active_Player == 1:
                if self.PvP == True:
                    if self.Online == False:
                        Window.hotseat_screen(Player)
                    else:
                        if self.Turn == 1:
                            Window.set_player_passcode(self, Player)
                        else:
                            Window.get_player_passcode(self, Player)
                Window.screen.clear()
                Window.get_grid(self, Player, Enemy, 0)
                Window.get_player_guess(Player, Enemy, Window.line, self)
                Window.screen.clear()
                Window.get_grid(self, Player, Enemy, 0)
                self.Active_Player = 2
                if self.Online == True:
                    Window.Save.save_game(Player, Enemy, self)
            if self.end_game(Player, Enemy) == False:
                if self.Active_Player == 2:
                    if self.PvP == True:
                        if self.Online == False:
                            Window.hotseat_screen(Enemy)
                        else:
                            if self.Turn == 1:
                                Window.set_player_passcode(self, Enemy)
                            else:
                                Window.get_player_passcode(self, Enemy)
                        Window.screen.clear()
                        Window.get_grid(self, Enemy, Player, 0)
                    if Enemy.Player == False:
                        Window.get_AI_guess(Enemy, Player, Window.line)
                    else:
                        Window.get_player_guess(Enemy, Player, Window.line, self)
                        Window.screen.clear()
                        Window.get_grid(self, Enemy, Player, 0)
                    self.Active_Player = 1
                    self.Turn += 1
                    if self.Online == True:
                        Window.Save.save_game(Player, Enemy, self)
            if self.end_game(Player, Enemy) == True:
                if Player.get_ships_alive() == 0:
                    self.P2_Wins +=1
                elif Enemy.get_ships_alive() == 0:
                    self.P1_Wins += 1
                Window.play_again(self, Player, Enemy)

    def setup(self, Player1, Player2):
        for ship in Player1.Ships.keys():
            Player1.auto_deploy(Player1.Ships[ship])
        for ship in Player2.Ships.keys():
            Player2.auto_deploy(Player2.Ships[ship])

    def start_game(self, Window):
        self.Game += 1
        self.Turn = 1
        player = Player("Player 1", 1)
        player2 = Player("Player 2", 2)
        enemy = AI("Player 2", 2)
        Window.get_player_names(game, player, player2)
        if self.PvP == True:
            self.setup(player, player2)
            self.take_turn(player, player2, Window)
        else:
            self.setup(player, enemy)
            self.take_turn(player, enemy, Window)

    def continue_game(self, Window):
        player = Player("Player 1", 1)
        player2 = Player("Player 2", 2)
        Window.Save.load_game(player, player2, self)
        self.PvP = True
        self.take_turn(player, player2, Window)

if __name__ == '__main__':
    game = Game()
    window = Window()
    window.Main_Menu(game)