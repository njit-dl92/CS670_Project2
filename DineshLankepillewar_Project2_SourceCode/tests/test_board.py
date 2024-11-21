import unittest
from cluedo.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_initialization(self):
        self.assertEqual(self.board.rooms, [])

    def test_setup_rooms(self):
        self.board.setup_rooms()
        self.assertEqual(len(self.board.rooms), 6)
        self.assertIn("Kitchen", self.board.rooms)

if __name__ == "__main__":
    unittest.main()
