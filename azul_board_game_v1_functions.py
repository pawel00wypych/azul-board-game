#azul_board_game_v1_functions

import random



def initialize_player_points_lists(player_score_list, player_negative_points_list, number_of_players=2):
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


def initialize_puzzle_sack(puzzle_sack, puzzle_counter_keys_list, puzzle_counter):

    while len(puzzle_sack) != 100:
        random_puzzle_type = random.choice(puzzle_counter_keys_list)
        if puzzle_counter[random_puzzle_type] > 0:
            puzzle_counter[random_puzzle_type] = puzzle_counter[random_puzzle_type] - 1
            puzzle_sack.append(random_puzzle_type)



def initialize_suppliers(number_of_suppliers, puzzle_sack, list_of_suppliers): 
    for i in range(number_of_suppliers):
        supplier = random.sample(puzzle_sack,4) # TODO raise ValueError("Sample larger than population or is negative") when puzzle_sack < 4 elements
        list_of_suppliers.append(supplier)
        for item in supplier:
            puzzle_sack.remove(item)


def initialize_player_boards(number_of_players, player_pattern_boards, player_temporary_boards):
    #WRONG IMPLEMENTATION:
    # temporary_rows = [[''],['',''],['','',''],['','','',''],['','','','','']]                                  # Both wall_of_puzzles and temporary_rows are created once and 
    # wall_of_puzzles = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]   # then assigned to each player's board. This means all players' 
    # for i in range(number_of_players):                                                                         # boards in player_pattern_boards and 
    #     player_pattern_boards[i] = wall_of_puzzles                                                             # player_temporary_boards are referencing the same objects 
    #     player_temporary_boards[i] = temporary_rows                                                            # (wall_of_puzzles and temporary_rows) in memory.
                                                                                                                 # When you modify one player's board, you're actually 
                                                                                                                 # modifying the shared object, which is why changes appear across all players' boards.
    #Correctly implemented:
    for i in range(number_of_players):
        player_pattern_boards[i] = [['', '', '', '', ''] for _ in range(5)]
        player_temporary_boards[i] = [[''] * (j + 1) for j in range(5)]


def display_suppliers(list_of_suppliers):
    for i in range(len(list_of_suppliers)):
        print(f"Supplier [{i}]: {list_of_suppliers[i]}")

def display_suppliers_leftovers(leftovers_from_suppliers):
    print(f"leftovers: {leftovers_from_suppliers}")

def get_puzzles_from_supplier(supplier_number, color, list_of_suppliers, leftovers_from_suppliers):

    chosen_puzzles = []
    for supp in list_of_suppliers[supplier_number]:
        for puzzle in supp:
            if puzzle == color:
                chosen_puzzles.append(puzzle)
            else:
                leftovers_from_suppliers.append(puzzle)
    list_of_suppliers[supplier_number].clear()

    return chosen_puzzles

def display_player_board(player_number, player_temporary_boards, player_pattern_boards):
    
    print(f"|----------------------player {player_number} board---------------------------|\n")
    for i in range(5):
        print(f"{str(player_temporary_boards[player_number][i]).rjust(20)}  |  {player_pattern_boards[player_number][i]} ")
    print("\n|---------------------------------------------------------------|")
    print()


def insert_puzzle_to_temp_board(player_num, puzzles, row, amount_of_puzzles, player_temporary_boards):
    for i in range(amount_of_puzzles):
        player_temporary_boards[player_num][row][len(player_temporary_boards[player_num][row])-i-1] = puzzles.pop()

