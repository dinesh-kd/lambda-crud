import fetch

def test_validate_data_pass():
    param = {'user_id': 1}
    assert fetch.validate_data(param) == True

def test_validate_data_fail():
    param = {'user_id': ''}
    assert fetch.validate_data(param) == False

