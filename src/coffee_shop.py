class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, customer, drink_name):
        for drink in self.drinks:
            if drink_name == drink.name:
                customer.reduce_money(drink.price)
                self.increase_till(drink.price)