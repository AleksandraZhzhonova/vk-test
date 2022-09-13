import pytest


def test_set_value_add():
    given_set = set('abcde')
    given_set.add('r')
    expected_set = set('abcder')

    assert given_set == expected_set


def test_add_wrong_object_type_raises():
    given_set = set('abcde')
    with pytest.raises(TypeError) as excinfo:
        given_set.add([1, 2, 3])
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "unhashable type: 'list'"
