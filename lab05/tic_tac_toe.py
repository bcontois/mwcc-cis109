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
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
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







# #recording of good or bad guess, guesses left
# #progrss statemtents, and updating of the board 
#     letters_guessed.append(guess)
#     if guess in word:
#         for i, letter in enumerate(word, start=0):
#             if letter == guess:
#                 board[i] = word[i]
#         print(f"\n\ngood guess! {guess} is in the word!")
#     else:
#         bad_guesses.append(guess)
#         remaining_guesses -= 1
#         if remaining_guesses == 1:
#             print("\n\n", end="")
#             print(f"sorry, {guess} is not in the word.", end=" ")
#             print(f"you have {remaining_guesses} guess left.")
#         else:
#             print("\n\n", end="")
#             print(f"sorry, {guess} is not in the word.", end=" ")
#             print(f"you have {remaining_guesses} guesses left.")