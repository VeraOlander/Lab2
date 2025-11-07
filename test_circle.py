from pytest import raises
from circle import Circle
import math

def test_valid_init():
    circle = Circle(radius=5)
    assert circle.radius == 5

def test_negative_parameter_fail():
    with raises(ValueError):
        Circle(radius=-1)

def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Circle(x = "1")

def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Circle(radius = True)

def test_zero_parameter_fail():
    with raises(ValueError):
        Circle(radius= 0)

def test_area_valid():
    c1 = Circle(2)
    assert c1.area == 4 * math.pi


def test_eq_fail():
    c1 = Circle(5)
    c2 = Circle(3,2,2)
    assert c1 != c2

def test_eq_valid():
    c1 = Circle(3)
    c2 = Circle(3,2,2)
    assert c1 == c2