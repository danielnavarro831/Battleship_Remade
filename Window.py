import curses
import time
import os
from Save_File import Save_File

class Window:
    def __init__(self):
        os.system('mode con: cols=120 lines=45')
        self.screen = curses.initscr()
        self.screen.clear()
        self.line = 0
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_RED)
        save = Save_File()
        self.Save = save

    def Main_Menu(self, Game):
        self.screen.clear()
        Game.P1_Wins = 0
        Game.P2_Wins = 0
        Game.Game = 0
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                                    Battleship                                             "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = "Type Your Selection"
        line5 = " * 1 Player"
        line6 = " * 2 Players"
        line7 = " * Online"
        line8 = " * Rules"
        line9 = " * Settings"
        line10 = ""
        Menu = [line, line2, line3, line4, line5, line6, line7, line8, line9, line10]
        counter = 1
        for a in range(len(Menu)):
            if a == 1:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(4))
                self.screen.addstr("Ver: ")
                self.screen.addstr(str(Game.Version), curses.color_pair(2))
            elif a == 3:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(3))
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "1 Player":
                Game.PvP = False
                Game.Online = False
                loop = False
                Game.start_game(self)
            elif response == "2 Players":
                Game.Online = False
                loop = False
                if self.Save.check_for_local_saved_data() == True:
                    self.continue_screen(Game)
                else:
                    Game.PvP = True
                    Game.start_game(self)
            elif response == "Online":
                Game.PvP = True
                Game.Online = True
                loop = False
                self.online_multiplayer(Game)
            elif response == "Rules":
                loop = False
                self.rules(Game)
            elif response == "Settings":
                loop = False
                self.settings(Game)
            else:
                self.screen.refresh()

    def online_multiplayer(self, Game):
        self.screen.clear()
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                               Battleship - Online                                             "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = "Type Your Selection"
        line5 = " * New Game"
        line6 = " * Continue"
        line7 = " * Back"
        line8 = ""
        counter = 1
        Menu = [line, line2, line3, line4, line5, line6, line7, line8]
        for a in range(len(Menu)):
            if a == 1:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(4))
            elif a == 3:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(3))
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "New Game":
                if self.Save.check_for_online_saved_data() == True:
                    if self.overwrite_save_data() == True:
                        loop = False
                        Game.start_game(self)
                    else:
                        loop = False
                        self.Main_Menu(Game)
                else:
                    loop = False
                    Game.start_game(self)
            elif response == "Continue":
                loop = False
                Game.continue_game(self)
            elif response == "Back":
                loop = False
                self.Main_Menu(Game)
            else:
                self.screen.refresh()

    def rules(self, Game):
        self.screen.clear()
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                                Battleship - Rules                                          "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = "Be the first person to sink the other person's ships!"
        line5 = "Each player takes turns guessing a location of an enemy ship on the 10x10 grid"
        line6 = "Guessing the correct location of a ship will result in a Hit: "
        line7 = "An incorrect guess will result in a Miss: "
        line8 = "Your own ships will appear hidden on your own grid as: "
        line9 = "Each player has 5 ships of varrying lengths:"
        line10 = " * Patrol Boat: 2"
        line11 = " * Submarine: 3"
        line12 = " * Destroyer: 3"
        line13 = " * Battleship: 4"
        line14 = " * Aircraft Carrier: 5"
        line15 = ""
        line16 = "Type "
        Menu = [line, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16]
        counter = 1
        for a in range(len(Menu)):
            if a == 5:
                self.screen.addstr(counter, 1, Menu[a])
                self.screen.addstr("X", curses.color_pair(1))
            elif a == 6:
                self.screen.addstr(counter, 1, Menu[a])
                self.screen.addstr("O", curses.color_pair(2))
            elif a == 7:
                self.screen.addstr(counter, 1, Menu[a])
                self.screen.addstr("*", curses.color_pair(3))
            elif a == 15:
                self.screen.addstr(counter, 1, Menu[a])
                self.screen.addstr("'Back'", curses.color_pair(2))
                self.screen.addstr(" to return to the Main Menu")
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "Back":
                loop = False
                self.Main_Menu(Game)
            else:
                self.screen.refresh()

    def settings(self, Game):
        self.screen.clear()
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                               Battleship - Settings                                       "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = "Type Your Selection:"
        line5 = " (1) Delete Local Saved Data"
        line6 = " (2) Delete Online Saved Data"
        line7 = " (3) Back"
        line8 = ""
        Menu = [line, line2, line3, line4, line5, line6, line7, line8]
        counter = 1
        for a in range(len(Menu)):
            if a == 1:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(4))
            elif a == 3:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(3))
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "Delete Local Saved Data" or response == "1":
                loop = False
                self.Save.delete_data("Local")
                self.screen.addstr(counter +1, 1, "Save Data Deleted")
                self.screen.refresh()
                response = self.screen.getstr(counter, 1).decode('utf-8')
                self.Main_Menu(Game)
            elif response == "Delete Online Saved Data" or response == "2":
                loop = False
                self.Save.delete_data("Online")
                self.screen.addstr(counter +1, 1, "Save Data Deleted")
                self.screen.refresh()
                response = self.screen.getstr(counter, 1).decode('utf-8')
                self.Main_Menu(Game)
            elif response == "Back" or response == "3":
                loop = False
                self.Main_Menu(Game)
            else:
                self.screen.refresh()

    def overwrite_save_data(self):
        self.screen.clear()
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                               Battleship - Online                                             "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = "Warning:"
        Menu = [line, line2, line3, line4]
        counter = 1
        for a in range(len(Menu)):
            if a == 1:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(4))
            elif a == 3:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(5))
                self.screen.addstr(" Saved Data for a previous game already exists. Overwrite Saved Data? (Yes/No)")
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "Yes":
                loop = False
                return True
            if response == "No":
                loop = False
                return False

    def get_player_passcode(self, Game, Player):
        self.screen.clear()
        passcode = ""
        if Game.Active_Player == 1:
            passcode = Game.P1_Passcode
        else:
            passcode = Game.P2_Passcode
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                               Battleship - Online                                             "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = ""
        line5 = "Enter Passcode or type "
        Menu = [line, line2, line3, line4, line5]
        counter = 1
        for a in range(len(Menu)):
            if a == 1:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(4))
            elif a == 3:
                self.screen.addstr(counter, 1, Menu[a])
                self.screen.addstr(Player.Name, curses.color_pair(4))
                self.screen.addstr("'s Turn")
            elif a == 4:
                self.screen.addstr(counter, 1, Menu[a])
                self.screen.addstr("'Refresh'", curses.color_pair(2))
                self.screen.addstr(" to see if it's your turn:")
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            if response == passcode:
                loop = False
            elif response == "Refresh" or response == "refresh":
                loop = False
                Game.continue_game(self)
            else:
                self.screen.addstr(counter +1, 1, "Incorrect passcode")
                self.screen.refresh()

    def set_player_passcode(self, Game, Player):
        self.screen.clear()
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                               Battleship - Online                                             "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = "Set Passcode between 3 and 12 characters for "
        Menu = [line, line2, line3, line4]
        counter = 1
        for a in range(len(Menu)):
            if a == 1:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(4))
            elif a == 3:
                self.screen.addstr(counter, 1, Menu[a])
                self.screen.addstr(Player.Name, curses.color_pair(4))
                self.screen.addstr(":")
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            if len(response) > 2  and len(response) < 13 and response != "Refresh" and response != "refresh":
                if Player.Player_Num == 1:
                    Game.P1_Passcode = response
                else:
                    Game.P2_Passcode = response
                loop = False
            elif len(response) < 3:
                self.screen.addstr(counter +1, 1, "Passcode is too short")
                self.screen.refresh()
            elif len(response) > 12:
                self.screen.addstr(counter +1, 1, "Passcode is too long")
                self.screen.refresh()
            elif response == "Refresh" or response == "refresh":
                self.screen.addstr(counter +1, 1, "You cannot set your password to the refresh command")

    def continue_screen(self, Game):
        self.screen.clear()
        line = "----------------------------------------------------------------------------------------------------------------------"
        line2 = "                                               Battleship - Hot Seat                                          "
        line3 = "----------------------------------------------------------------------------------------------------------------------"
        line4 = "Type Your Selection"
        line5 = " * New Game"
        line6 = " * Continue"
        line7 = " * Back"
        line8 = ""
        counter = 1
        Menu = [line, line2, line3, line4, line5, line6, line7, line8]
        for a in range(len(Menu)):
            if a == 1:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(4))
            elif a == 3:
                self.screen.addstr(counter, 1, Menu[a], curses.color_pair(3))
            else:
                self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "New Game":
                Game.PvP = True
                loop = False
                Game.start_game(self)
            elif response == "Continue":
                loop = False
                Game.continue_game(self)
            elif response == "Back":
                loop = False
                self.Main_Menu(Game)
            else:
                self.screen.refresh()
    
    def get_grid(self, Game, Player, Enemy, Line):
        counter = Line
        th1 = "----------------------------------------------------------------------------------------------------------------------"
        th2 = "Game: "
        th3 = "  Turn: "
        th4 = "----------------------------------------------------------------------------------------------------------------------"
        self.screen.addstr(counter, 1, th1)
        counter +=1
        self.screen.addstr(counter, 1, th2)
        self.screen.addstr(str(Game.Game), curses.color_pair(2))
        self.screen.addstr(th3)
        self.screen.addstr(str(Game.Turn), curses.color_pair(2))
        counter +=1
        self.screen.addstr(counter, 1, th4)
        counter +=1
        times = 1  
        ship_names = ["Patrol Boat", "Destroyer", "Submarine", "Battleship", "Aircraft Carrier"]
        while times < 3:
            ship_counter = 0
            #Make Header
            h1 = "-----------------------------------"
            h2 = " "
            if times == 1:
                h2 += Enemy.Name
            else:
                h2 += Player.Name
            if len(h2) > len(h1):
                while len(h1) < len(h2) + 3:
                    h1 += ("-")
            if len(h2) < len(h1) -2:
                while len(h2) < len(h1) -2:
                    h2 += " "
            h3 = "---------------------------------"
            if len(h3) < len(h1) -2:
                while len(h3) < len(h1)-2:
                    h3 += "-"
            self.screen.addstr(counter, 1, h1)
            counter +=1 
            self.screen.addstr(counter, 1, h2, curses.color_pair(4))
            self.screen.addch("/")
            counter += 1
            self.screen.addstr(counter, 1, h3)
            counter += 1
            #Display Wins
            self.screen.addstr(counter, 1, "Wins: ")
            if times == 1:
                self.screen.addstr(str(Game.P2_Wins), curses.color_pair(2))
            else:
                self.screen.addstr(str(Game.P1_Wins), curses.color_pair(2))
            counter += 2
            #Make Grid
            line = "    "
            for d in range(1, Player.Grid.Max + 1):
                line += str(d)
                if d < 10:
                    line += "  "
                else:
                    line += " "
            self.screen.addstr(counter, 1, line)
            counter += 1
            if times == 1: #Guess Grid
                for a in Player.Guess_Grid.grid.keys():
                    line = " " + a + " "
                    self.screen.addstr(counter, 1, line)
                    for b in Player.Guess_Grid.grid[a].keys():
                        self.screen.addch("[")
                        if Player.Guess_Grid.grid[a][b] == "Blank":
                            self.screen.addch(Player.Guess_Grid.Blank)
                        elif Player.Guess_Grid.grid[a][b] == "Hit":
                            self.screen.addch(Player.Guess_Grid.Hit, curses.color_pair(1))
                        elif Player.Guess_Grid.grid[a][b] == "Sunk":
                            self.screen.addch(Player.Guess_Grid.Sunk, curses.color_pair(1))
                        elif Player.Guess_Grid.grid[a][b] == "Miss":
                            self.screen.addch(Player.Guess_Grid.Miss, curses.color_pair(2))
                        elif Player.Guess_Grid.grid[a][b] == "Hidden":
                            self.screen.addch(Player.Guess_Grid.Hidden, curses.color_pair(3))
                        self.screen.addch("]")
                    #Display Ship Status
                    if counter % 2 == 0:
                        if ship_counter < len(ship_names):
                            self.display_sunk_status(Enemy.Ships[ship_names[ship_counter]], counter)
                        ship_counter += 1
                    counter += 1
            else:          #Player Grid
                for a in Player.Grid.grid.keys():
                    line = " " + a + " "
                    self.screen.addstr(counter, 1, line)
                    for b in Player.Grid.grid[a].keys():
                        self.screen.addch("[")
                        if Player.Grid.grid[a][b] == "Blank":
                            self.screen.addch(Player.Grid.Blank)
                        elif Player.Grid.grid[a][b] == "Hit":
                            self.screen.addch(Player.Grid.Hit, curses.color_pair(1))
                        elif Player.Grid.grid[a][b] == "Sunk":
                            self.screen.addch(Player.Grid.Sunk, curses.color_pair(1))
                        elif Player.Grid.grid[a][b] == "Miss":
                            self.screen.addch(Player.Grid.Miss, curses.color_pair(2))
                        elif Player.Grid.grid[a][b] == "Hidden":
                            self.screen.addch(Player.Grid.Hidden, curses.color_pair(3))
                        self.screen.addch("]")
                    #Display Ship Status
                    if counter % 2 == 0:
                        if ship_counter < len(ship_names):
                            self.display_sunk_status(Player.Ships[ship_names[ship_counter]], counter)
                        ship_counter += 1
                    counter += 1
            counter += 2
            times += 1
        self.screen.refresh()
        self.line = counter

    def hotseat_screen(self, Player):
        self.screen.clear()
        line = Player.Name
        line2 = "'s Turn"
        line3 = "Press "
        line4 = " to continue"
        mid = 60 - int((len(Player.Name) + len(line2))/2)
        self.screen.addstr(20, mid, line, curses.color_pair(4))
        self.screen.addstr(line2)
        self.screen.addstr(21, 48, line3)
        self.screen.addstr("Enter", curses.color_pair(2))
        self.screen.addstr(line4)
        self.screen.refresh()
        response = self.screen.getstr().decode('utf-8')

    def get_player_guess(self, Player, Enemy, Line, Game):
        counter = Line
        self.screen.addstr(counter, 1, "Where will you fire missiles?")
        counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            self.screen.move(counter +1, 0)
            self.screen.clrtoeol() 
            self.screen.refresh()
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "Save" and Game.PvP == True:
                if Player.Player_Num == 1:
                    self.screen.addstr(counter +1, 1, "Saving...")
                    self.screen.refresh()
                    self.Save.save_game(Player, Enemy, Game)
                    self.screen.addstr(counter +1, 1, "Save Complete!")
                    self.screen.refresh()
                    self.screen.move(counter, 0)
                    self.screen.clrtoeol()
                    self.screen.refresh()
                else:
                    self.screen.addstr(counter +1, 1, "Saving...")
                    self.screen.refresh()
                    self.Save.save_game(Enemy, Player, Game)
                    self.screen.addstr(counter +1, 1, "Save Complete!")
                    self.screen.refresh()
                    self.screen.move(counter, 0)
                    self.screen.clrtoeol()
                    self.screen.refresh()
            elif response == "Quit":
                loop = False
                self.Main_Menu(Game)
            else:
                if len(response) > 3 or len(response) < 2:
                    self.screen.move(counter, 0)
                    self.screen.clrtoeol() 
                    self.screen.addstr(counter +1, 1, "Invalid Response")
                    self.screen.refresh()
                    response = self.screen.getstr(counter, 1).decode('utf-8')
                else:
                    check_row = response[0]
                    check_column = ""
                    for i in range(1, len(response)):
                        check_column += response[i]
                    if check_row.isalpha() and Player.Grid.translate_row(check_row) <= Player.Grid.Max and check_column.isdigit() and int(check_column) <= Player.Grid.Max and int(check_column) >= Player.Grid.Min:
                        if response in Player.Guesses:
                            self.screen.addstr(counter +1, 1, "Location already guessed. Choose another location.")
                            self.screen.refresh()
                            response = self.screen.getstr(counter, 1).decode('utf-8')
                        else:
                            attack = Enemy.check_guess(response)
                            if attack[0] == True:
                                self.hit(Player, Enemy, attack[1], response, counter)
                            else:
                                self.miss(Player, Enemy, response, counter)
                            loop = False
                    else:
                        self.screen.addstr(counter +1, 1, "Invalid Response")
                        self.screen.refresh()
                        response = self.screen.getstr(counter, 1).decode('utf-8')

    def get_AI_guess(self, Player, Enemy, Line):
        counter = Line
        self.screen.move(counter, 0)
        self.screen.clrtoeol() 
        self.screen.refresh()
        target = Player.AI_guess()
        txt = Player.Name + " fires missiles at " + str(target)
        self.screen.addstr(counter, 1, txt)
        counter += 1
        attack = Enemy.check_guess(target)
        if attack[0] == True:
            self.hit(Player, Enemy, attack[1], target, counter)
        else:
            self.miss(Player, Enemy, target, counter)

    def hit(self, Player, Enemy, Ship, Guess, Line):
        Enemy.Grid.update_grid(Guess[0], int(Guess[1:]), "Hit")
        Player.Guess_Grid.update_grid(Guess[0], int(Guess[1:]), "Hit")
        Player.Guesses[Guess] = "Hit"
        for point in range(len(Enemy.Ships[Ship].Points)):
            if Guess in Enemy.Ships[Ship].Points[point].values():
                Enemy.Ships[Ship].Points[point]["Status"] = "Hit"
        line = ""
        if Enemy.Ships[Ship].check_status(Player) == True:
            line = Player.Name + " sunk " + Enemy.Name + "'s " + Ship
        else:
            line = Player.Name + "'s attack hits!"
        self.screen.move(Line +1, 0)
        self.screen.clrtoeol() 
        self.screen.addstr(Line +1, 1, line)
        self.screen.refresh()
        response = self.screen.getstr(Line +1, 1).decode('utf-8')

    def miss(self, Player, Enemy, Guess, Line):
        Enemy.Grid.update_grid(Guess[0], int(Guess[1:]), "Miss")
        Player.Guess_Grid.update_grid(Guess[0], int(Guess[1:]), "Miss")
        Player.Guesses[Guess] = "Miss"
        line = Player.Name + "'s attack missed!"
        self.screen.move(Line +1, 0)
        self.screen.clrtoeol() 
        self.screen.addstr(Line +1, 1, line)
        self.screen.refresh()
        response = self.screen.getstr(Line, 1).decode('utf-8')

    def display_sunk_status(self, Ship, Line):
        line = Ship.Name + ": "
        self.screen.addstr(Line, 37, line)
        if Ship.Sunk == True:
            line = "Sunk"
            self.screen.addstr(line, curses.color_pair(1))
        else:
            line = "Active"
            self.screen.addstr(line, curses.color_pair(3))
        self.screen.refresh()

    def get_player_names(self, Game, Player, Enemy):
        self.screen.clear()
        if Game.PvP == True:
            loop = True
            player = 1
            while loop == True:
                self.screen.clear()
                self.screen.addstr(20, 46, "What is the name of ")
                if player == 1:
                    self.screen.addstr("Player 1", curses.color_pair(4))
                else:
                    self.screen.addstr("Player 2", curses.color_pair(4))
                self.screen.addstr("?")
                self.screen.refresh()
                response = self.screen.getstr(21, 46).decode('utf-8')
                response = response.title()
                if len(response) < 13 and len(response) > 0:
                    if player == 1:
                        Player.Name = response
                        player += 1
                    else:
                        if response != Player.Name:
                            Enemy.Name = response
                            loop = False
                        else:
                            self.screen.addstr(22, 32, "That name is already in use. Please use a different name")
                            self.screen.refresh()
                elif len(response) > 13:
                    self.screen.addstr(22, 36, "Please enter a name no longer than 12 characters")
                    self.screen.refresh()
                elif len(response) < 1:
                    self.screen.addstr(22, 33, "Please enter a name that is at least 1 character long")
                    self.screen.refresh()
        else:
            loop = True
            while loop == True:
                self.screen.addstr(20, 51, "What is your name?")
                self.screen.refresh()
                response = self.screen.getstr(21, 51).decode('utf-8')
                response = response.title()
                if len(response) < 13 and len(response) > 0:
                    Player.Name = response
                    loop = False
                elif len(response) > 13:
                    self.screen.addstr(22, 36, "Please enter a name no longer than 12 characters")
                    self.screen.refresh()
                elif len(response) < 1:
                    self.screen.addstr(22, 33, "Please enter a name that is at least 1 character long")
                    self.screen.refresh()

    def play_again(self, Game, Player, Enemy):
        confirm = ["Yes", "Yeah", "Sure", "Yea", "Ye", "Ok", "Aiight", "Alright", "Y"]
        cancel = ["No", "Nah", "Na", "Nope", "N", "Quit", "End", "Cancel", "Negative"]
        loop = True
        winner = ""
        if Player.get_ships_alive() == 0:
            winner = Enemy.Name
        else:
            winner = Player.Name
        line = " wins!"
        mid = 60 - int((len(line) + len(winner))/2)
        while loop == True:
            self.screen.clear()
            self.screen.addstr(19, mid, winner, curses.color_pair(4))
            self.screen.addstr(line)
            self.screen.addstr(20, 46, "Would you like to play again?")
            self.screen.refresh()
            response = self.screen.getstr(21, 46).decode('utf-8')
            response = response.title()
            if response in confirm:
                loop = False
                Game.start_game(self)
            elif response in cancel:
                loop2 = True
                while loop2 == True:
                    self.screen.clear()
                    self.screen.addstr(20, 47, "Return to Main Menu?")
                    self.screen.refresh()
                    response = self.screen.getstr(21, 47).decode('utf-8')
                    response = response.title()
                    if response in confirm:
                        loop = False
                        loop2 = False
                        self.Main_Menu(Game)
                    else:
                        self.screen.clear()
                        self.screen.addstr(20, 47, "Thanks for playing!")
                        self.screen.refresh()
                        loop2 = False
                        loop = False
                        response = self.screen.getstr(21, 47).decode('utf-8')
                        curses.endwin()
