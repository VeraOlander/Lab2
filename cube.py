from shape import Shape
from numbers import Number
from validations import validate_coordinates
from validations import validate_parameters


class Cube(Shape):
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


