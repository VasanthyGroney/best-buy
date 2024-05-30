# setup initial stock of inventory
class Store:
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} is added")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product.name} removed from store.")
        else:
            print(f"Product {product.name} not available")

    def get_total_quantity(self):
        total_quantity = sum(product.quantity for product in self.products)
        return total_quantity

    def get_all_products(self):
        list_products = list(self.products)
        return list_products

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if quantity > 0:
                if product.quantity >= quantity:
                    product_total = product.price * quantity  # Calculate cost
                    total_price += product_total
                    product.quantity -= quantity  # Decrease the stock
                else:
                    print(f"Not enough stock for {product.name}. Only {product.quantity} available.")
                    continue
        return total_price





bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

store = Store([bose, mac])

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
store.add_product(pixel)


product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)