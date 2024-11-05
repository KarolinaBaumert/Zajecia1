from ecommerce.product.product import Product
from ecommerce.order.order import Order


def main():
    product1 = Product("Laptop", 999.99)
    product2 = Product("Smartphone", 499.99)

    order = Order()
    order.add_product(product1)
    order.add_product(product2)

    print("Zamówienie zawiera:")
    print(order)
    print(f"Całkowita cena: ${order.total_price():.2f}")


if __name__ == "__main__":
    main()
