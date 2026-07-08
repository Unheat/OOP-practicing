import math


class Shape:
    def __init__(self, name: str):
        self._name = name

    def area(self) -> float:
        # TODO: return 0 by default
        return 0

    def perimeter(self) -> float:
        # TODO: return 0 by default
        return 0

    def describe(self):
        # TODO: print "Shape: name, Area: area, Perimeter: perimeter"
        # Hint: use f"{value:.2f}" for formatting
        print(f"Shape: {self._name}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")
    
# '''
# so like interface will like force implement why inheritance dont, is that the core idea, so in my it is does not force implement as it return 0
# by default so it is inheritance but if we force it is interface
# '''
# import math
# from abc import ABC, abstractmethod

# # Shape is now an Abstract Base Class (serving as both interface and base parent)
# class Shape(ABC):
#     def __init__(self, name: str):
#         self._name = name

#     @abstractmethod
#     def area(self) -> float:
#         """Contract: Subclasses MUST implement this, or Python will crash."""
#         pass

#     @abstractmethod
#     def perimeter(self) -> float:
#         """Contract: Subclasses MUST implement this, or Python will crash."""
#         pass

#     def describe(self):
#         # Concrete logic: Inherited and reused perfectly by child classes
#         print(f"Shape: {self._name}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        # TODO: initialize self._radius
        self.radius = radius
    def area(self) -> float:
        # TODO: return math.pi * radius * radius
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        # TODO: return 2 * math.pi * radius
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        # TODO: initialize self._width and self._height
        self.width = width
        self.height = height

    def area(self) -> float:
        # TODO: return width * height
        return self.width * self.height

    def perimeter(self) -> float:
        # TODO: return 2 * (width + height)
        return 2*(self.width + self.height)


if __name__ == "__main__":
    circle = Circle(5.0)
    circle.describe()

    rect = Rectangle(4.0, 6.0)
    rect.describe()
    