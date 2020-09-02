import unittest
from Ship import Ship
from Player import Player
from Battleship_Remade import Game

class TestPlayerMethods(unittest.TestCase):
    def setUp(self):
        #Initializes before every test
        self.game = Game()
        self.game.Difficulty = "Easy"
        self.p1 = Player("Player 1", self.game, 1)

    def test_player_num(self):
        #Should only allow numbers 1 and 2
        p2 = Player("Player 2", self.game, 2)
        self.assertEqual(self.p1.Player_Num, 1)
        self.assertEqual(p2.Player_Num, 2)
        self.assertRaises(Exception, Player, "Player 3", self.game, 3)
        self.assertRaises(Exception, Player, "Player 0", self.game, 0)

    def test_player_ship_creation(self):
        #All 5 ships should exist in self.p1.Ships upon player class creation
        pb = "Patrol Boat" in self.p1.Ships
        sub = "Submarine" in self.p1.Ships
        dest = "Destroyer" in self.p1.Ships
        batt = "Battleship" in self.p1.Ships
        ac = "Aircraft Carrier" in self.p1.Ships
        self.assertEqual(pb, True)
        self.assertEqual(sub, True)
        self.assertEqual(dest, True)
        self.assertEqual(batt, True)
        self.assertEqual(ac, True)
        #All 5 ships should be named and initialized correctly upon player class creation
        self.assertEqual(self.p1.Ships["Patrol Boat"].Name, "Patrol Boat")
        self.assertEqual(self.p1.Ships["Submarine"].Name, "Submarine")
        self.assertEqual(self.p1.Ships["Destroyer"].Name, "Destroyer")
        self.assertEqual(self.p1.Ships["Battleship"].Name, "Battleship")
        self.assertEqual(self.p1.Ships["Aircraft Carrier"].Name, "Aircraft Carrier")

    def test_player_ships_alive(self):
        #No ships should be defaulted to sunk status upon player creation
        self.assertEqual(self.p1.get_ships_alive(), 5)

    def test_auto_deploy_ships(self):
        #Each ship should have the correct number of points equal to their length
        for ship in self.p1.Ships.keys():
            self.p1.auto_deploy(self.p1.Ships[ship])
        self.assertEqual(len(self.p1.Ships["Patrol Boat"].Points), 2)
        self.assertEqual(len(self.p1.Ships["Submarine"].Points), 3)
        self.assertEqual(len(self.p1.Ships["Destroyer"].Points), 3)
        self.assertEqual(len(self.p1.Ships["Battleship"].Points), 4)
        self.assertEqual(len(self.p1.Ships["Aircraft Carrier"].Points), 5)
        #Each point should be set to the 'Hidden' status for each ship when initialized
        for ship in self.p1.Ships.keys():
            for point in range(len(self.p1.Ships[ship].Points)):
                self.assertEqual(self.p1.Ships[ship].Points[point]["Status"], "Hidden")

    def test_updating_guess_list(self):
        #Guess is correctly added to the user's guess list and guess grid
        self.p1.update_guess_list("A1", "Miss")
        in_list = "A1" in self.p1.Guesses
        self.assertEqual(in_list, True)
        self.assertEqual(len(self.p1.Guesses), 1)
        self.assertEqual(self.p1.Guesses["A1"], "Miss")
        self.assertEqual(self.p1.Guess_Grid.grid["A"][1], "Miss")

    def test_check_guess(self):
        self.p1.auto_deploy(self.p1.Ships["Patrol Boat"])
        #check[0] should return True if the guess hits a ship. Check[1] should return the name of the ship hit
        guess = self.p1.Ships["Patrol Boat"].Points[0]["Point"]
        check = self.p1.check_guess(guess)
        self.assertEqual(check[0], True)
        self.assertEqual(check[1], "Patrol Boat")
        #The status of the ship's hit point should display as "Hit"
        self.assertEqual(self.p1.Ships["Patrol Boat"].Points[0]["Status"], "Hit")

if __name__ == '__main__':
    unittest.main()