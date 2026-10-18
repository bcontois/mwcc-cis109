#Brian J Contois
#17 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#tic_tac_toe.py

import random

random_number = (random.randint(1, 20)) % 2

winner = False
draw = False

players = ["X","O"]

board = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

for row_key, row_value in enumerate(board, start = 0):
    #print(f"Row: {row_key}; Value: {row_value}\n", end="")
    for col_key, col_value in enumerate(row_value, start = 0):
        #print(f"Column: {col_key}; Value: {col_value}\n", end="")
        if row_key == 0:
            print(f" {col_value} ", end="")
            if col_key == 2:
                print(f"\n--|---|--\n", end="")
        elif row_key == 1:
            print(f" {col_value} ", end="")
            if col_key == 2:
                print(f"\n--|---|--\n", end="")
        elif row_key == 2:
            print(f" {col_value} ", end="")

while winner == False or draw == False:

    row_choice = input("\n\nSelect a Row(1-3): ")

    if len(row_choice) != 1 or not row_choice.isdigit():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\ninvalid input. please enter a valid row.\n\n\n\n\n\n")
        input("\nplease hit [enter] to continue...")
        continue

    if int(row_choice) < 1 or int(row_choice) > 3:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\ninvalid input. please enter a valid row.\n\n\n\n\n\n")
        input("\nplease hit [enter] to continue...")
        continue

    col_choice = input("\nSelect a Column(1-3): ")

    if len(col_choice) != 1 or not col_choice.isdigit():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\ninvalid input. please enter a valid column.\n\n\n\n\n\n")
        input("\nplease hit [enter] to continue...")
        continue

    if int(col_choice) < 1 or int(col_choice) > 3:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\ninvalid input. please enter a valid column.\n\n\n\n\n\n")
        input("\nplease hit [enter] to continue...")
        continue
   
    for row_key, row_value in enumerate(board, start = 0):
        #print(f"Row: {row_key}; Value: {row_value}\n", end="")
        for col_key, col_value in enumerate(row_value, start = 0):
            #print(f"Column: {col_key}; Value: {col_value}\n", end="")
            if row_key == int(row_choice)-1 and col_key == int(col_choice)-1:
                board[row_key][col_key] = "-"
                print(f"{row_key} {col_value}")

    for row_key, row_value in enumerate(board, start = 0):
        #print(f"Row: {row_key}; Value: {row_value}\n", end="")
        for col_key, col_value in enumerate(row_value, start = 0):
            #print(f"Column: {col_key}; Value: {col_value}\n", end="")
            if row_key == 0:
                print(f" {col_value} ", end="")
                if col_key == 2:
                    print(f"\n--|---|--\n", end="")
            elif row_key == 1:
                print(f" {col_value} ", end="")
                if col_key == 2:
                    print(f"\n--|---|--\n", end="")
            elif row_key == 2:
                print(f" {col_value} ", end="")

    # I am able to print board and take over a letter with a dash 
    # in an endless looping. this is improving but not quite done