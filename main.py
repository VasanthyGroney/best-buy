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

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} is added")


    def remove_product(self, product):
        if product in self.product:
            self.product.remove(product)
            print(f"Product {product.name} removed from store.")
        else:
            print(f"Product {product.name} not available")

    def get_total_quantity(self):
        total_quantity = sum(product.quantity for product in self.products)
        return total_quantity

    def get_all_products(self):
        list_products = list(self.products)
        return list_products

    def oder(self, shopping_list):

        total_price = 0
        for product, quantity in order:
            total_price += product.price * quantity
        return total_price
















