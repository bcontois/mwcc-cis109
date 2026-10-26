#Brian J Contois
#10 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#tictactoe_03.py

import random

random_number = (random.randint(1, 20)) % 2

if random_number == 0:
    print("\n\n\n\nO's will go first.\n\n")
    player_1 = "O"
    player_2 = "X"
else:
    print("\n\n\n\nX's will go first.\n\n")
    player_1 = "X"
    player_2 = "O"

matrix = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

print(matrix[0], matrix[1], matrix[2])
print(matrix[3], matrix[4], matrix[5])
print(matrix[6], matrix[7], matrix[8])
print("\n\n")

while True:

    print(f"{player_1}'s Turn")
    choice_row = input(f"Enter Row:")
    if not choice_row.isdigit():
        print(f"\n\nInvalid Option\n\n")
        continue
    if int(choice_row) < 1 or int(choice_row) > 3:
        print(f"\n\nInvalid Option\n\n") 
        continue