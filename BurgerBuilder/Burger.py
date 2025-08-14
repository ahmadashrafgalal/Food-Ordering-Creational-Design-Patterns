class Burger:
    def __init__(self):
        self.bread = None
        self.meat = None
        self.toppings = []
        self.sauce = None

    def __str__(self):
        return f"Bread: {self.bread}, Meat: {self.meat}, Toppings: {self.toppings}, Sauce: {self.sauce}"
