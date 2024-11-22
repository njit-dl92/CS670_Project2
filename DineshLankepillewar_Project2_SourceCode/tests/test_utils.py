import unittest
from unittest.mock import patch
from cluedo.utils import validate_input

class TestUtils(unittest.TestCase):
    @patch("builtins.input", side_effect=["Invalid", "Valid Option"])
    def test_validate_input_valid(self, mock_input):
        result = validate_input("Enter your choice: ", ["Valid Option"])
        self.assertEqual(result, "Valid Option")

    @patch("builtins.input", side_effect=["Wrong", "Invalid", "Correct"])
    def test_validate_input_multiple_attempts(self, mock_input):
        result = validate_input("Enter a valid choice: ", ["Correct", "Option"])
        self.assertEqual(result, "Correct")

if __name__ == "__main__":
    unittest.main()
