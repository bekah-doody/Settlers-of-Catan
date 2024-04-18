# import unittest
# import player
# class TestPlayer(unittest.TestCase):
#     def setUp(self):
#         self.test_player = player.Player("TestPlayer", (255, 0, 0))
#
#     def test_initial_values(self):
#         self.assertEqual(self.test_player.name, "TestPlayer")
#         self.assertEqual(self.test_player.color, (255, 0, 0))
#         self.assertEqual(self.test_player.wood, 0)
#         self.assertEqual(self.test_player.brick, 0)
#         self.assertEqual(self.test_player.sheep, 0)
#         self.assertEqual(self.test_player.wheat, 0)
#         self.assertEqual(self.test_player.ore, 0)
#         self.assertEqual(self.test_player.settlements, 0)
#         self.assertEqual(self.test_player.cities, 0)
#         self.assertEqual(self.test_player.roads, 0)
#         self.assertEqual(self.test_player.turn, 0)
#         # self.assertEqual(self.test_player.cards, [])
#
#     def test_name_setter(self):
#         self.test_player.name = "NewPlayer"
#         self.assertEqual(self.test_player.name, "NewPlayer")
#
#     def test_add_resources(self):
#         self.test_player.collect_wood(2)
#         self.test_player.collect_brick(3)
#         self.test_player.collect_sheep(1)
#         self.test_player.collect_wheat(4)
#         self.test_player.collect_ore(2)
#         self.assertEqual(self.test_player.wood, 2)
#         self.assertEqual(self.test_player.brick, 3)
#         self.assertEqual(self.test_player.sheep, 1)
#         self.assertEqual(self.test_player.wheat, 4)
#         self.assertEqual(self.test_player.ore, 2)
#         # self.assertEqual(len(self.test_player.cards), 12)
#
#     def test_add_settlement(self):
#         self.test_player.add_settlement()
#         self.assertEqual(self.test_player.settlements, 1)
#
#     def test_add_city(self):
#         self.test_player.add_city()
#         self.assertEqual(self.test_player.cities, 1)
#         self.assertEqual(self.test_player.settlements, -1)
#
#     def test_add_road(self):
#         self.test_player.add_road()
#         self.assertEqual(self.test_player.roads, 1)
#
#     def test_next_turn(self):
#         self.test_player.next_turn()
#         self.assertEqual(self.test_player.turn, 1)
#
#
# if __name__ == '__main__':
#     unittest.main()