import unittest
from cluedo.game import CluedoGame
from cluedo.player import Player

class TestCluedoGame(unittest.TestCase):
    def setUp(self):
        self.game = CluedoGame()
        self.game.setup()
    

