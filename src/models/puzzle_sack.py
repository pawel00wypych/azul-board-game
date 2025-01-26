import random

class PuzzleSack:
    """
    The Puzzle sack represents sack from which puzzles are given to the suppliers.

    Attributes:
    - puzzle_sack (list): A list representing the sack, containing the puzzles to be distributed.
    - puzzle_counter (dict): A dictionary tracking the available quantity of each puzzle type ('R', 'B', 'G', 'Y', 'W').
    - puzzle_counter_keys_list (list): A list of puzzle types for random selection.
    - _instance (PuzzleSack or None): A private class-level variable to ensure the singleton pattern.
    
    Methods:
    - __new__(cls, *args, **kwargs): Ensures only one instance of PuzzleSack is created (singleton).
    - __init__(self): Initializes the puzzle counter and keys list.
    - fill_puzzle_sack(cls): Fills the puzzle sack with 100 puzzles, randomly selecting from the available types.
    """
    puzzle_sack = []

    puzzle_counter = dict()
    
    puzzle_counter_keys_list = []

    _instance = None

    def __init__(self):
        PuzzleSack.puzzle_counter = {
                    'R': 20,
                    'B': 20,
                    'G': 20,
                    'Y': 20,
                    'W': 20}
        PuzzleSack.puzzle_counter_keys_list = list(PuzzleSack.puzzle_counter.keys())

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def fill_puzzle_sack(cls):
        while len(cls.puzzle_sack) != 100:
            random_puzzle_type = random.choice(cls.puzzle_counter_keys_list)
            if cls.puzzle_counter[random_puzzle_type] > 0:
                cls.puzzle_counter[random_puzzle_type] = cls.puzzle_counter[random_puzzle_type] - 1
                cls.puzzle_counter.append(random_puzzle_type)