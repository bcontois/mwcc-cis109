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

for row, row_value in enumerate(board, start = 0):
#   print(f"Row: {row}; Value: {row_value}\n", end="")
    for col, col_value in enumerate(row_value, start =0):
#       print(f"Column: {col}; Value: {col_value}\n", end="")
        if row == 0:
            print(f" {col_value} ", end="")
            if col == 2:
                print(f"\n--+---+--\n", end="")
        elif row == 1:
            print(f" {col_value} ", end="")
            if col == 2:
                print(f"\n--+---+--\n", end="")
        elif row == 2:
            print(f" {col_value} ", end="")
        

























# print(random_number)
# print("Welcome to Tic Tac Toe!\n")
# if random_number == 0:
#     print("X's will go first.\n\n\n\n\n\n")
# else:
#     print("O's will go first.\n\n\n\n\n\n")

