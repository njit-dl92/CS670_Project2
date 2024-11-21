import unittest
from cluedo.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer")

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.cards, [])

    def test_receive_card(self):
        self.player.receive_card("Kitchen")
        self.assertIn("Kitchen", self.player.cards)

    def test_make_guess(self):
        with unittest.mock.patch('builtins.input', side_effect=["Library", "Knife", "Miss Scarlet"]):
            guess = self.player.make_guess()
        self.assertEqual(guess, ("Library", "Knife", "Miss Scarlet"))

if __name__ == "__main__":
    unittest.main()
