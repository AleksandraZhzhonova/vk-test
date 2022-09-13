import pytest


def test_integer_addition():
    a = 5
    b = 6
    actual_result = a + b
    expected_result = 11

    assert actual_result == expected_result


@pytest.mark.parametrize('a, b',
                         [(-3, -10),
                          (3, 10),
                          (30, 1),
                          (15, 2)])
def test_integer_multiplication(a, b):
    actual_result = a * b
    expected_result = 30

    assert actual_result == expected_result
