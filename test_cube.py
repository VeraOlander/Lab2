from pytest import raises
from cube import Cube

def test_valid_init():
    cube = Cube(side=5)
    assert cube.side == 5

def test_negative_parameter_fail():
    with raises(ValueError):
        Cube(side =-1)

def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Cube(side = "1")

def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Cube(side = True)

def test_zero_parameter_fail():
    with raises(ValueError):
        Cube(side = 0)

def test_surface_area_valid():
    c1 = Cube(2)
    assert c1.surface_area == 24

def test_volume_valid():
    c1 = Cube(2)
    assert c1.volume == 8


def test_eq_fail():
    c1 = Cube(5)
    c2 = Cube(3,2,2)
    assert c1 != c2

def test_eq_valid():
    c1 = Cube(3)
    c2 = Cube(3,2,2)
    assert c1 == c2