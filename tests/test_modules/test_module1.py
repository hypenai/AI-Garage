# Tests for module1.py

import unittest
from src.modules.module1 import function_in_module1

class TestModule1(unittest.TestCase):
    def test_function_in_module1(self):
        self.assertEqual(function_in_module1(), "This is a function from Module 1")
