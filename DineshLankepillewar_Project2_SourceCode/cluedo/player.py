class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def receive_card(self, card):
        self.cards.append(card)

    def make_guess(self):
        print(f"{self.name}, make your guess!")
        room = input("Room: ")
        weapon = input("Weapon: ")
        character = input("Character: ")
        return room, weapon, character
