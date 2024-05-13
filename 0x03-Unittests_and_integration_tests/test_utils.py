#!/usr/bin/env python3
"""
parameterize a test unit
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    the TestAcessNestedMap class
    """
    @parameterizes.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        the test_acess_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__': 
    unittest.main()
