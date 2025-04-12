class Product:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert len(name) >= 5, f"Product name must be at least 5 characters long!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError(f"Quantity {quantity} cannot be less than zero!")
        self.quantity = quantity

    def is_active(self):
        return self.quantity > 0

    def activate(self):
        if self.quantity <= 0:
            self.quantity = 1
        print(f"{self.name} has been activated.")

    def deactivate(self):
        self.quantity = 0
        print(f"{self.name} has been deactivated")

    def show(self):
        return f"{self.name}, {self.price}, {self.quantity}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough stock to complete purchase.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        return f"{self.name} {self.price} (Non-stocked)"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum}")
        return super().buy(quantity)

    def show(self):
        return f"{self.name} - {self.price} (Limit: {self.maximum} per order, Stock: {self.quantity})"





