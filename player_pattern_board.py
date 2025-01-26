from player_board import PlayerBoard

class PlayerPatternBoard(PlayerBoard):
    """
    Player pattern board represents place where puzzles are stored at the end of the round. 
    At the end of the game player receives bonus points for collected patterns. 

    Attributes:
    - player_pattern_board (list): A 2D list representing the pattern board, initialized with a fixed
      size of 5 rows and 5 columns.
    
    Methods:
    - initialize_player_pattern_board(): Initializes the pattern board as a 2D list with 5 rows and
      5 columns, all filled with empty strings.

    """

    def __init__(self, player_number):
        super().__init__(player_number)
        self.player_pattern_board = self.initialize_player_pattern_board()

    def initialize_player_temporary_board():
        return [['','','','',''] for _ in range(5)]