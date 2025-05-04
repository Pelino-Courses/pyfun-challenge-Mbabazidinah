import math

class Shape:
    """Abstract base class for shapes."""
    def __init__(self, name):
        if not name:
            raise ValueError("Shape must have a name.")
        self.name = name

    def area(self):
        """Return the area of the shape."""
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        """Return string representation of the shape."""
        return self.name


class Circle(Shape):
    """Represents a circle with a radius."""
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{self.name}: radius={self.radius}, area={self.area():.1f}"


class Rectangle(Shape):
    """Represents a rectangle with width and height."""
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of the rectangle."""
        return self.width * self.height

    def __str__(self):
        return f"{self.name}: width={self.width}, height={self.height}, area={self.area():.1f}"


class Triangle(Shape):
    """Represents a triangle with base and height."""
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        """Calculate area of the triangle."""
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{self.name}: base={self.base}, height={self.height}, area={self.area():.1f}"
