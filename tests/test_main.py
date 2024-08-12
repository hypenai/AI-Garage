# Test for the main.py script

import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), None)
