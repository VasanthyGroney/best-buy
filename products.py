class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product with a name, price, and quantity.

        :param name: Name of the product.
        :param price: Price of the product.
        :param quantity: Quantity of the product in stock.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")

        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount: int) -> float:
        """
        Buy a specified amount of the product, reducing the quantity in stock.

        :param amount: The amount to buy.
        :return: The total price for the amount bought.
        :raises ValueError: If the amount requested is greater than available stock.
        """
        if amount > self.quantity:
            raise ValueError("Not enough stock available")
        self.set_quantity(self.quantity - amount)
        return self.price * amount

    def is_active(self) -> bool:
        """
        Check if the product is active (i.e., has stock).

        :return: True if the product has stock, False otherwise.
        """
        return self.quantity > 0

    def show(self):
        """
        Display the details of the product.
        """
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the product.

        :param quantity: The new quantity of the product.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.quantity = quantity
