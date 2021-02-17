import pytest

from myapp.triangles import triangle_type

all_triangles = [
    # check 90 for each angle
    (90, 60, 30, "right"),
    (10, 90, 80, "right"),
    (85, 5, 90, "right"),
    # big angles
    (0.01, 0.01, 179.98, "obtuse"),
    (1, 1, 178, "obtuse"),
    (91, 44, 45, "obtuse"),
    # just under 90
    (89, 89, 2, "acute"),
    (60, 60, 60, "acute"),
    # zeroes
    (0, 0, 0, "invalid"),
    # sum > 180
    (61, 60, 60, "invalid"),
    # negative numbers
    (90, 91, -1, "invalid"),
]


@pytest.mark.parametrize("a, b, c, expected", all_triangles)
def test_triangle_type(a, b, c, expected):
    assert triangle_type(a, b, c) == expected
