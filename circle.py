from shape import Shape
from numbers import Number
from validations import validate_coordinates
from validations import validate_parameters
import math
import matplotlib.patches as patches

class Circle(Shape):
    """
    A class to create a Circle object
     Attributes:     
     - radius (Number): the distance from the center to the edge of a circle, larger than 0
     - x: x-coordinate, inherited from parent class Shape, default value 0
     - y: y-coordinate, inherited from parent class Shape, default value 0
     - area: calculated from radius
     - circumference: calculated from radius
     ...
    Methods:
    - __eq__: == operator overload to compare circle instances by their radiuses
    - __lt__: < operator overload to compare circle instances by their radiuses
    - __le__: <= operator overload to compare circle instances by their radiuses
    - __gt__: > operator overload to compare circle instances by their radiuses
    - __ge__: >= operator overload to compare circle instances by their radiuses
    - translate(): moves the object by changing x and y coordinates
    - is_unit_circle(): checks whether a Circle instance is a unit circle
    - draw_circle(): creates a matplotlib circle patch out of a Circle class instance with the given parameters

    Example usage:
    >>> circle1=Circle(1,0,0)
    >>> circle1.area
    >>> circle1.is_unit_circle()
    >>> circle1.translate(4,5)
    """
        
    def __init__(self, radius: Number, x = 0, y = 0):
        super().__init__(x, y)
        self.radius=radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        validate_parameters(radius)        
        self._radius = radius

    @property
    def area(self):
        return math.pi * (self._radius ** 2)
    
    @property
    def circumference(self):
        return 2 * math.pi * self._radius

    def __repr__(self):
        return f"Circle (radius = {self.radius}, x = {self.x}, y = {self.y})"
    
    def __str__(self):
        return f"This is a circle with a radius = {self.radius} and center coordinates: x = {self.x}, y = {self.y}"
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False
               
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return False
    
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return False
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return False
    
    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return False
    
    def translate(self, move_x, move_y):
        validate_coordinates(move_x)
        validate_coordinates(move_y)
        self.x +=move_x
        self.y +=move_y

    def is_unit_circle(self):
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False
        
    def draw_circle(self, ax):
        circle_patch = patches.Circle((self.x, self.y), self.radius, edgecolor='blue', facecolor='none', linewidth=2)
        ax.add_patch(circle_patch)
        ax.plot(self.x, self.y, marker='o', color='blue', markersize=2)
        ax.set_aspect('equal')
        return ax

        

