from numbers import Number

# refactoring

def validate_coordinates(coordinate):
    if not isinstance(coordinate, Number):
            raise TypeError("coordinate must be a number")
        
    if isinstance(coordinate, bool):
        raise TypeError("coordinate can not be boolean")
    


def validate_parameters(parameter):
    if not isinstance(parameter, Number):
            raise TypeError("This parameter must be a number")
        
    if isinstance(parameter, bool):
        raise TypeError("This parameter can not be boolean")
    
    if parameter <= 0:
        raise ValueError("This parameter can not be negative or equal to zero")
    

