class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = 0


    def reduce_money(self, amount):
        self.wallet -= amount

    def add_or_reduce_energy(self, amount):
        self.energy += amount
    