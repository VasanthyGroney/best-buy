from products import Product


class Store:
    def __init__(self, products=None):
        """
        Initialize a new store with a list of products.

        :param products: A list of Product objects.
        """
        if products is None:
            self.products = []
        elif isinstance(products, list) and all(isinstance(p, Product) for p in products):
            self.products = products
        else:
            raise ValueError("Products must be a list of Product objects")

    def add_product(self, product: Product):
        """
        Add a product to the store.

        :param product: The Product object to add.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        self.products.append(product)
        print(f"Product {product.name} is added")

    def remove_product(self, product: Product):
        """
        Remove a product from the store.

        :param product: The Product object to remove.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product.name} removed from store.")
        else:
            print(f"Product {product.name} not available")

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all products in the store.

        :return: The total quantity.
        """
        total_quantity = sum(product.quantity for product in self.products)
        return total_quantity

    def get_all_products(self) -> list:
        """
        Get a list of all products in the store.

        :return: A list of Product objects.
        """
        return list(self.products)

    def order(self, shopping_list: list) -> float:
        """
        Process an order for a list of products.

        :param shopping_list: A list of tuples containing Product objects and quantities.
        :return: The total price for the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise ValueError("Invalid product")
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError("Quantity must be a non-negative integer")
            if product in self.products:
                try:
                    total_price += product.buy(quantity)
                except ValueError as e:
                    print(f"Could not order {product.name}: {e}")
            else:
                print(f"Product {product.name} not available in the store")
        return total_price
