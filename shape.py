from numbers import Number
from Lab2.validate_coordinates import validate_coordinates
# class Shape to represent the center position of the object

class Shape:
    def __init__(self, x: float, y: float):
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
        return f"Coordinates: x = {self.x}, y = {self.y}"

