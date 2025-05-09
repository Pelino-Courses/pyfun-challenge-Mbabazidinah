# docstring
""" This is a class which uses methods to add a product, remove a product, calculate
 the total amount of the product, and display the output.
"""

class Product:  # Class definition
    def __init__(self, name: str, price: float, quantity: int):  # Constructor
        self.name = name
        self.price = price
        self.quantity = quantity
        if price < 0:  # Validation of inputs
            raise ValueError("Price must be positive")  # Error handling
        if quantity < 0:
            raise ValueError("Quantity must be positive")

    def add_quantity(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.quantity += amount

    def remove_quantity(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount must be positive")
        if amount > self.quantity:
            raise ValueError("Insufficient quantity to remove")
        self.quantity -= amount

    def total(self) -> float:
        return self.quantity * self.price

    def __str__(self):
        return (
            f"Product name: {self.name}\n"
            f"Product price: {self.price}\n"
            f"Product quantity: {self.quantity}\n"
            f"Total value: {self.total()}"
        )
    

