import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Alan", 20 , 30 )
        self.customer2 = Customer("Joy", 30 , 14 )
        self.drink = Drink("mocha", 4, 5)
        self.food = Food("burger", 10, -10)
        self.coffee_shop = CoffeeShop("Starbucks", 50, [self.drink], [self.food])
        
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Starbucks", self.coffee_shop.name)
    

    def test_coffee_shop_till_amount(self):
        self.assertEqual(50, self.coffee_shop.till)
    

    def test_coffee_shop_has_drinks(self):
        self.assertEqual("mocha", self.coffee_shop.drinks[0].name)
    

    def test_coffee_shop_has_food(self):
        self.assertEqual("burger", self.coffee_shop.foods[0].name)


    def test_increase_till(self):
        self.coffee_shop.increase_till(4)
        self.assertEqual(54, self.coffee_shop.till)
    
    
    def test_add_stock(self):
        self.coffee_shop.add_stock("mocha", 100)
        self.assertEqual(100, self.coffee_shop.stock["mocha"] )

    def test_find_drink(self):
        drink_found = self.coffee_shop.find_drink("mocha")
        self.assertEqual("mocha", drink_found.name)


    def test_find_food(self):
        food_found = self.coffee_shop.find_food("burger")
        self.assertEqual("burger", food_found.name) 


    def test_can_sell_drink(self):
        self.coffee_shop.sell_drink(self.customer, "mocha")
        self.assertEqual(16, self.customer.wallet)
        self.assertEqual(5, self.customer.energy)
        self.assertEqual(54, self.coffee_shop.till)


    def test_can_sell_food(self):
        self.coffee_shop.sell_food(self.customer, "burger")
        self.assertEqual(10, self.customer.wallet)
        self.assertEqual(-10, self.customer.energy)
        self.assertEqual(60, self.coffee_shop.till)


    def test_cannot_sell_underage(self):
        self.coffee_shop.sell_drink(self.customer2, "mocha")
        self.assertEqual(30, self.customer2.wallet)
        self.assertEqual(0, self.customer2.energy)
        self.assertEqual(50, self.coffee_shop.till)


    def test_cannot_sell_energy_levels(self):
        self.coffee_shop.sell_drink(self.customer, "mocha")
        self.coffee_shop.sell_drink(self.customer, "mocha")
        self.coffee_shop.sell_drink(self.customer, "mocha")
        self.assertEqual(12, self.customer.wallet)
        self.assertEqual(10, self.customer.energy)
        self.assertEqual(58, self.coffee_shop.till)


    


