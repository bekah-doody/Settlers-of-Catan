import unittest
import development_cards

class TestDevelopmentCards(unittest.TestCase):
    def test_knight_card_str(self):
        knight_card = development_cards.KnightCard()
        output = knight_card.__str__()
        self.assertEqual(output,
                         "Knight Card\nYou can move the robber! \n and you can steal 1 resource from the owner of a settlement\n or adjacent to the robber's new hex.")

    def test_road_building_str(self):
        road_building_card = development_cards.RoadBuilding()
        output = road_building_card.__str__()
        self.assertEqual(output, "Road Building Card\nPlace 2 new roads as if you had just built them!")

    def test_year_of_plenty_str(self):
        year_of_plenty_card = development_cards.YearOfPlenty()
        output = year_of_plenty_card.__str__()
        self.assertEqual(output,
                         "Year of Plenty Card\nTake any 2 resources from the bank!\nAdd them to your hand.\nThey can be 2 of the same or different resources")

    def test_monopoly_str(self):
        monopoly_card = development_cards.Monopoly()
        output = monopoly_card.__str__()
        self.assertEqual(output,
                         "Monopoly Card\nWhen you play this card, announce 1 type of resource card.\nAll players must give you all of their resource cards of that type")

    def test_victory_point_str(self):
        victory_point_card = development_cards.VictoryPointCard()
        output = victory_point_card.__str__()
        self.assertEqual(output, "Victory Point Card\n1 free Victory Point! :D")

    def test_knight_card_check_materials(self):
        knight_card = development_cards.KnightCard()

        # Test with enough materials
        self.assertTrue(knight_card.CheckMaterials(ore=1, wheat=1, wool=1))

        # Test with insufficient materials
        self.assertFalse(knight_card.CheckMaterials(ore=0, wheat=1, wool=1))

    def test_road_building_card_check_materials(self):
        road_building_card = development_cards.RoadBuilding()

        # Test with enough materials
        self.assertTrue(road_building_card.CheckMaterials(ore=2, wheat=1, wool=1))

        # Test with insufficient materials
        self.assertFalse(road_building_card.CheckMaterials(ore=1, wheat=1, wool=1))

    def test_year_of_plenty_card_check_materials(self):
        year_of_plenty_card = development_cards.YearOfPlenty()

        # Test with enough materials
        self.assertTrue(year_of_plenty_card.CheckMaterials(ore=0, wheat=0, wool=0))

        # Test with insufficient materials
        self.assertFalse(year_of_plenty_card.CheckMaterials(ore=1, wheat=0, wool=0))

    def test_monopoly_card_check_materials(self):
        monopoly_card = development_cards.Monopoly()

        # Test with enough materials
        self.assertTrue(monopoly_card.CheckMaterials(ore=0, wheat=0, wool=0))

        # Test with insufficient materials
        self.assertFalse(monopoly_card.CheckMaterials(ore=1, wheat=0, wool=0))

if __name__ == '__main__':
    unittest.main()