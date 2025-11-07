from pytest import raises
from rectangle import Rectangle

def test_valid_init():
    rectangle = Rectangle(width=5, height = 7)
    assert rectangle.width == 5 and rectangle.height == 7

def test_negative_parameter_fail():
    with raises(ValueError):
        Rectangle(width=5, height=-1)

def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Rectangle(x = "1")

def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Rectangle(width = True)

def test_zero_parameter_fail():
    with raises(ValueError):
        Rectangle(width= 0, height=5)

def test_area_valid():
    r1 = Rectangle(2,4)
    assert r1.area == 8

def test_perimeter_valid():
    r1 = Rectangle(2,4)
    assert r1.perimeter == 12


def test_eq_fail():
    r1 = Rectangle(1,4)
    r2 = Rectangle(4,2)
    assert r1 != r2

def test_eq_valid():
    r1 = Rectangle(2,4)
    r2 = Rectangle(4,2)
    assert r1 == r2