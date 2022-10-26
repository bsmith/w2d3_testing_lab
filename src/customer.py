class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


    def reduce_money(self, amount):
        self.wallet -= amount


    def buy_drink(self, coffee_shop, drink_name):
        for drink in coffee_shop.drinks:
            if drink_name == drink.name:
                self.reduce_money(drink.price)
                coffee_shop.increase_till(drink.price)
                