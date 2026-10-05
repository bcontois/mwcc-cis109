#Brian J Contois
#30 September 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#hangman.py

import random

wordlist = ["python", "program", "computer", "science", "algorithm",]

random_number = random.randint(0, len(wordlist) - 1)
word = wordlist[random_number].strip()

letters_guessed = []
bad_guesses = []
remaining_guesses = 6

board = list("_" * len(word))
print(f"Welcome to Hangman, Presented to you by Brian Joseph Contois!!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWord to guess: {board}\n")

while True:
    guess = input("guess a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ninvalid input. please enter a single letter.")
        input("Hit [enter] to continue...")
        continue
    if guess in letters_guessed:
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou have already guessed that letter. Please try again.\nPreviously guessed: {letters_guessed}")
        input("Hit [enter] to continue...")
        continue
    letters_guessed.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                board[i] = guess
        print(f"\n\n\n\n\n\n\nGood guess! {guess} is in the word!")
    else:
        bad_guesses.append(guess)
        remaining_guesses -= 1
        if remaining_guesses == 1:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSorry, {guess} is not in the word. You have {remaining_guesses} guess left.")
        else:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSorry, {guess} is not in the word. You have {remaining_guesses} guesses left.")
    print(f"Word: {' '.join(board)}")
    print(f"Bad guesses: {', '.join(bad_guesses)}")
    if "_" not in board:
        print(f"\n\n\nCongratulations! {word} is correct! You win! ^-^\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        break
    if remaining_guesses <= 0:
        print(f"\n\n\nBoo Hiss! Game over! The word was '{word}' >_<\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        break
