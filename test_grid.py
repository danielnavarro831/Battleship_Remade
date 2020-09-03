import unittest
from Grid import Grid
from Player import Player

class TestGridMethods(unittest.TestCase):
    def setUp(self):
        self.grid1 = Grid()

    def test_size(self):
        #Grid size is 10x10
        self.assertEqual(self.grid1.Min, 1)
        self.assertEqual(self.grid1.Max, 10)
        self.assertEqual("J" in self.grid1.grid, True)
        self.assertEqual("K" in self.grid1.grid, False)
        self.assertEqual(10 in self.grid1.grid["J"], True)
        self.assertEqual(11 in self.grid1.grid["J"], False)

    def test_status_initialization(self):
        #Each cell should initialize as "Blank"
        for row in self.grid1.grid.keys():
            for column in self.grid1.grid[row].keys():
                self.assertEqual(self.grid1.grid[row][column], "Blank")

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
        p1 = Player("Player1", 1)
        p1.Guesses = {"A1": "Hit", "A2":"Miss", "B1":"Hit"}
        self.grid1.set_guess_grid(p1)
        self.assertEqual(self.grid1.grid["A"][1], "Hit")
        self.assertEqual(self.grid1.grid["A"][2], "Miss")
        self.assertEqual(self.grid1.grid["B"][1], "Hit")

if __name__ == '__main__':
    unittest.main()