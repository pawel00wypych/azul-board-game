from models.player import Player


class PlayerBoard:
    """
    Represents player board, place where player put his puzzles in order to collect points.
    
    Attributtes:
    - number_of_players (int): Number of players that can play, varies from 2 to 4

    Methods:
    """

    def __init__(self, player_number):
        self.player_number = player_number
