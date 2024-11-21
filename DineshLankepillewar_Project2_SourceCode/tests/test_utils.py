import unittest
from cluedo.utils import validate_input

class TestUtils(unittest.TestCase):
    def test_validate_input_valid(self):
        with unittest.mock.patch('builtins.input', side_effect=["Kitchen"]):
            result = validate_input("Choose a room: ", ["Kitchen", "Library"])
        self.assertEqual(result, "Kitchen")

    def test_validate_input_invalid(self):
        with unittest.mock.patch('builtins.input', side_effect=["Bathroom", "Kitchen"]):
            result = validate_input("Choose a room: ", ["Kitchen", "Library"])
        self.assertEqual(result, "Kitchen")

if __name__ == "__main__":
    unittest.main()
