import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Alan", 20 )
        self.drink = Drink("mocha", 4)
        self.coffee_shop = CoffeeShop("Starbucks", 50, [self.drink])

    def test_has_name(self):
        self.assertEqual("Alan", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_can_buy_drink(self):
        self.customer.wallet = 20
        self.customer.buy_drink(self.coffee_shop, "mocha")
        self.assertEqual(16, self.customer.wallet)
        self.assertEqual(54, self.coffee_shop.till)

    def test_reduce_money(self):
        self.customer.wallet = 20
        self.customer.reduce_money(5)
        self.assertEqual(15, self.customer.wallet)
    
    