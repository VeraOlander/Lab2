from pytest import raises
from sphere import Sphere
import math

def test_valid_init():
    sphere = Sphere(radius=5)
    assert sphere.radius == 5

def test_negative_parameter_fail():
    with raises(ValueError):
        Sphere(radius=-1)

def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Sphere(radius = "1")

def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Sphere(radius = True)

def test_zero_parameter_fail():
    with raises(ValueError):
        Sphere(radius = 0)

def test_surface_area_valid():
    s1 = Sphere(2)
    assert s1.surface_area == 16 * math.pi

def test_volume_valid():
    s1 = Sphere(2)
    assert s1.volume == (4/3) * math.pi * 8


def test_eq_fail():
    s1 = Sphere(5)
    s2 = Sphere(3,2,2)
    assert s1 != s2

def test_eq_valid():
    s1 = Sphere(3)
    s2 = Sphere(3,2,2)
    assert s1 == s2