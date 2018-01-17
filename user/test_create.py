import create

def test_validate_data_pass():
    param = {'name': 'Dinesh', 'username': 'dinesh-kd', 'email': 'dinesh.kd@diversey.com', 'password': 'Dinesh@123'}
    assert create.validate_data(param) == True

def test_validate_data_fail():
    param = {'name': 'Dinesh', 'username': 'dinesh-kd', 'email': 'dinesh.kd@diversey.com', 'password': ''}
    assert create.validate_data(param) == False

