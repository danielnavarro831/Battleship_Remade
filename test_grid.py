import unittest
from Grid import Grid
from Player import Player
from Battleship_Remade import Game

class TestGridMethods(unittest.TestCase):
    def setUp(self):
        self.grid1 = Grid("Easy")
        self.grid2 = Grid("Medium")
        self.grid3 = Grid("Hard")

    def test_size(self):
        #Easy = 10x10, Medium = 15x15, Hard = 20x20
        #Grid 1
        self.assertEqual(self.grid1.Min, 1)
        self.assertEqual(self.grid1.Max, 10)
        self.assertEqual("J" in self.grid1.grid, True)
        self.assertEqual("K" in self.grid1.grid, False)
        self.assertEqual(10 in self.grid1.grid["J"], True)
        self.assertEqual(11 in self.grid1.grid["J"], False)
        #Grid2
        self.assertEqual(self.grid2.Min, 1)
        self.assertEqual(self.grid2.Max, 15)
        self.assertEqual("O" in self.grid2.grid, True)
        self.assertEqual("P" in self.grid2.grid, False)
        self.assertEqual(15 in self.grid2.grid["O"], True)
        self.assertEqual(16 in self.grid2.grid["O"], False)
        #Grid3
        self.assertEqual(self.grid3.Min, 1)
        self.assertEqual(self.grid3.Max, 20)
        self.assertEqual("T" in self.grid3.grid, True)
        self.assertEqual("U" in self.grid3.grid, False)
        self.assertEqual(20 in self.grid3.grid["T"], True)
        self.assertEqual(21 in self.grid3.grid["T"], False)
        #Non-Easy, Medium, or Hard difficulty settings should raise an Exception
        self.assertRaises(Exception, Grid, "Legendary")

    def test_status_initialization(self):
        #Easy
        for row in self.grid1.grid.keys():
            for column in self.grid1.grid[row].keys():
                self.assertEqual(self.grid1.grid[row][column], "Blank")
        #Medium
        for row in self.grid2.grid.keys():
            for column in self.grid2.grid[row].keys():
                self.assertEqual(self.grid2.grid[row][column], "Blank")
        #Hard
        for row in self.grid3.grid.keys():
            for column in self.grid3.grid[row].keys():
                self.assertEqual(self.grid3.grid[row][column], "Blank")

    def test_translate_key(self):
        key = "C10"
        check = self.grid1.translate_key(key)
        self.assertEqual(check[0], "C")
        self.assertEqual(check[1], 10)

    def test_update_grid(self):
        self.grid1.update_grid("A", 1, "Hit")
        self.assertEqual(self.grid1.grid["A"][1], "Hit")

    def test_translate_grid(self):
        XY = [3, 6]
        translation = self.grid1.translate_grid(XY)
        self.assertEqual(translation, "C6")

    def test_translate_row(self):
        row = "J"
        translation = self.grid1.translate_row(row)
        self.assertEqual(translation, 10)

    def test_set_guess_grid(self):
        game = Game()
        game.Difficulty = "Easy"
        p1 = Player("Player1", game, 1)
        p1.Guesses = {"A1": "Hit", "A2":"Miss", "B1":"Hit"}
        self.grid1.set_guess_grid(p1)
        self.assertEqual(self.grid1.grid["A"][1], "Hit")
        self.assertEqual(self.grid1.grid["A"][2], "Miss")
        self.assertEqual(self.grid1.grid["B"][1], "Hit")

if __name__ == '__main__':
    unittest.main()