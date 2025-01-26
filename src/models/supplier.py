import random

class Supplier:
    """
    Represents a supplier in the game, managing the puzzles they hold, their leftovers, 
    and interactions with a shared puzzle sack.

    Class Attributes:
    - number_of_suppliers (int): Required number of suppliers, determined by the number of players.
    - list_of_suppliers (list): List holding all supplier instances.
    - leftovers_from_suppliers (list): A shared list containing puzzles leftover from
      suppliers after a player action.
    
    Instance Attributes:
    - puzzles (list): The puzzles currently assigned to this supplier. 
      
    Methods:
    - __repr__(self): 
        Returns a string representation of the supplier.
        
    - set_number_of_suppliers(cls, number_of_players): 
        Sets the number of suppliers based on the number of players.

    - display_suppliers(cls): 
        Displays suppliers if enough exist, otherwise prints a warning.

    - display_suppliers_leftovers(cls): 
        Displays all leftover puzzles from suppliers.

    - refill_suppliers(cls, puzzle_sack):
        Refills suppliers with puzzles from the `puzzle_sack`, adding up to 4 puzzles per supplier.
        Stops refilling when the puzzle sack is empty or contains insufficient puzzles.

    - get_puzzles_from_supplier(self, color):
        Retrieves puzzles of the specified `color` from the current supplier.
        Moves puzzles that do not match the specified `color` to `leftovers_from_suppliers`.
        Clears the supplier's puzzles after processing.

    - get_puzzles_from_leftovers(cls, color):
        Retrieves puzzles of the specified `color` from `leftovers_from_suppliers`.
        Removes the retrieved puzzles from the leftovers pool.
    """

    number_of_suppliers = 5
    list_of_suppliers = []
    leftovers_from_suppliers = []

    def __init__(self, puzzles):
        self.puzzles = puzzles
        Supplier.list_of_suppliers.append(self)

    
    def __repr__(self):
        return f"Supplier(puzzles={self.puzzles})"

    @classmethod
    def set_number_of_suppliers(cls, number_of_players):
        match number_of_players:
            case 2:
                cls.number_of_suppliers = 5
            case 3:
                cls.number_of_suppliers =  7
            case 4:
                cls.number_of_suppliers = 9

    @classmethod
    def display_suppliers(cls):
        if len(cls.list_of_suppliers) < cls.number_of_suppliers:
            print("Not enough suppliers to display.")
        else:
            for i in range(cls.number_of_suppliers):
                print(f"Supplier [{i}]: {cls.list_of_suppliers[i]}")

    @classmethod
    def display_suppliers_leftovers(cls):
        print(f"Leftovers from suppliers: {cls.leftovers_from_suppliers}")

    @classmethod
    def refill_suppliers(cls, puzzle_sack):
        sample_size = 4
        finish = False
        for i in range(cls.number_of_suppliers):
            if len(puzzle_sack) < 4:
                sample_size = len(puzzle_sack)
                finish = True
            if sample_size ==0:
                break

            supplier = random.sample(puzzle_sack, sample_size)
            cls.list_of_suppliers.append(supplier)
            for item in supplier:
                puzzle_sack.remove(item)
            if finish:
                break;
    
    @classmethod
    def get_puzzles_from_leftovers(cls, color):
        chosen_puzzles = [puzzle for puzzle in cls.leftovers_from_suppliers if puzzle == color]
        cls.leftovers_from_suppliers[:] = [puzzle for puzzle in cls.leftovers_from_suppliers if puzzle != color]
        return chosen_puzzles

    def get_puzzles_from_supplier(self, color):
        chosen_puzzles = []
        for puzzle in self.puzzles:
            if puzzle == color:
                chosen_puzzles.append(puzzle)
            else:
                Supplier.leftovers_from_suppliers.append(puzzle)
        self.puzzles.clear()

        return chosen_puzzles
    