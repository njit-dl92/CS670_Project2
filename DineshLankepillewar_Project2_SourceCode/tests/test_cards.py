import unittest
from cluedo.cards import Cards

class TestCards(unittest.TestCase):
    def setUp(self):
        self.cards = Cards()

    def test_cards_initialization(self):
        self.assertEqual(len(self.cards.rooms), 3)
        self.assertEqual(len(self.cards.weapons), 3)
        self.assertEqual(len(self.cards.characters), 3)

    def test_shuffle_deck(self):
        original_deck = self.cards.deck.copy()
        self.cards.shuffle()
        self.assertNotEqual(original_deck, self.cards.deck)

    def test_pick_solution(self):
        solution = self.cards.pick_solution()
        self.assertIn(solution["room"], self.cards.rooms)
        self.assertIn(solution["weapon"], self.cards.weapons)
        self.assertIn(solution["character"], self.cards.characters)

if __name__ == "__main__":
    unittest.main()
