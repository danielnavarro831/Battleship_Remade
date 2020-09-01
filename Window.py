import curses
import time
import os

class Window:
    def __init__(self):
        os.system('mode con: cols=120 lines=45')
        self.screen = curses.initscr()
        self.screen.clear()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        #self.screen.endwin()

    def Main_Menu(self, Game):
        #screen = curses.initscr()
        self.screen.clear()
        line = "------------------------------------------------------------------------------"
        line2 = "                                   Battleship                                 "
        line3 = "------------------------------------------------------------------------------"
        line4 = "Type Your Difficulty:"
        line5 = " * Easy"
        line6 = " * Medium"
        line7 = " * Hard"
        line8 = ""
        Menu = [line, line2, line3, line4, line5, line6, line7, line8]
        counter = 1
        for a in range(len(Menu)):
            self.screen.addstr(counter, 1, Menu[a])
            counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if response == "Easy" or response == "Medium" or response == "Hard":
                Game.Difficulty = response
                self.screen.refresh()
                loop == False
            else:
                self.screen.refresh()
    
    def get_grid(self, Game, Player, Enemy, Line):
        counter = Line
        th1 = "-----------------------------------------------------------------------------------------------------------------------"
        th2 = "Turn: "
        th3 = "-----------------------------------------------------------------------------------------------------------------------"
        self.screen.addstr(counter, 1, th1)
        counter +=1
        self.screen.addstr(counter, 1, th2)
        self.screen.addstr(str(Game.Turn), curses.color_pair(2))
        counter +=1
        self.screen.addstr(counter, 1, th3)
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
            if times == 1:
                self.screen.addstr(counter, 1, h2, curses.color_pair(4))
            else:
                self.screen.addstr(counter, 1, h2, curses.color_pair(4))
            self.screen.addch("/")
            counter += 1
            self.screen.addstr(counter, 1, h3)
            counter += 1
            #Display Wins
            self.screen.addstr(counter, 1, "Wins: ")
            if times == 1:
                self.screen.addstr(str(Enemy.Wins), curses.color_pair(2))
            else:
                self.screen.addstr(str(Player.Wins), curses.color_pair(2))
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
                        self.display_sunk_status(Player.Ships[ship_names[ship_counter]], counter)
                        ship_counter += 1
                    counter += 1
            counter += 2
            times += 1
        self.screen.refresh()
        self.get_player_guess(Player, Enemy, counter)

    def get_player_guess(self, Player, Enemy, Line):
        counter = Line
        self.screen.addstr(counter, 1, "Where will you fire missiles?")
        counter += 1
        self.screen.refresh()
        loop = True
        while loop == True:
            response = self.screen.getstr(counter, 1).decode('utf-8')
            response = response.title()
            if len(response) > 3 or len(response) < 2:
                self.screen.addstr(counter, 1, "Invalid Response")
                self.screen.refresh()
            else:
                check_row = response[0]
                check_column = ""
                for i in range(1, len(response)):
                    check_column += response[i]
                if check_row.isalpha() and Player.Grid.translate_row(check_row) <= Player.Grid.Max and check_column.isdigit() and int(check_column) <= Player.Grid.Max and int(check_column) >= Player.Grid.Min:
                    if response in Player.Guesses:
                        self.screen.addstr(counter, 1, "Location already guessed. Choose another location.")
                        self.screen.refresh()
                    else:
                        attack = Enemy.check_guess(response)
                        if attack[0] == True:
                            self.hit(Player, Enemy, attack[1], response, counter)
                        else:
                            self.miss(Player, Enemy, response, counter)
                        loop = False

    def hit(self, Player, Enemy, Ship, Guess, Line):
        Enemy.Grid.update_grid(Guess[0], int(Guess[1:]), "Hit")
        Player.Guess_Grid.update_grid(Guess[0], int(Guess[1:]), "Hit")
        Player.Guesses[Guess] = "Hit"
        for point in range(len(Enemy.Ships[Ship].Points)):
            if Guess in Enemy.Ships[Ship].Points[point].values():
                Enemy.Ships[Ship].Points[point]["Status"] = "Hit"
        line = ""
        if Enemy.Ships[Ship].check_status() == True:
            line = Player.Name + " sunk " + Enemy.Name + "'s " + Ship
        else:
            line = Player.Name + "'s attack hits!"
        self.screen.addstr(Line, 1, line)
        self.screen.refresh()

    def miss(self, Player, Enemy, Guess, Line):
        Enemy.Grid.update_grid(Guess[0], int(Guess[1:]), "Miss")
        Player.Guess_Grid.update_grid(Guess[0], int(Guess[1:]), "Miss")
        Player.Guesses[Guess] = "Miss"
        line = Player.Name + "'s attack missed!"
        self.screen.addstr(Line, 1, line)
        self.screen.refresh()

    def display_sunk_status(self, Ship, Line):
        line = Ship.Name + ": "
        self.screen.addstr(Line, 37, line)
        if Ship.Sunk == True:
            line = "Sunk"
            self.screen.addstr(line, curses.color_pair(1))
            #line2 = "  " + str(Ship.Points)
            #self.screen.addstr(Line + 1, 37, line2)
        else:
            line = "Active"
            self.screen.addstr(line, curses.color_pair(3))
            #line2 = "  " + str(Ship.Points)
            #self.screen.addstr(Line + 1, 37, line2)
        self.screen.refresh()