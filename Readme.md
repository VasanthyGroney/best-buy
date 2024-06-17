# Best Buy Store Management

This project implements a basic store management system in Python. It includes the functionality to manage products, display available products, show total quantity, and handle customer orders.

## File Structure


README.md
markdown
Copy code
# Best Buy Store Management

This project implements a basic store management system in Python. It includes the functionality to manage products, display available products, show total quantity, and handle customer orders.

## File Structure

best_buy/
│
├── main.py
├── products.py
├── store.py
└── README.md
## Classes

### Product

The `Product` class represents a product in the store.

#### Attributes:
- `name`: Name of the product (str)
- `price`: Price of the product (float)
- `quantity`: Quantity of the product available (int)
- `active`: Boolean indicating if the product is active (bool)

#### Methods:
- `__init__(self, name, price, quantity)`: Initializes a new product.
- `get_quantity(self)`: Returns the quantity of the product.
- `set_quantity(self, quantity)`: Sets the quantity of the product.
- `is_active(self)`: Returns if the product is active.
- `activate(self)`: Activates the product.
- `deactivate(self)`: Deactivates the product.
- `show(self)`: Returns a string representation of the product.
- `buy(self, quantity)`: Buys a given quantity of the product.

### Store

The `Store` class manages a collection of products.

#### Attributes:
- `products`: List of products in the store (list)

#### Methods:
- `__init__(self, products=None)`: Initializes the store with an optional list of products.
- `add_product(self, product)`: Adds a product to the store.
- `remove_product(self, product)`: Removes a product from the store.
- `get_all_products(self)`: Returns a list of all products in the store.
- `get_total_quantity(self)`: Returns the total quantity of all products in the store.
- `find_product(self, name)`: Finds a product by name.
- `buy_product(self, name, quantity)`: Buys a quantity of a product by name.
- `show_products(self)`: Displays all products in the store.
- `order(self, shopping_list)`: Processes an order given a shopping list of products and quantities.

## Running the Program

Ensure you are in the `best_buy` directory and run the `main.py` script:
