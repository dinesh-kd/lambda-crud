import os, sys
import json
import unittest

here = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(here)
sys.path.append(os.path.join(root))

import create


create_success_body = json.loads(open('../mock/create.json').read())
create_failure_body = json.loads(open('../mock/create_fail.json').read())


class TestDeleteUser(unittest.TestCase):

    def test_validate_data_pass(self):
        self.assertTrue(create.validate_data(create_success_body))

    def test_validate_data_fail(self):
        self.assertFalse(create.validate_data(create_failure_body))

    def test_create_success(self):
        response = create.create(create_success_body, '')
        self.assertEqual(response['statusCode'], 200)

    def test_create_failure(self):
        response = create.create(create_failure_body, '')
        self.assertEqual(response['statusCode'], 400)


if __name__ == '__main__':
    unittest.main()
