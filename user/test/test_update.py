import json
import user.update as update

update_success_body = json.loads(open('../mock/update.json').read())
update_failure_body = json.loads(open('../mock/update_fail.json').read())


def test_validate_data_pass():
    assert update.validate_data(update_success_body) is True


def test_validate_data_fail():
    assert update.validate_data(update_failure_body) is False


def test_create_success():
    response = update.update(update_success_body, '')
    assert response['statusCode'] == 200

def test_create_failure():
    response = update.update(update_failure_body, '')
    assert response['statusCode'] == 400
