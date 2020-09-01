import unittest
from Ship import Ship

class TestShipMethods(unittest.TestCase):

    def test_basic(self):
        "Ship should not be already sunk when created"
        ship = Ship("Patrol Boat")
        assert not ship.check_status()

    def test_length(self):
        "Checks to see if each ship is the correct length"
        patrol_boat = Ship("Patrol Boat")
        submarine = Ship("Submarine")
        destroyer = Ship("Destroyer")
        battleship = Ship("Battleship")
        aircraft_carrier = Ship("Aircraft Carrier")
        self.assertEqual(patrol_boat.Length, 2)
        self.assertEqual(submarine.Length, 3)
        self.assertEqual(destroyer.Length, 3)
        self.assertEqual(battleship.Length, 4)
        self.assertEqual(aircraft_carrier.Length, 5)
        self.assertRaises(Exception, Ship, "Banana")

    def test_check_status(self):
        patrol_boat = Ship("Patrol Boat")
        point1 = {"Point": "A1", "Status": "Hit"}
        point2 = {"Point": "A2", "Status": "Hit"}
        patrol_boat.Points.append(point1)
        patrol_boat.Points.append(point2)
        #The status of each point should change to "Sunk" and ship.Sunk should become True
        self.assertEqual(patrol_boat.check_status(), True)
        self.assertEqual(patrol_boat.Points[0]["Status"], "Sunk")
        self.assertEqual(patrol_boat.Points[1]["Status"], "Sunk")
        self.assertEqual(patrol_boat.Sunk, True)

if __name__ == '__main__':
    unittest.main()
