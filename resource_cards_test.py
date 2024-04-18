import unittest
import resource_cards


class TestResourceCards(unittest.TestCase):
    def test_brick_card_str(self):
        brick_card = resource_cards.BrickCard()
        output = brick_card.__str__()
        self.assertEqual(output, "Brick Card")

    def test_wood_card_str(self):
        wood_card = resource_cards.WoodCard()
        output = wood_card.__str__()
        self.assertEqual(output, "Wood Card")

    def test_sheep_card_str(self):
        sheep_card = resource_cards.SheepCard()
        output = sheep_card.__str__()
        self.assertEqual(output, "Sheep Card")

    def test_wheat_card_str(self):
        wheat_card = resource_cards.WheatCard()
        output = wheat_card.__str__()
        self.assertEqual(output, "Wheat Card")

    def test_ore_card_str(self):
        ore_card = resource_cards.OreCard()
        output = ore_card.__str__()
        self.assertEqual(output, "Ore Card")


if __name__ == '__main__':
    unittest.main()
