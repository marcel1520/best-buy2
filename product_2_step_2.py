from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float, quantity=None, promotion=None):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity is None or quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert len(name) >= 5, f"Product name must be at least 5 characters long!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = promotion

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError(f"Quantity {quantity} cannot be less than zero!")
        self.quantity = quantity

    def is_active(self):
        return self.quantity is None or self.quantity > 0

    def activate(self):
        if self.quantity <= 0:
            self.quantity = 1
        print(f"{self.name} has been activated.")

    def deactivate(self):
        self.quantity = 0
        print(f"{self.name} has been deactivated")

    def show(self):
        return f"{self.name}, {self.price}, {self.quantity}, {self.promotion}"

    def buy(self, quantity):
        if self.quantity is None:
            return self.price * quantity

        if quantity > self.quantity:
            raise ValueError("Not enough stock to complete purchase.")

        self.quantity -= quantity

        if self.quantity is not None and self.quantity == 0:
            self.deactivate()

        if self.promotion:
            return self.promotion.set_promotion(self.price, quantity)
        return self.price * quantity

    def set_promotion(self, promotion):
        self.promotion = promotion

    def __str__(self):
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Promotion: {self.promotion}"


class NonStockedProduct(Product):
    def __init__(self, name, price, promotion=None):
        super().__init__(name, price, quantity=None, promotion=promotion)

    def show(self):
        return f"{self.name} {self.price} (Non-stocked)"

    def is_active(self):
        return True

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if self.promotion:
            return self.promotion.set_promotion(self.price, quantity)


        return self.price * quantity

    def __str__(self):
        promotion_str = f"Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: Unlimited, {promotion_str}"


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


class Promotions(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_promotion(self, price, quantity):
        pass

    def __str__(self):
        return self.name


class SecondHalfPrice(Promotions):
    def set_promotion(self, price, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * price) + (half_price_items * price / 2)


class ThirdOneFree(Promotions):
    def set_promotion(self, price, quantity):
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items - free_items


class PercentDiscount(Promotions):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def set_promotion(self, price, quantity):
        total = price * quantity
        discount = total * (self.percent / 100)
        return total - discount


