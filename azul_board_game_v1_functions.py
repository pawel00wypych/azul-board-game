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


def get_puzzles_from_leftovers(leftovers_from_suppliers, color):

    chosen_puzzles = [puzzle for puzzle in leftovers_from_suppliers if puzzle == color]
    leftovers_from_suppliers[:] = [puzzle for puzzle in leftovers_from_suppliers if puzzle != color]
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


def check_if_color_in_supp(supp, color, list_of_suppliers):
    if list_of_suppliers[supp]:
        if color in list_of_suppliers[supp]:
            return True
        else:
            print(f"There is no [{color}] in the supplier [{supp}]!\n")
    else:
        print(f"Supplier {supp} is empty!\n")
    return False

def check_if_color_in_lefftovers(color, leftovers_from_suppliers):
    if leftovers_from_suppliers:
        if color in leftovers_from_suppliers:
            return True
        else:
            print(f"There is no [{color}] in the leftovers [{leftovers_from_suppliers}]!\n")
    else:
        print(f"Leftovers {leftovers_from_suppliers} is empty!\n")
    return False


def choose_supplier_and_color(player_num, list_of_suppliers):
    while True:
        try:
            supp, color = input(f"Player [{player_num}] choose supplier [0-4] and color [R,B,G,Y,W] [separated by space]:").split()
        except ValueError as e:
            print("Wrong number of arguments!\n")
            continue

        try:
            supp = int(supp)
            if supp not in [0,1,2,3,4]:
                raise ValueError
        except ValueError as e:
            print(f"Supplier: {supp} has wrong value, provide only integer values in range 0-4!\n")
            continue

        try:
            color = color.upper()
            if not color.isalpha() or not color.isupper() or color not in ['R','B','G','Y','W']:
                raise ValueError
        except ValueError as e:
            print(f"Color: {color} has wrong value, provide only letters from list [R,B,G,Y,W]!\n")
            continue

        if check_if_color_in_supp(supp, color, list_of_suppliers):
            return supp, color
        
def choose_color(player_num, leftovers_from_suppliers):
    while True:
        try:
            color = input(f"Player [{player_num}] choose color [R,B,G,Y,W]:")
        except ValueError as e:
            print("Wrong number of arguments!\n")
            continue

        try:
            color = color.upper()
            if not color.isalpha() or not color.isupper() or color not in ['R','B','G','Y','W']:
                raise ValueError
        except ValueError as e:
            print(f"Color: {color} has wrong value, provide only letters from list [R,B,G,Y,W]!\n")
            continue

        if check_if_color_in_lefftovers(color, leftovers_from_suppliers):
            return color
        

def get_number_of_puzzles(temp_puzzles):
    
    while True:
        try:
            num_of_puzzles = int(input("Provide number of puzzles:"))
            if num_of_puzzles > len(temp_puzzles) or num_of_puzzles <= 0:
                raise ValueError
            break;
        except ValueError as e:
            print(f"Number of puzzles must be integer between [1 - {len(temp_puzzles)}!")
            continue
    
    return num_of_puzzles

def get_row_number(num_of_puzzles, color, player_temporary_boards):
    
    while True:
        try:
            row = int(input("Provide row number:"))
            if check_if_row_is_valid(num_of_puzzles, row, color, player_temporary_boards):
                return row
            continue
        except ValueError as e:
            print(f"Row number must be integer!")
            continue
    
    


#TODO correct this function
def check_if_row_is_valid(num_of_puzzles, row_number, color, player_temporary_boards):

    puzzles_in_row = 0

    for i in range(len(player_temporary_boards[row_number])):
        if player_temporary_boards[row_number][i] != color and player_temporary_boards[row_number][i] != ['']:
            print(f"Puzzles in a row must be of the same color [{player_temporary_boards[row_number][i]}]!")
            return False
        else:
            puzzles_in_row += 1

    if len(player_temporary_boards[row_number]) - puzzles_in_row < num_of_puzzles:
        print(f"There is not enough space for puzzles of a color {color} in the row {row_number}!") 
        return False
    
    return True