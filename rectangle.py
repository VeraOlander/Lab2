from shape import Shape
from validate_coordinates import validate_coordinates
from validate_parameters import validate_parameters

class Rectangle(Shape):
    def __init__(self, length, width, x=0, y=0):
        super().__init__(x, y)
        self.length=length
        self.width=width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        validate_parameters(length)        
        self._length = length

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        validate_parameters(width)        
        self._width = width

    @property
    def area(self):
        return (self._length * self._width)
    
    @property
    def perimeter(self):
        return 2 * (self._length + self._width)

    def __repr__(self):
        return f"Rectangle with a length = {self.length}, width = {self.width} and coordinates: x = {self.x}, y = {self.y}"
    
    def __str__(self):
        return f"This is a rectangle with a length = {self.length}, width = {self.width} and coordinates: x = {self.x}, y = {self.y}"
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return {self.length, other.length} == {self.width, other.width}
        return False
               
    def __lt__(self, other):
        return self.area < other.area
    
    def __le__(self, other):
        return self.area <= other.area
    
    def __gt__(self, other):
        return self.area > other.area
    
    def __ge__(self, other):
        return self.area >= other.area
    
    def translate(self, move_x, move_y):
        validate_coordinates(move_x)
        validate_coordinates(move_y)
        self.x +=move_x
        self.y +=move_y

    def is_square(self):
        if self.length == self.width:
            return True
        else:
            return False
        