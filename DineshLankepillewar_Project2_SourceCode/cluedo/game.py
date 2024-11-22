from cluedo.player import Player  # Import Player class from the player module

class CluedoGame:
    def __init__(self):
        self.players = []
        self.rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Study", "Hall", "Library"]
        self.suspects = ["Miss Scarlet", "Colonel Mustard", "Professor Plum", "Mr. Green", "Mrs. Peacock", "Mrs. White"]
        self.weapons = ["Knife", "Candlestick", "Revolver", "Rope", "Lead Pipe", "Wrench"]
        self.solution = None
        self.current_turn = 0  # Track whose turn it is

    def setup(self):
        print("Setting up the game...")
        self.solution = (
            self.suspects[0],  # Randomly selecting the first suspect for simplicity
            self.weapons[0],  # Randomly selecting the first weapon for simplicity
            self.rooms[0]     # Randomly selecting the first room for simplicity
        )
        print("Rooms setup complete!")

        # Get number of players
        num_players = int(input("Enter the number of players (2-6): "))
        self.players = self.initialize_players(num_players)

    def initialize_players(self, num_players):
        return [Player(input(f"Enter name for Player {i + 1}: ")) for i in range(num_players)]

    def distribute_cards(self):
        print("Distributing cards to players...")
        # Here, you'd distribute cards (excluding solution) to each player
        print("Cards distributed successfully.")

    def start(self):
        print("Game started! Solve the mystery.")

        # Main game loop
        while True:
            current_player = self.players[self.current_turn % len(self.players)]
            print(f"\n{current_player.name}'s turn:")

            # Displaying action choices
            print("1. Move to a new room")
            print("2. Make a suggestion")
            print("3. Make an accusation")
            print("4. Quit the game")

            choice = input("Choose an action: ")

            if choice == "1":
                self.move_to_room(current_player)
            elif choice == "2":
                self.make_suggestion(current_player)
            elif choice == "3":
                if self.make_accusation(current_player):
                    print(f"{current_player.name} wins! Game over.")
                    break
                else:
                    print(f"{current_player.name} made an incorrect accusation!")
            elif choice == "4":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            self.current_turn += 1  # Move to the next player's turn

    def move_to_room(self, player):
        print("Available rooms:", ", ".join(self.rooms))
        room = input("Enter the room you want to move to: ")
        if room in self.rooms:
            player.current_room = room
            print(f"{player.name} moved to the {room}.")
        else:
            print("Invalid room. Try again.")

    def make_suggestion(self, player):
        suspect = input("Enter a suspect: ")
        weapon = input("Enter a weapon: ")
        print(f"{player.name} suggests it was {suspect} with the {weapon} in the {player.current_room}.")
        # Logic to handle suggestions can be added here.

    def make_accusation(self, player):
        suspect = input("Enter a suspect: ")
        weapon = input("Enter a weapon: ")
        room = input("Enter a room: ")

        if (suspect, weapon, room) == self.solution:
            return True
        return False
