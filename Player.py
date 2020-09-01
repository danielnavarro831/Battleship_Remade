from Ship import Ship
from Grid import Grid
import random

class Player:
    def __init__(self, Name, Game, Player_Number):
        self.Name = Name.title()
        if Player_Number > 0 and Player_Number < 3:
            self.Player_Num = Player_Number
        else:
            raise Exception("Invalid Player Number:", Player_Number)
        self. Player = True
        self.Ships = {}
        patrol_boat = Ship("Patrol Boat")
        submarine = Ship("Submarine")
        destroyer = Ship("Destroyer")
        battleship = Ship("Battleship")
        aircraft_carrier = Ship("Aircraft Carrier")
        self.Ships["Patrol Boat"] = patrol_boat
        self.Ships["Submarine"] = submarine
        self.Ships["Destroyer"] = destroyer
        self.Ships["Battleship"] = battleship
        self.Ships["Aircraft Carrier"] = aircraft_carrier
        #{"Patrol Boat": patrol_boat, "Submarine": submarine...}
        self.Wins = 0
        self.Ships_Remaining = self.get_ships_alive()
        self.Guesses = {}
        #Guesses = {"A1": "Hit", "B2": "Miss"...}
        grid = Grid(Game.Difficulty)
        self.Grid = grid
        guess_grid = Grid(Game.Difficulty)
        self.Guess_Grid = guess_grid

    def get_ships_alive(self):
        counter = 0
        for ship in self.Ships.keys():
            if self.Ships[ship].Info["Sunk"] == False:
                counter += 1
        return counter

    def auto_deploy(self, Ship):
        ymax = 0
        xmax = 0
        ship_length = Ship.Length - 1
        orientation = random.randint(1, 2)
        if orientation == 1: #Horizontal
            xmax = self.Grid.Max - ship_length
            ymax = self.Grid.Max
        else:                #vertical
            xmax = self.Grid.Max
            ymax = self.Grid.Max - ship_length
        loop = True
        while loop == True:
            potential_placement = []
            X = random.randint(1,xmax)
            Y = random.randint(1,ymax)
            anchor = [Y, X]
            potential_placement.append(anchor) #first point of placement
            for point in range(1, Ship.Length):
                next_point = []
                if orientation == 1: #Horizontal
                    X += 1
                    next_point = [Y, X]
                else:                #Vertical
                    Y += 1
                    next_point = [Y, X]
                potential_placement.append(next_point)
            occupied = False
            for ship in self.Ships.keys():
                for point in self.Ships[ship].Info.keys():
                    if point == "Points":
                        lst = self.Ships[ship].Info["Points"]
                        for z in range(len(lst)):
                            for y in range(len(lst[z])):
                                for potential_point in range(len(potential_placement)):
                                    if "Point" in lst[z]:
                                        if lst[z]["Point"] == self.Grid.translate_grid(potential_placement[potential_point]):
                                            occupied = True
            if occupied == False:
                loop = False
                for a in range(len(potential_placement)):
                    location = self.Grid.translate_grid(potential_placement[a])
                    b = {"Point": location, "Status": "Hidden"}
                    self.Grid.update_grid(location[0], int(location[1:]), "Hidden")
                    Ship.Points.append(b)

    def update_guess_list(self, Guess, Status):
        self.Guesses[Guess] = Status
        row = self.Guess_Grid.translate_key(Guess)[0]
        column = int(self.Guess_Grid.translate_key(Guess)[1])
        self.Guess_Grid.update_grid(row, column, Status)

    def check_guess(self, Guess):
        Hit = False
        Ship = ""
        for ship in self.Ships.keys():
            for point in range(len(self.Ships[ship].Points)):
                if Guess == self.Ships[ship].Points[point]["Point"]:
                    self.Ships[ship].Points[point]["Status"] = "Hit"
                    Hit = True
                    Ship = ship
        return [Hit, Ship]

class AI(Player):
    pass