from numbers import Number

# refactoring
def validate_coordinates(coordinate):
    if not isinstance(coordinate, Number):
            raise TypeError("coordinate must be a number")
        
    if isinstance(coordinate, bool):
        raise TypeError("coordinate can not be boolean")
