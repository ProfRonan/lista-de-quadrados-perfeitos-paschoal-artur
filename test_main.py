"""Test file for testing the main.py file"""

import unittest
from unittest.mock import patch
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="1")
    def test_squares_1(self, _mock_input):
        """Testa se o programa imprime 1 quando a entrada é 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("1",captured_output.getvalue().strip())

    @patch("builtins.input", return_value="3")
    def test_squares_3(self, _mock_input):
        """Testa se o programa imprime 1, 4 e 9 quando a entrada é 3"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("1\n4\n9",captured_output.getvalue().strip())

    @patch("builtins.input", return_value="6")
    def test_squares_6(self, _mock_input):
        """Testa se o programa imprime 1, 4, 9, 16, 25 e 36 quando a entrada é 6"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("1\n4\n9\n16\n25\n36",captured_output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
