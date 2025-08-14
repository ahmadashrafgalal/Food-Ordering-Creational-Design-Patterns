import copy

class Meal:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __str__(self):
        return f"{self.name} - Items: {', '.join(self.items)}"

    def clone(self):
        return copy.deepcopy(self)