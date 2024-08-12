# Tests for module2.py

import unittest
from src.modules.module2 import function_in_module2

class TestModule2(unittest.TestCase):
    def test_function_in_module2(self):
        self.assertEqual(function_in_module2(), "This is a function from Module 2")
