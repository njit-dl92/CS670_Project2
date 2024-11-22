import unittest
from cluedo.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player")

    def test_initialization(self):
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.cards, [])
        self.assertIsNone(self.player.current_room)

    def test_receive_card(self):
        self.player.receive_card("Kitchen")
        self.assertIn("Kitchen", self.player.cards)
        self.assertEqual(len(self.player.cards), 1)

    def test_receive_multiple_cards(self):
        cards = ["Kitchen", "Knife", "Miss Scarlet"]
        for card in cards:
            self.player.receive_card(card)
        self.assertEqual(self.player.cards, cards)

if __name__ == "__main__":
    unittest.main()
