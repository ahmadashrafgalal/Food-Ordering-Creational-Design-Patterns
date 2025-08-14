from .Payment import Payment


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount}$ using PayPal.")