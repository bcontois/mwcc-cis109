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
print(f'''Welcome to Hangman, Presented to You by Brian Joseph Contois!!
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
the word to guess is: {board}\n''')

while True:
    guess = input("guess a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
        invalid input. please enter a single letter.''')

        input("\nplease hit [enter] to continue...")
        continue
    if guess in letters_guessed:
        print(f'''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
        you have already guessed that letter. please try again.
        letters previously guessed: {letters_guessed}\n\n''')

        input("\nplease hit [enter] to continue...")
        continue
    letters_guessed.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                board[i] = guess
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\ngood guess! {guess} is in the word!\n")
    else:
        bad_guesses.append(guess)
        remaining_guesses -= 1
        if remaining_guesses == 1:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nsorry, {guess} is not in the word. you have {remaining_guesses} guess left.\n")
        else:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nsorry, {guess} is not in the word. you have {remaining_guesses} guesses left.\n")
    print(f"Word: {' '.join(board)}")
    print(f"Bad guesses: {', '.join(bad_guesses)}\n")
    if "_" not in board:
        print(f"\n\n\n\n\n\nCongratulations! ~{word}~ Is Correct! You Win! ^-^\n\n\n")
        break
    if remaining_guesses == 0:
        print(f"\n\n\n\n\n\nBoo Hiss! Game Over! The Word Was '{word}' >_<\n\n\n")
        break
