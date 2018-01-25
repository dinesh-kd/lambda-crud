import os, sys
import json
import unittest

here = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(here)
sys.path.append(os.path.join(root))

import update

update_success_body = json.loads(open('../mock/update.json').read())
update_failure_body = json.loads(open('../mock/update_fail.json').read())


class TestDeleteUser(unittest.TestCase):
    def test_validate_data_pass(self):
        self.assertTrue(update.validate_data(update_success_body))

    def test_validate_data_fail(self):
        self.assertFalse(update.validate_data(update_failure_body))

    def test_create_success(self):
        response = update.update(update_success_body, '')
        self.assertEqual(response['statusCode'], 200)

    def test_create_failure(self):
        response = update.update(update_failure_body, '')
        self.assertEqual(response['statusCode'], 400)
