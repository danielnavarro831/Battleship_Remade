
class Grid:
    def __init__(self, Difficulty):
        self.Rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
                     "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        self.Min = 1
        self.Max = 1
        if Difficulty == "Easy":
            self.Max = 10
        elif Difficulty == "Medium":
            self.Max = 15
        elif Difficulty == "Hard":
            self.Max = 20
        else:
            raise Exception("Invalid Difficulty Setting:", Difficulty)
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

    def translate_key(self, Key):
        keys = []
        keys.append(Key[0])
        keys.append(int(Key[1:]))
        return keys

    def update_grid(self, Row, Column, Status):
        self.grid[Row][Column] = Status

    def translate_grid(self, Point):
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
        elif Point[0] == 11:
            point += "K"
        elif Point[0] == 12:
            point += "L"
        elif Point[0] == 13:
            point += "M"
        elif Point[0] == 14:
            point += "N"
        elif Point[0] == 15:
            point += "O"
        elif Point[0] == 16:
            point += "P"
        elif Point[0] == 17:
            point += "Q"
        elif Point[0] == 18:
            point += "R"
        elif Point[0] == 19:
            point += "S"
        elif Point[0] == 20:
            point += "T"
        point += str(Point[1])
        return point

    def translate_row(self, Row):
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
        elif Row == "K":
            return 11
        elif Row == "L":
            return 12
        elif Row == "M":
            return 13
        elif Row == "N":
            return 14
        elif Row == "O":
            return 15
        elif Row == "P":
            return 16
        elif Row == "Q":
            return 17
        elif Row == "R":
            return 18
        elif Row == "S":
            return 19
        elif Row == "T":
            return 20
