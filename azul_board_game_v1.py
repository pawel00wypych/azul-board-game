# Azul board game v.1

import random

print("\n|------------------Welcome to Azul board game!------------------|")
print()
print("  In the game Azul, together with your friends, you take on the \n"
      "  roles of artists who, at the king's request, create beautiful, \n"
      "  intricate mosaics on the walls of the palace in Évora. Each of \n"
      "  you will create your own piece of the puzzle using elements \n"
      "  available from shared suppliers.\n")
print("|---------------------------------------------------------------|")
print("\n\n\n")

number_of_players = 0
number_of_suppliers = 5


while number_of_players != 2 and number_of_players != 3 and number_of_players != 4:
    try:
        number_of_players = int(input("Please provide number of players [2, 3, 4]: \n"))
    except ValueError as e:
        print("Provide only integer values!")


player_score_list = list()
player_negative_points_list = list()
player_pattern_boards = dict()
player_temporary_boards = dict()

for i in range(number_of_players):
    player_score_list.append(0)
    player_negative_points_list.append(0)


def set_number_of_suppliers(number_of_players):
    match number_of_players:
        case 2:
            return 5
        case 3:
            return 7
        case 4:
            return 9


number_of_suppliers = set_number_of_suppliers(number_of_players)

puzzle_counter = {'R': 20,
                  'B': 20,
                  'G': 20,
                  'Y': 20,
                  'W': 20}

puzzle_sack = list()
puzzle_counter_keys_list = list(puzzle_counter.keys())
puzzle_box = list()
list_of_suppliers = list()
leftovers_from_suppliers = list()

def initialize_puzzle_sack():

    while len(puzzle_sack) != 100:
        random_puzzle_type = random.choice(puzzle_counter_keys_list)
        if puzzle_counter[random_puzzle_type] > 0:
            puzzle_counter[random_puzzle_type] = puzzle_counter[random_puzzle_type] - 1
            puzzle_sack.append(random_puzzle_type)

initialize_puzzle_sack()


def initialize_suppliers(): 
    for i in range(number_of_suppliers):
        supplier = random.sample(puzzle_sack,4) # TODO raise ValueError("Sample larger than population or is negative") when puzzle_sack < 4 elements
        list_of_suppliers.append(supplier)
        for item in supplier:
            puzzle_sack.remove(item)

initialize_suppliers()


def initialize_player_boards(number_of_players):
    temporary_rows = [[''],['',''],['','',''],['','','',''],['','','','','']]
    wall_of_puzzles = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
    for i in range(number_of_players):
        player_pattern_boards[i] = wall_of_puzzles
        player_temporary_boards[i] = temporary_rows

def display_suppliers():
    for i in range(len(list_of_suppliers)):
        print(f"Supplier [{i}]: {list_of_suppliers[i]}")

def display_suppliers_leftovers():
    print(f"leftovers: {leftovers_from_suppliers}")

def get_puzzles_from_supplier(supplier_number, color):

    chosen_puzzles = []
    for supp in list_of_suppliers[supplier_number]:
        for puzzle in supp:
            if puzzle == color:
                chosen_puzzles.append(puzzle)
            else:
                leftovers_from_suppliers.append(puzzle)
    list_of_suppliers[supplier_number].clear()

    return chosen_puzzles

def display_player_board(player_number):
    
    print(f"|----------------------player {player_number} board---------------------------|\n")
    for i in range(5):
        print(f"{str(player_temporary_boards[player_number][i]).rjust(20)}  |  {player_pattern_boards[player_number][i]} ")
    print("\n|---------------------------------------------------------------|")
    print()

initialize_player_boards(number_of_players)

print()
print(puzzle_counter)
print()
print(puzzle_sack)


print("|---------------------------------------------------------------|")
print("|                         Game begins!                          |")
print("|---------------------------------------------------------------|\n\n")
round = 0
while True:

    print("|---------------------------------------------------------------|")
    print(f"|                           {round:02} round.                           |")
    print("|---------------------------------------------------------------|\n\n")

    print("|---------------------------------------------------------------|")
    print("|                       Choosing puzzles                        |")
    print("|---------------------------------------------------------------|\n\n")

    for i in range(number_of_players):
            display_suppliers()
            display_suppliers_leftovers()
            print()
            display_player_board(i)
            supp, color = input(f"                   Player [{i+1}] choose supplier and color [separated by space]:             ").split() #TODO input verification
            temp = get_puzzles_from_supplier(int(supp), color)
            print(f"Player [{i}] puzzles: [{temp}]")

    input()





    round += 1



    

initialize_suppliers()
print()
print(f"list_of_suppliers: {list_of_suppliers}")
print()
print(f"puzzle sack: {puzzle_sack}")
print()
initialize_suppliers()
print()
print(f"list_of_suppliers: {list_of_suppliers}")
print()
print(f"puzzle sack: {puzzle_sack}")
print()
initialize_suppliers()
print()
print(f"list_of_suppliers: {list_of_suppliers}")
print()
print(f"puzzle sack: {puzzle_sack}")
print()
