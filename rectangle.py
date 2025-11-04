from shape import Shape
from validate_coordinates import validate_coordinates
from validate_parameters import validate_parameters
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Rectangle(Shape):
    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width=width
        self.height=height
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        validate_parameters(width)        
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        validate_parameters(height)        
        self._height = height
    
    @property
    def area(self):
        return (self._height * self._width)
    
    @property
    def perimeter(self):
        return 2 * (self._height + self._width)

    def __repr__(self):
        return f"Rectangle with a height = {self.height}, width = {self.width} and lower left corner coordinates: x = {self.x}, y = {self.y}"
    
    def __str__(self):
        return f"This is a rectangle with a height = {self.height}, width = {self.width} and lower left corner coordinates: x = {self.x}, y = {self.y}"
    
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
        
    def draw_rectangle(self,ax):
        rectangle_patch = patches.Rectangle((self.x, self.y), self.width, self.height, edgecolor='red', facecolor='none', linewidth=2)
        ax.set_aspect('equal')
        ax.add_patch(rectangle_patch)
        return ax
        
