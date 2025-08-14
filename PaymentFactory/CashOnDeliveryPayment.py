from .Payment import Payment

class CashOnDeliveryPayment(Payment):
    def pay(self, amount):
        print(f"Will pay {amount}$ in cash on delivery.")