from abc import ABC, abstractmethod

class Promotions(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_promotion(self, price, quantity):
        pass


class SecondHalfPrice(Promotions):
    def set_promotion(self, price, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * price) + (half_price_items * price/2)


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