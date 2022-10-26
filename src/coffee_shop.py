class CoffeeShop:
    def __init__(self, name, till, drinks, foods):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.foods = foods
        self.stock = {}
    
    def increase_till(self, amount):
        self.till += amount

    def add_stock(self, name, amount):
        if name in self.stock:
            self.stock[name] = self.stock[name] + amount
        else:
            self.stock[name] = amount

    def find_drink(self, drink_name):
        for drink in self.drinks:
            if drink_name == drink.name:
                return drink


    def find_food(self, food_name):
        for food in self.foods:
            if food_name == food.name:
                return food


    def sell_drink(self, customer, drink_name):
        drink = self.find_drink(drink_name)
        if customer.age >= 16 and customer.energy < 10:
                customer.reduce_money(drink.price)
                customer.add_or_reduce_energy(drink.caffeine_level)
                self.increase_till(drink.price)
    

    def sell_food(self, customer, food_name):
        food = self.find_food(food_name)
        customer.reduce_money(food.price)
        customer.add_or_reduce_energy(food.rejuvenation)
        self.increase_till(food.price)

   
   
   