import json
import user.create as create

create_success_body = json.loads(open('../mock/create.json').read())
create_failure_body = json.loads(open('../mock/create_fail.json').read())


def test_validate_data_pass():
    assert create.validate_data(create_success_body) is True


def test_validate_data_fail():
    assert create.validate_data(create_failure_body) is False


def test_create_success():
    response = create.create(create_success_body, '')
    assert response['statusCode'] == 200

def test_create_failure():
    response = create.create(create_failure_body, '')
    assert response['statusCode'] == 400
