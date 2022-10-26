import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food = Food("burger", 10, -10)

    def test_food_has_name(self):
        self.assertEqual("burger", self.food.name)

    def test_price_has_price(self):
        self.assertEqual(10, self.food.price)
    
    def test_food_has_rejuvenation(self):
        self.assertEqual(-10, self.food.rejuvenation)