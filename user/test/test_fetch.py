import os, sys
import json
import unittest

here = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(here)
sys.path.append(os.path.join(root))

import fetch

fetch_success_body = json.loads(open('../mock/fetch.json').read())
fetch_failure_body = json.loads(open('../mock/fetch_fail.json').read())


class TestDeleteUser(unittest.TestCase):
    def test_validate_data_pass(self):
        self.assertTrue(fetch.validate_data(fetch_success_body))

    def test_validate_data_fail(self):
        self.assertFalse(fetch.validate_data(fetch_failure_body))

    def test_fetch_success(self):
        response = fetch.fetch(fetch_success_body, '')
        self.assertEqual(response['statusCode'], 200)

    def test_fetch_failure(self):
        response = fetch.fetch(fetch_failure_body, '')
        self.assertEqual(response['statusCode'], 400)
