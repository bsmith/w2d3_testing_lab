import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("Starbucks", 50, ["mocha"])
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Starbucks", self.coffee_shop.name)
    
    def test_coffee_shop_till_amount(self):
        self.assertEqual(50, self.coffee_shop.till)
    
    def test_coffee_shop_has_drinks(self):
        self.assertEqual(["mocha"], self.coffee_shop.drinks)
    
    def test_increase_till(self):
        self.coffee_shop.increase_till(4)
        self.assertEqual(54, self.coffee_shop.till)
