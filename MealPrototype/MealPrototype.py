class MealRegistry:
    def __init__(self):
        self._meals = {}

    def register_meal(self, key, meal):
        self._meals[key] = meal

    def get_meal(self, key):
        meal = self._meals.get(key)
        return meal.clone() if meal else None

    def get_available_meals(self):
        return " ( " + " / ".join(self._meals.keys()) + " ) "
