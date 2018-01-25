import os, sys
import json
import unittest

here = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(here)
sys.path.append(os.path.join(root))

import delete

delete_success_body = json.loads(open('../mock/delete.json').read())
delete_failure_body = json.loads(open('../mock/delete_fail.json').read())


class TestDeleteUser(unittest.TestCase):

    def test_validate_data_pass(self):
        self.assertTrue(delete.validate_data(delete_success_body))

    def test_validate_data_fail(self):
        self.assertFalse(delete.validate_data(delete_failure_body))

    def test_create_success(self):
        response = delete.delete(delete_success_body, '')
        self.assertEqual(response['statusCode'], 200)

    def test_create_failure(self):
        response = delete.delete(delete_failure_body, '')
        self.assertEqual(response['statusCode'], 400)
