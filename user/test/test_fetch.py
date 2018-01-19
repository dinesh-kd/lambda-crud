import json
import user.fetch as fetch

fetch_success_body = json.loads(open('../mock/fetch.json').read())
fetch_failure_body = json.loads(open('../mock/fetch_fail.json').read())


def test_validate_data_pass():
    assert fetch.validate_data(fetch_success_body) is True


def test_validate_data_fail():
    assert fetch.validate_data(fetch_failure_body) is False


def test_fetch_success():
    response = fetch.fetch(fetch_success_body, '')
    assert response['statusCode'] == 200

def test_fetch_failure():
    response = fetch.fetch(fetch_failure_body, '')
    assert response['statusCode'] == 400