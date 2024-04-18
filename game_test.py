import unittest
import game
import pygame
class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game_instance = game.Game()

    def tearDown(self):
        pygame.quit()

    def test_generate_vertices(self):
        self.game_instance.generate_vertices()
        self.assertEqual(len(self.game_instance.vertices), 54)

    # def test_change_player(self):
    #     self.game_instance.current_player = self.game_instance.players[0]
    #     self.game_instance.change_player()
    #     self.assertEqual(self.game_instance.current_player, self.game_instance.players[1])

    def test_roll_die(self):
        result = self.game_instance.roll_die()
        self.assertTrue(1 <= result <= 6)

    def test_roll_dice(self):
        result1, result2 = self.game_instance.roll_dice()
        self.assertTrue(1 <= result1 <= 6)
        self.assertTrue(1 <= result2 <= 6)


if __name__ == '__main__':
    unittest.main()