class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price:.2f}₽"


class Order:
    all_orders = []

    def __init__(self, products):
        self.products = products
        Order.all_orders.append(self)

    def total_price(self):
        return sum(p.price for p in self.products)

    def apply_discount(self, discount_percent):
        return Discount.calculate_discount(self.total_price(), discount_percent)

    @classmethod
    def total_order_count(cls):
        return len(cls.all_orders)

    @classmethod
    def total_revenue(cls):
        return sum(order.total_price() for order in cls.all_orders)

    def __str__(self):
        product_list = '\n  '.join(str(p) for p in self.products)
        return f"Заказ:\n  {product_list}\n  Сумма заказа: {self.total_price():.2f}₽"


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        order_list = '\n\n'.join(str(order) for order in self.orders)
        return f"Клиент: {self.name}\nЗаказы:\n{order_list}" if self.orders else f"Клиент: {self.name}\nНет заказов"


class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def calculate_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(price):
        return Discount.calculate_discount(price, 15)

    @staticmethod
    def promo_code_discount(price):
        return Discount.calculate_discount(price, 25)

    def __str__(self):
        return f"{self.description} ({self.discount_percent}%)"

