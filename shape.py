from numbers import Number
from validations import validate_coordinates

class Shape:
    """
    A class Shape to represent the center position of a Shape
     Attributes:
     - x (Number): coordinate on X-axis
     - y (Number): coordinate on Y-axis
    
    Example usage:
    >>> shape1=Shape(8, -2)
    """

    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y
  
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        validate_coordinates(x)     
        self._x = x


    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        validate_coordinates(y)     
        self._y = y

    def __repr__(self):
        return f"Coordinates (x = {self.x}, y = {self.y})"

