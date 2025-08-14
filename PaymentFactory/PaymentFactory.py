from . import CashOnDeliveryPayment, CreditCardPayment, PayPalPayment

class PaymentFactory:
    _payments =  {}

    @staticmethod
    def add_payment(payment_name, payment_class):
        PaymentFactory._payments[payment_name] = payment_class

    @staticmethod
    def create_payment(method):
        payment_class = PaymentFactory._payments.get(method)
        if payment_class:
            return payment_class()
        else:
            raise ValueError("Unknown payment method")
        
    @staticmethod
    def get_available_payments():
        return " ( " + " / ".join(PaymentFactory._payments.keys()) + " ) " 