

class Player:
    """
    Represents a player.

    Attributes:
    - number_of_players (int): Number of players that can play, varies from 2 to 4
    - points (int): The player's current points.
    - player_number(int): Number of the player.
    
    Methods:
    - set_number_of_players(number_of_players): Sets number of players at the class level.
    - validate_number_of_players(number_of_players): Checks if type of input is int and number of players if correct.
    """
    number_of_players = 2 
    
    def __init__(self, player_number, points=0):
        self.points = points
        self.player_number = player_number

    @classmethod
    def set_number_of_players(cls, number_of_players):
        cls.number_of_players = cls.validate_number_of_players(number_of_players)

    @staticmethod
    def validate_number_of_players(number_of_players):
        try:
            number_of_players = int(number_of_players)
        except ValueError:
            raise ValueError("The number of players must be an integer.")

        if not (2 <= number_of_players <= 4):
            raise ValueError("Number of players must be between 2 and 4.")
        
        return number_of_players