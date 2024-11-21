import unittest
from cluedo.game import CluedoGame

class TestCluedoGame(unittest.TestCase):
    def test_game_initialization(self):
        game = CluedoGame()
        self.assertIsNotNone(game)

if __name__ == "__main__":
    unittest.main()
