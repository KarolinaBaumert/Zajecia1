from ecommerce.product.product import Product


class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def total_price(self):
        return sum(product.price for product in self.items)

    def __str__(self):
        return ', '.join(str(product) for product in self.items)
