import user.fetch

def test_validate_data_pass():
    param = {'user_id': 1}
    assert user.fetch.validate_data(param) == True

def test_validate_data_fail():
    param = {'user_id': ''}
    assert user.fetch.validate_data(param) == False

