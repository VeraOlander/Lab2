from shape import Shape
from validate_coordinates import validate_coordinates
from validate_parameters import validate_parameters

class Rectangle(Shape):
    def __init__(self, height, width, x=0, y=0):
        super().__init__(x, y)
        self.height=height
        self.width=width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        validate_parameters(height)        
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        validate_parameters(width)        
        self._width = width

    @property
    def area(self):
        return (self._height * self._width)
    
    @property
    def perimeter(self):
        return 2 * (self._height + self._width)

    def __repr__(self):
        return f"Rectangle with a length = {self.height}, width = {self.width} and coordinates: x = {self.x}, y = {self.y}"
    
    def __str__(self):
        return f"This is a rectangle with a length = {self.height}, width = {self.width} and coordinates: x = {self.x}, y = {self.y}"
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return {self.height, other.height} == {self.width, other.width}
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
        if self.height == self.width:
            return True
        else:
            return False
        