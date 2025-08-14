class OrderManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(OrderManager, cls).__new__(cls)
            cls.__instance.orders = []
        return cls.__instance

    def add_order(self, order):
        self.orders.append(order)

    def show_orders(self):
        for idx, order in enumerate(self.orders, start=1):
            print(f"{idx}. {order}")
