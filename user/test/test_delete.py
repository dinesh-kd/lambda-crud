import json
import user.delete as delete

delete_success_body = json.loads(open('../mock/delete.json').read())
delete_failure_body = json.loads(open('../mock/delete_fail.json').read())


def test_validate_data_pass():
    assert delete.validate_data(delete_success_body) is True


def test_validate_data_fail():
    assert delete.validate_data(delete_failure_body) is False


def test_create_success():
    response = delete.delete(delete_success_body, '')
    assert response['statusCode'] == 200

def test_create_failure():
    response = delete.delete(delete_failure_body, '')
    assert response['statusCode'] == 400
