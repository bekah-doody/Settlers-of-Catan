import unittest
import board
import pygame


class TestBoard(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.board_instance = board.board()

    def tearDown(self):
        pygame.quit()

    def test_generate_hexagon_colors(self):
        colors = self.board_instance.generate_hexagon_colors()
        self.assertEqual(len(colors), 19)  # Assuming 19 hexagons are generated

    def test_generate_hexagon_numbers(self):
        numbers = self.board_instance.generate_hexagon_numbers()
        self.assertEqual(len(numbers), 18)  # Assuming 18 numbers are generated



if __name__ == '__main__':
    unittest.main()
