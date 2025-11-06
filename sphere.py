from circle import Circle
from validations import validate_coordinates
from validations import validate_parameters
import math



class Sphere(Circle):
    def __init__(self, radius: float | int, x: float | int = 0, y: float | int = 0):
        super().__init__(radius, x, y)
        
    @property
    def volume(self):
        return (4/3) * math.pi * (self._radius ** 3)
    
    @property
    def circumference(self):
        return 2 * math.pi * self._radius
    
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