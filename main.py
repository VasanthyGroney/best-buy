class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount > self.quantity:
            return "Not enough stock available"
        else:
            self.quantity -= amount
            return f"{amount} units of {self.name} bought. {self.quantity} remaining."

    def is_active(self):
        return self.quantity > 0

    def show(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def set_quantity(self, quantity):
        self.quantity = quantity



