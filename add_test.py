from add import add
import pytest


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 6, 11),
    (12, 6, 18),
    (5, 6, 11),
    (0, 1, 1),
    (5, 0, 5),
])
def test_add(a, b, expected):
    got = add(a, b)
    assert got == expected, f"expected = {expected}, got = {got}"
