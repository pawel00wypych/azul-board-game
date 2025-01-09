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
    leftovers_from_suppliers = list()


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

        for i in range(number_of_players):
                azul.display_suppliers(list_of_suppliers)
                azul.display_suppliers_leftovers(leftovers_from_suppliers)
                print()
                azul.display_player_board(i, player_temporary_boards, player_pattern_boards)
                supp, color = input(f"Player [{i}] choose supplier and color [separated by space]:").split() #TODO input verification
                temp_puzzles = azul.get_puzzles_from_supplier(int(supp), color, list_of_suppliers, leftovers_from_suppliers)

                print(f"Player [{i}] choose where to put puzzles")
                num_of_puzzles = int(input("Provide number of puzzles:"))
                row_num = int(input("Provide row number:"))
                azul.insert_puzzle_to_temp_board(i, temp_puzzles, row_num, num_of_puzzles, player_temporary_boards)

                print(f"Player [{i}] puzzles: [{temp_puzzles}]")

        print()
        print(f"player_temporary_boards: {player_temporary_boards}")
        print()
        print(f"player_temporary_boards: {player_pattern_boards}")
        print()

        input()
        round += 1

