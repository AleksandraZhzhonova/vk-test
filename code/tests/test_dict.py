def test_dict_value_update():
    given_dict = {'name': 'Bob', 'age': 40}
    given_dict['age'] = 35
    expected_dict = {'name': 'Bob', 'age': 35}

    assert given_dict == expected_dict


def test_dict_by_key_delete():
    given_dict = {'name': 'Bob', 'age': 40}
    del given_dict['age']
    expected_dict = {'name': 'Bob'}

    assert given_dict == expected_dict
