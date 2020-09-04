
class Grid:
    def __init__(self):
        self.Rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.Min = 1
        self.Max = 10
        self.Blank = " "
        self.Hit = "X"
        self.Miss = "O"
        self.Hidden = "*"
        self.Sunk = self.Hit
        self.grid = {}
        row_counter = 0
        for a in range(self.Max):
            column_counter = 1
            row = {}
            for b in range(self.Max):
                row[column_counter] = "Blank"
                column_counter += 1
            self.grid[self.Rows[row_counter]] = row
            row_counter += 1
    #Grid = {A:{1:Blank, 2:Blank, 3:Blank...}, 
    #        B:{1:Blank, 2:Blank, 3:Blank...}, ...}

    def set_guess_grid(self, Player):
        for guess in Player.Guesses.keys():
            self.update_grid(self.translate_key(guess)[0], self.translate_key(guess)[1], Player.Guesses[guess])

    def update_grid(self, Row, Column, Status):
        self.grid[Row][int(Column)] = Status

    def translate_key(self, Key): #Translates A1 to [A, 1]
        keys = []
        keys.append(Key[0])
        keys.append(int(Key[1:]))
        return keys

    def translate_grid(self, Point): #Translates [1, 1] to A1
        point = ""
        if Point[0] == 1:
            point += "A"
        elif Point[0] == 2:
            point += "B"
        elif Point[0] == 3:
            point += "C"
        elif Point[0] == 4:
            point += "D"
        elif Point[0] == 5:
            point += "E"
        elif Point[0] == 6:
            point += "F"
        elif Point[0] == 7:
            point += "G"
        elif Point[0] == 8:
            point += "H"
        elif Point[0] == 9:
            point += "I"
        elif Point[0] == 10:
            point += "J"
        point += str(Point[1])
        return point

    def translate_row(self, Row): #Translates A to 1
        if Row == "A":
            return 1
        elif Row == "B":
            return 2
        elif Row == "C":
            return 3
        elif Row == "D":
            return 4
        elif Row == "E":
            return 5
        elif Row == "F":
            return 6
        elif Row == "G":
            return 7
        elif Row == "H":
            return 8
        elif Row == "I":
            return 9
        elif Row == "J":
            return 10
        else:
            return 11
