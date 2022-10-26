import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Alan", 20 , 30 )


    def test_has_name(self):
        self.assertEqual("Alan", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(30, self.customer.age)

    def test_has_energy(self):
        self.assertEqual(0, self.customer.energy)


    def test_reduce_money(self):
        self.customer.reduce_money(5)
        self.assertEqual(15, self.customer.wallet)

    
    
    
    