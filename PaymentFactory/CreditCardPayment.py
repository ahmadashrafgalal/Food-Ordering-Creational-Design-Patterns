from .Payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount}$ using Credit Card.")