import unittest
import board
import pygame
import game
import player
import development_cards



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
        self.assertEqual(len(numbers), 18) # Assuming 18 numbers are generated

class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game_instance = game.Game()

    def tearDown(self):
        pygame.quit()

    def test_generate_vertices(self):
        self.game_instance.generate_vertices()
        self.assertEqual(len(self.game_instance.vertices), 72)

    def test_change_player(self):
        self.game_instance.current_player = self.game_instance.players[0]
        self.game_instance.change_player()
        self.assertEqual(self.game_instance.current_player, self.game_instance.players[1])

    def test_roll_die(self):
        result = self.game_instance.roll_die()
        self.assertTrue(1 <= result <= 6)

    def test_roll_dice(self):
        result1, result2 = self.game_instance.roll_dice()
        self.assertTrue(1 <= result1 <= 6)
        self.assertTrue(1 <= result2 <= 6)

class TestVertex(unittest.TestCase):
    def setUp(self):
        self.vertex_instance = game.Vertex(100,100)

    def test_buy_settlement(self):
        player_instance = player.Player("player1", ((255, 165, 0)))
        self.vertex_instance.buy_settlement(player_instance)
        self.assertTrue(self.vertex_instance.settlement)
        self.assertEqual(self.vertex_instance.color, player_instance.color)


class TestDevelopmentCards(unittest.TestCase):
    def test_knight_card_str(self):
        knight_card = development_cards.KnightCard()
        output = knight_card.__str__()
        self.assertEqual(output, "Knight Card\nYou can move the robber! \n and you can steal 1 resource from the owner of a settlement\n or adjacent to the robber's new hex.")

    def test_road_building_str(self):
        road_building_card = development_cards.RoadBuilding()
        output = road_building_card.__str__()
        self.assertEqual(output, "Road Building Card\nPlace 2 new roads as if you had just built them!")

    def test_year_of_plenty_str(self):
        year_of_plenty_card = development_cards.YearOfPlenty()
        output = year_of_plenty_card.__str__()
        self.assertEqual(output, "Year of Plenty Card\nTake any 2 resources from the bank!\nAdd them to your hand.\nThey can be 2 of the same or different resources")

    def test_monopoly_str(self):
        monopoly_card = development_cards.Monopoly()
        output = monopoly_card.__str__()
        self.assertEqual(output, "Monopoly Card\nWhen you play this card, announce 1 type of resource card.\nAll players must give you all of their resource cards of that type")

    def test_victory_point_str(self):
        victory_point_card = development_cards.VictoryPointCard()
        output = victory_point_card.__str__()
        self.assertEqual(output, "Victory Point Card\n1 free Victory Point! :D")


if __name__ == '__main__':
    unittest.main()
