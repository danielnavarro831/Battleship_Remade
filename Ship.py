
class Ship:
    def __init__(self, Name):
        self.Name = Name
        if Name == "Patrol Boat":
            self.Length = 2
        elif Name == "Submarine" or Name == "Destroyer":
            self.Length = 3
        elif Name == "Battleship":
            self.Length = 4
        elif Name == "Aircraft Carrier":
            self.Length = 5
        self.Points = []
        #Points = [{Point: A1, Status: Hit}, {Point: A2, Status: Hit}, {Point: A3, Status: Blank}]
        self.Sunk = False
        self.Info = {"Name": self.Name, "Length": self.Length, "Points": self.Points, "Sunk": self.Sunk}

    def check_status(self):
        counter = 0
        sunk = False
        for point in range(len(self.Points)):
            if self.Points[point]["Status"] == "Hit":
                counter += 1
        if counter == self.Length:
            self.Sunk = True
            for point in range(len(self.Points)):
                self.Points[point]["Status"] = "Sunk"
            sunk = True
        return sunk