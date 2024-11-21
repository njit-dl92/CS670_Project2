class Board:
    def __init__(self):
        self.rooms = []

    def setup_rooms(self):
        self.rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Library", "Lounge"]
        print("Rooms setup complete!")
