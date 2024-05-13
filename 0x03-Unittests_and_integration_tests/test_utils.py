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
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected_result: Any) -> None:
        """
        the test_acess_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exceptions(self, nested_map: Mapping,
                                          path: Sequence) -> None:
        """
        the test_access_nested_map_exceptios function
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
