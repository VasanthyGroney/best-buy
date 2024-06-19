class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product with a name, price, and quantity.
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
        self.promotion = None

    def set_promotion(self, promotion):
        """
        Set a promotion for the product.

        :param promotion: The promotion to be applied.
        """
        self.promotion = promotion

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
        if self.promotion:
            return self.promotion.apply_promotion(self, amount)
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
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo_info}")

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the product.

        :param quantity: The new quantity of the product.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.quantity = quantity


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int):
        raise ValueError("Cannot set quantity for non-stocked products")

    def buy(self, amount: int) -> float:
        return self.price * amount

    def show(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: Unlimited")


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initialize a limited product with a name, price, quantity, and maximum purchase limit.
        """
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum must be a positive integer")
        self.maximum = maximum

    def buy(self, amount: int) -> float:
        if amount > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} units of {self.name} at a time.")
        return super().buy(amount)

    def show(self):
        """
        Display the details of the limited product.
        """
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}{promo_info}")
