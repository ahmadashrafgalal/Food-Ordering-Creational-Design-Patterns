from .Burger import Burger

class CustomBurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def set_bread(self, bread):
        self.burger.bread = bread
        return self

    def set_meat(self, meat):
        self.burger.meat = meat
        return self

    def add_topping(self, topping):
        self.burger.toppings.append(topping)
        return self

    def set_sauce(self, sauce):
        self.burger.sauce = sauce
        return self

    def build(self):
        return self.burger
