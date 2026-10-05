#Brian J Contois
#30 September 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#hangman.py

import random

wordlist = ["python", "program", "computer", "science", "algorithm", "zebra"]





while(len(bad_guesses) <= max_bad_guesses and "_" in(board)):
    print(f"\nWord: {' '.join(board)}")
    print(f"Bad guesses: {', '.join(bad_guesses)}")
    guess = input("Guess a letter: ").lower()


word = wordlist[random.randint(0, len(wordlist) - 1)].strip()
board = list("_" * len(word))
bad_guesses = []
max_bad_guesses = 6

while(len(bad_guesses) <= max_bad_guesses and "_" in(board)    
    print("\nWelcome to Hangman!\n")
    print(f"


#Input Validation
if len(guess) != 1 or not guess.isalpha():
        print("\nInvalid input. Please enter a single letter.")
        input("Hit [enter] to continue...\n")
        continue
        if guess in bad_guesses or guess in board:
            print("\nYou have already guessed that letter. Please try again.")
            input("Hit [enter] to continue...\n")
            continue

    is_found = False
    for i, letter in enumerate(word, start=0):
        if letter == guess:
            board[i] = word[i]
            is_found = True
        if not is_found:
            bad_guesses.append(guess)
            print(f"\nSorry, {guess} is not in the word.")
            input("Hit [enter] to continue...\n")
        else:
            print(f"\nGood guess! {guess} is in the word.")
            input("Hit [enter] to continue...\n")