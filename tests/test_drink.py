import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Latte", 3, 5)

    def test_drink_has_name(self):
        self.assertEqual("Latte", self.drink.name)

    def test_price_has_price(self):
        self.assertEqual(3, self.drink.price)
    
    def test_drink_has_caffeine(self):
        self.assertEqual(5, self.drink.caffeine_level)