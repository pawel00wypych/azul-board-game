from models.player_board import PlayerBoard 

class PlayerTemporaryBoard(PlayerBoard):
    """
    Represents place where player put his puzzles before pmoving them to pattern board at the end of the round.

    Attributtes:
    - player_temporary_board (list): A 2D list representing the temporary board, initialized with increasing row sizes (1 to 5).

    Methods:
    - initialize_player_temporary_board(): Initializes the temporary board as a 2D list with rows of increasing size.
    """

    def __init__(self, player_number):
        super().__init__(player_number)
        self.player_temporary_board = self.initialize_player_temporary_board()

    def initialize_player_temporary_board(self):
        return [[''] * (j + 1) for j in range(5)]
    
