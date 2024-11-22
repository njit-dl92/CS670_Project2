import unittest
from cluedo.cards import Cards

class TestCards(unittest.TestCase):
    def setUp(self):
        self.cards = Cards()

    def test_initialization(self):
        self.assertEqual(self.cards.rooms, ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Library", "Lounge"])
        self.assertEqual(self.cards.weapons, ["Knife", "Candlestick", "Revolver", "Rope", "Lead Pipe", "Wrench"])
        self.assertEqual(self.cards.characters, ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mr. Green", "Mrs. Peacock", "Mrs. White"])
        self.assertEqual(
            self.cards.deck,
            self.cards.rooms + self.cards.weapons + self.cards.characters
        )

    def test_shuffle(self):
        original_deck = self.cards.deck[:]
        self.cards.shuffle()
        self.assertNotEqual(self.cards.deck, original_deck)
        self.assertEqual(sorted(self.cards.deck), sorted(original_deck))

    def test_pick_solution(self):
        solution = self.cards.pick_solution()
        self.assertIn(solution["room"], self.cards.rooms)
        self.assertIn(solution["weapon"], self.cards.weapons)
        self.assertIn(solution["character"], self.cards.characters)

if __name__ == "__main__":
    unittest.main()
