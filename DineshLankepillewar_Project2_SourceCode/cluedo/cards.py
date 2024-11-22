import random

class Cards:
    def __init__(self):
        self.rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Library", "Lounge"]
        self.weapons = ["Knife", "Candlestick", "Revolver", "Rope", "Lead Pipe", "Wrench"]
        self.characters = ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mr. Green", "Mrs. Peacock", "Mrs. White"]
        self.deck = self.rooms + self.weapons + self.characters

    def shuffle(self):
        random.shuffle(self.deck)

    def pick_solution(self):
        return {
            "room": random.choice(self.rooms),
            "weapon": random.choice(self.weapons),
            "character": random.choice(self.characters)
        }
