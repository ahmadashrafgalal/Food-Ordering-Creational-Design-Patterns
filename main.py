from BurgerBuilder import CustomBurgerBuilder
from Orders import OrderManager
from PaymentFactory import PaymentFactory, CashOnDeliveryPayment, PayPalPayment, CreditCardPayment
from MealPrototype import Meal, MealRegistry


PaymentFactory.add_payment("credit", CreditCardPayment)
PaymentFactory.add_payment("paypal", PayPalPayment)
PaymentFactory.add_payment("cash", CashOnDeliveryPayment)


order_manager = OrderManager()

meal_registry = MealRegistry()
meal_registry.register_meal("pizza_combo", Meal("Pizza Combo", ["Pizza", "Cola", "Salad"]))
meal_registry.register_meal("sushi_combo", Meal("Sushi Combo", ["Sushi", "Green Tea", "Miso Soup"]))

while True:
    
    print("""\n--- Online Food Ordering ---
    1. Build custom burger
    2. Order pre-made meal
    3. Show all orders
    4. Exit""")

    choice = input("Choose: ")

    if choice == "1":
        builder = CustomBurgerBuilder()
        bread = input("Choose bread: ")
        meat = input("Choose meat: ")
        topping = input("Add a topping: ")
        sauce = input("Choose sauce: ")

        burger = (builder.set_bread(bread)
                            .set_meat(meat)
                            .add_topping(topping)
                            .set_sauce(sauce)
                            .build())

        order_manager.add_order(str(burger))

        pay_method = input(f"Payment method {PaymentFactory.get_available_payments()}: ")
        payment = PaymentFactory.create_payment(pay_method)
        payment.pay(10)

    elif choice == "2":
        meal_type = input(f"Choose meal {meal_registry.get_available_meals()}: ")
        meal = meal_registry.get_meal(meal_type)
        if meal:
            order_manager.add_order(str(meal))
            pay_method = input(f"Payment method {PaymentFactory.get_available_payments()}: ")
            payment = PaymentFactory.create_payment(pay_method)
            payment.pay(15)
        else:
            print("Meal not found.")

    elif choice == "3":
        order_manager.show_orders()

    elif choice == "4":
        break
    else:
        print("Invalid choice.")
