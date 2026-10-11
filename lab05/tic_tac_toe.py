#Brian J Contois
#10 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#tic_tac_toe.py

import random

random_number = (random.randint(1, 20)) % 2

row_0 = ["-", "-", "-"]
row_1 = ["-", "-", "-"]
row_2 = ["-", "-", "-"]

matrix= [
    row_0,
    row_1,
    row_2
]
print(random_number)
print("Welcome to Tic Tac Toe!\n")
if random_number == 0:
    print("X's will go first.\n\n\n\n\n\n")
else:
    print("O's will go first.\n\n\n\n\n\n")

print(matrix[0])
print(matrix[1])
print(matrix[2])
print("\n\n\n\n\n\n")