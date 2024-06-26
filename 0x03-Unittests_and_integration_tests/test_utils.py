#!/usr/bin/env python3
"""
parameterize a test unit
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import (
        Mapping,
        Sequence,
        Any,
)
from unittest.mock import patch
import json


class TestAccessNestedMap(unittest.TestCase):
    """
    the TestAcessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ['a'], 1),
        ({"a": {"b": 2}}, ['a'], {"b": 2}),
        ({"a": {"b": 2}}, ['a', 'b'], 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected_result: Any) -> None:
        """
        the test_acess_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ['a']),
        ({"a": 1}, ['a', 'b'])
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        the test_access_nested_map_exceptios function
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    the TestGetJson class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        the test_get_json function
        """
        with patch('utils.requests.get') as mock_request_get:
            mock_request_get.return_value.json.return_value = test_payload
            resp = get_json(test_url)
            mock_request_get.assert_called_with(test_url)
            self.assertEqual(resp, test_payload)


class TestMemoize(unittest.TestCase):
    """
    the TestMemoize class
    """
    def test_memoize(self):
        """
        the test_memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
