import pytest
import myapp.triangles

all_triangles = [
    (90, 60, 30, "right"),
    (100, 40, 40, "obtuse"),
    (60, 60, 60, "acute"),
    (0, 0, 0, "invalid")
]

@pytest.mark.parametrize('a, b, c, expected', all_triangles)
def test_triangle_type(a, b, c, expected):
    assert myapp.triangles.triangle_type(a, b, c) == expected
