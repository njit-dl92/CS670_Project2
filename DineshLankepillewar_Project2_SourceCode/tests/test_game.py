import unittest
from unittest.mock import patch
from cluedo.game import CluedoGame

class TestCluedoGame(unittest.TestCase):
    def setUp(self):
        self.game = CluedoGame()

    @patch("builtins.input", side_effect=["2", "Alice", "Bob"])  # Mock inputs: number of players and their names
    def test_setup(self, mock_input):
        self.game.setup()
        self.assertIsNotNone(self.game.solution)
        self.assertEqual(len(self.game.players), 2)  # Should create 2 players
        self.assertEqual(len(self.game.board.rooms), 6)

if __name__ == "__main__":
    unittest.main()
