# Azul board game v.1
import azul_board_game_v1_functions as azul

if __name__ == '__main__':


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

    number_of_suppliers = azul.set_number_of_suppliers(number_of_players)

    puzzle_counter = {'R': 20,
                    'B': 20,
                    'G': 20,
                    'Y': 20,
                    'W': 20}

    puzzle_sack = list()
    puzzle_counter_keys_list = list(puzzle_counter.keys())
    puzzle_box = list()
    list_of_suppliers = list()
    leftovers_from_suppliers = []

    azul.initialize_puzzle_sack(puzzle_sack, puzzle_counter_keys_list, puzzle_counter)
    azul.initialize_suppliers(number_of_suppliers, puzzle_sack, list_of_suppliers)
    azul.initialize_player_boards(number_of_players, player_pattern_boards, player_temporary_boards)

    print("|---------------------------------------------------------------|")
    print("|                                                               |")
    print("|                         Game begins!                          |")
    print("|                                                               |")
    print("|---------------------------------------------------------------|\n\n")
    round = 0
    while True:

        print("|---------------------------------------------------------------|")
        print(f"|                           {round:02} round.                           |")
        print("|---------------------------------------------------------------|")
        print("|---------------------------------------------------------------|")
        print("|                       Choosing puzzles                        |")
        print("|---------------------------------------------------------------|\n\n")

        for player_num in range(number_of_players):
                azul.display_suppliers(list_of_suppliers)
                azul.display_suppliers_leftovers(leftovers_from_suppliers)
                print()
                azul.display_player_board(player_num, player_temporary_boards, player_pattern_boards)
                

                while True:
                    puzzles_from = 'S'
                    if leftovers_from_suppliers:
                        try:
                            puzzles_from = input("Do you want to get puzzles from suppliers[s] or from leftovers[l]:").upper()
                            if puzzles_from != 'S' and puzzles_from != 'L':
                                raise ValueError
                        except ValueError as e:
                            print("Provide only letters [s] or [l]!")
                            continue
                    
                    if puzzles_from == 'S':
                        supp, color = azul.choose_supplier_and_color(player_num, list_of_suppliers)
                        temp_puzzles = azul.get_puzzles_from_supplier(int(supp), color, list_of_suppliers, leftovers_from_suppliers)
                    else:
                        color = azul.choose_color(player_num, leftovers_from_suppliers)
                        temp_puzzles = azul.get_puzzles_from_leftovers(leftovers_from_suppliers, color)

                    print(f"Player [{player_num}] choose where to put puzzles")
                    num_of_puzzles = azul.get_number_of_puzzles(temp_puzzles)
                    row_num = azul.get_row_number(num_of_puzzles, color, player_temporary_boards)
                    azul.insert_puzzle_to_temp_board(player_num, temp_puzzles, row_num, num_of_puzzles, player_temporary_boards)
                    break

                print(f"Player [{player_num}] puzzles: [{temp_puzzles}]\n\n")

        input("Click to continue......")
        round += 1

