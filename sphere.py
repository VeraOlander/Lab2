from circle import Circle
from validations import validate_coordinates
from validations import validate_parameters
import math



class Sphere(Circle):
    """
    A class to create a Sphere object
     Attributes:     
     - radius (Number): the distance from the center to the edge of a Sphere, larger than 0, inherited from parent class Circle
     - x: x-coordinate, inherited from parent class Circle, default value 0
     - y: y-coordinate, inherited from parent class Circle, default value 0
     - surface_area: calculated from radius
     - volume: calculated from radius
     ...
    Methods:
    - __eq__: == operator overload to compare Sphere instances by their radiuses
    - __lt__: < operator overload to compare Sphere instances by their radiuses
    - __le__: <= operator overload to compare Sphere instances by their radiuses
    - __gt__: > operator overload to compare Sphere instances by their radiuses
    - __ge__: >= operator overload to compare Sphere instances by their radiuses
    - translate(): moves the object by changing x and y coordinates

    Example usage:
    >>> sphere1=Sphere(1,0,0)
    >>> sphere1.surface_area
    >>> sphere1.translate(4,5)
    """
        
    def __init__(self, radius: float | int, x: float | int = 0, y: float | int = 0):
        super().__init__(radius, x, y)
        
    @property
    def volume(self):
        return (4/3) * math.pi * (self._radius ** 3)
     
    @property
    def surface_area(self):
        return 4 * math.pi * (self._radius ** 2)

    def __repr__(self):
        return f"Sphere (radius = {self.radius}, center coordinates: x = {self.x}, y = {self.y})"
    
    def __str__(self):
        return f"This is a sphere with a radius = {self.radius} and center coordinates: x = {self.x}, y = {self.y}"
    
    def __eq__(self, other):
        if isinstance(other, Sphere):
            return self.radius == other.radius
        return False
               
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius
    
    def translate(self, move_x, move_y):
        validate_coordinates(move_x)
        validate_coordinates(move_y)
        self.x +=move_x
        self.y +=move_y