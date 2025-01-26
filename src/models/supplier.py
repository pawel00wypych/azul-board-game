
class Supplier:
    """
    The Supplier class manages suppliers, tracks them in a shared list, and determines the required number 
    of suppliers based on the number of players.

    Attributes:
    - number_of_suppliers (int): Required number of suppliers (default: 5).
    - list_of_suppliers (list): List holding all supplier instances.
    
    Methods:
    - __repr__(self): Returns a string representation of the supplier.
    - set_number_of_suppliers(cls, number_of_players): Sets the number of suppliers based on the number of players.
    - display_suppliers(cls): Displays suppliers if enough exist, otherwise prints a warning.
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
