import unittest
import board
class TestBoard(unittest.TestCase):

    def test_generate_hexagon_colors(self):
        b = board.board()
        colors = b.generate_hexagon_colors()
        self.assertEqual(len(colors), 19)  # Assuming 19 hexagons are generated

    def test_generate_hexagon_numbers(self):
        b = board.board()
        numbers = b.generate_hexagon_numbers()
        self.assertEqual(len(numbers), 18)  # Assuming 18 numbers are generated

if __name__ == '__main__':
    unittest.main()