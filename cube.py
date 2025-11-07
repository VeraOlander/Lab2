from shape import Shape
from numbers import Number
from validations import validate_coordinates
from validations import validate_parameters


class Cube(Shape):
    """
    A class to create a Cube object
     Attributes:     
     - side (Number): the side length, larger than 0
     - x: x-coordinate, inherited from parent class Shape, default value 0
     - y: y-coordinate, inherited from parent class Shape, default value 0
     - surface_area: calculated from side length
     - volume: calculated from side length
     ...
    Methods:
    - __eq__: == operator overload to compare Cube instances by their side lengths
    - __lt__: < operator overload to compare Cube instances by their side lengths
    - __le__: <= operator overload to compare Cube instances by their side lengths
    - __gt__: > operator overload to compare Cube instances by their side lengths
    - __ge__: >= operator overload to compare Cube instances by their side lengths
    - translate(): moves the object by changing x and y coordinates

    Example usage:
    >>> cube1=Cube(1,0,0)
    >>> cube1.surface_area
    >>> cube1.translate(4,5)
    """
        
    def __init__(self, side: Number, x: Number = 0, y: Number = 0):
        super().__init__(x, y)
        self.side=side
                
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, side):
        validate_parameters(side)        
        self._side = side
        
    @property
    def surface_area(self):
        return 6 * (self._side ** 2)
    
    @property
    def volume(self):
        return self._side ** 3

    def __repr__(self):
        return f"Cube (side length = {self.side}, x = {self.x}, y = {self.y})"
    
    def __str__(self):
        return f"This is a cube with a side length = {self.side} and center coordinates: x = {self.x}, y = {self.y}"
    
    def __eq__(self, other):
        if isinstance(other, Cube):
            return self.side == other.side
        return False
               
    def __lt__(self, other):
        if isinstance(other, Cube):
            return self.side < other.side
        return False
    
    def __le__(self, other):
        if isinstance(other, Cube):
            return self.side <= other.side
        return False
    
    def __gt__(self, other):
        if isinstance(other, Cube):
            return self.side > other.side
        return False
    
    def __ge__(self, other):
        if isinstance(other, Cube):
            return self.side >= other.side
        return False
    
    def translate(self, move_x, move_y):
        validate_coordinates(move_x)
        validate_coordinates(move_y)
        self.x +=move_x
        self.y +=move_y


