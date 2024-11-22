class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None  # To track where the player is currently
        self.cards = []  # To store cards the player holds

    def receive_card(self, card):
        self.cards.append(card)

    def make_guess(self):
        print(f"{self.name}, make your guess!")
        room = input("Room: ")
        weapon = input("Weapon: ")
        character = input("Character: ")
        return room, weapon, character
