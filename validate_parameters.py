from numbers import Number

def validate_parameters(parameter):
    if not isinstance(parameter, Number):
            raise TypeError("This parameter must be a number")
        
    if isinstance(parameter, bool):
        raise TypeError("This parameter can not be boolean")
    
    if parameter <= 0:
        raise ValueError("This parameter can not be negative or equal to zero")
