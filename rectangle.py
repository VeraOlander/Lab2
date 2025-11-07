from shape import Shape
from numbers import Number
from validations import validate_coordinates
from validations import validate_parameters
import matplotlib.patches as patches

class Rectangle(Shape):
    """
    A class to create a Rectangle object
     Attributes:     
     - width (Number): larger than 0
     - height (Number): larger than 0
     - x: x-coordinate, inherited from parent class Shape, default value 0
     - y: y-coordinate, inherited from parent class Shape, default value 0
     - area: calculated from width and height
     - perimeter: calculated from width and height
     ...
    Methods:
    - __eq__: == operator overload to compare rectangle instances by their width/height
    - __lt__: < operator overload to compare rectangle instances by their areas
    - __le__: <= operator overload to compare rectangle instances by their areas
    - __gt__: > operator overload to compare rectangle instances by their areas
    - __ge__: >= operator overload to compare rectangle instances by their areas
    - translate(): moves the object by changing x and y coordinates
    - is_square(): checks whether a Rectangle instance is square, namely that width and height are equal
    - draw_rectangle(): creates a matplotlib rectangle patch out of a Rectangle class instance with the given parameters. As matplotlib rectangle patches are plotted starting
    from Lower left point, coordinates are adjusted by subtracting half width from x and half heiht from y to keep the center of Rectangle class instance

    Example usage:
    >>> rectangle1=Rectangle(2,3,0,0)
    >>> rectangle1.area
    >>> rectangle1.is_square()
    >>> rectangle1.translate(4,5)
    """
    def __init__(self, width: Number, height: Number, x: Number = 0, y: Number = 0):
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
        return f"Rectangle (height = {self.height}, width = {self.width}, x = {self.x}, y = {self.y})"
    
    def __str__(self):
        return f"This is a rectangle with a height = {self.height}, width = {self.width} and center coordinates: x = {self.x}, y = {self.y}"
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return {self.height, other.height} == {self.width, other.width}
        return False
               
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        return False
    
    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area <= other.area
        return False
    
    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area > other.area
        return False
    
    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area >= other.area
        return False
    
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
        rectangle_patch = patches.Rectangle((self.x-self.width/2, self.y-self.height/2), self.width, self.height, edgecolor='red', facecolor='none', linewidth=2)
        ax.plot(self.x, self.y, marker='o', color='red', markersize=2)
        ax.set_aspect('equal')
        ax.add_patch(rectangle_patch)
        return ax
        
