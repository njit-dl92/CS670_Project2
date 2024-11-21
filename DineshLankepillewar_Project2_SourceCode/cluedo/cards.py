import random

class Cards:
    def __init__(self):
        self.rooms = ["Kitchen", "Ballroom", "Conservatory"]
        self.weapons = ["Knife", "Candlestick", "Revolver"]
        self.characters = ["Miss Scarlet", "Colonel Mustard", "Mrs. Peacock"]
        self.deck = self.rooms + self.weapons + self.characters

    def shuffle(self):
        random.shuffle(self.deck)

    def pick_solution(self):
        return {
            "room": random.choice(self.rooms),
            "weapon": random.choice(self.weapons),
            "character": random.choice(self.characters)
        }
