from shape import Shape
from numbers import Number
from validations import validate_coordinates
from validations import validate_parameters
import math
import matplotlib.patches as patches

class Circle(Shape):
    def __init__(self, radius: Number, x=0, y=0):
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

        

