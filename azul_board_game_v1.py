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
print()


puzzle_counter = {'R': 20,
                  'B': 20,
                  'G': 20,
                  'Y': 20,
                  'W': 20}

puzzle_sack = list()
puzzle_counter_keys_list = list(puzzle_counter.keys())


def initialize_puzzle_sack():

    while len(puzzle_sack) != 100:
        random_puzzle_type = random.choice(puzzle_counter_keys_list)
        if puzzle_counter[random_puzzle_type] > 0:
            puzzle_counter[random_puzzle_type] = puzzle_counter[random_puzzle_type] - 1
            puzzle_sack.append(random_puzzle_type)

initialize_puzzle_sack()

print()
print(puzzle_counter)
print()
print(puzzle_sack)


list_of_suppliers = list()
leftovers_from_suppliers = list()

def initialize_suppliers():
    for i in range(5):
        list_of_suppliers.append(random.sample(puzzle_sack,4))


initialize_suppliers()
print()
print(list_of_suppliers)

