from cluedo.player import Player
from cluedo.board import Board
from cluedo.cards import Cards

class CluedoGame:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.cards = Cards()
        self.solution = None

    def setup(self):
        print("Setting up the game...")
        self.cards.shuffle()
        self.solution = self.cards.pick_solution()
        self.board.setup_rooms()
        self.players = self.initialize_players()

    def initialize_players(self):
        num_players = int(input("Enter the number of players: "))
        return [Player(input(f"Enter name for Player {i + 1}: ")) for i in range(num_players)]

    def start(self):
        self.setup()
        print("Game started! Solve the mystery.")
