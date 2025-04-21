from product_2_step_2 import *


class Store:
    def __init__(self, products=None):
        self.products = products or []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Only instances of Product can be added.")
        self.products.append(product)
        print(f"{product.name} has been added to the store.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} has been removed from the store.")
        else:
            print(f"{product.name} is not in the store.")

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products if product.quantity is not None)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if not product.is_active():
                print(f"{product.name} is inactive.")
                continue

            if product.quantity is not None:
                if product.quantity < quantity:
                    print(f"{product.name} is not available in the requested quantity.")
                    continue

            total_price += product.buy(quantity)
            print(f"Added {quantity} of {product.name} to the order.")

        return total_price


    def show_items(self):
        print("Inventory")
        for product in self.products:
            print(f"{product}")

second_half = SecondHalfPrice("Second Half Price")
third_free = ThirdOneFree("Third One Free!")
perc_disc = PercentDiscount("30% off", 30)


store = Store(
    [Product("MacBook Air M2", price=50, quantity=10, promotion=second_half),
     Product("Bose QuietComfort Earbuds", price=40, quantity=50, promotion=third_free),
     Product("Google Pixel 7", price=30, quantity=25, promotion=None),
     NonStockedProduct("Windows License", price=20, promotion=perc_disc),
     LimitedProduct("Shipping Fee", price=10, quantity=20, maximum=1),
    ]
)
