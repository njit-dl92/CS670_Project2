import unittest
from cluedo.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertEqual(self.board.rooms, [])

    def test_setup_rooms(self):
        self.board.setup_rooms()
        expected_rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Library", "Lounge", "Hall", "Study"]
        self.assertEqual(self.board.rooms, expected_rooms)

if __name__ == "__main__":
    unittest.main()
