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

print(f"Welcome to Hangman, Presented to You by Brian Joseph Contois!!", end="")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
print(f"\nthe word to guess is: {board}\n")

while True:
    guess = input("guess a letter: ").lower()

    match remaining_guesses:
        case 5:
            print('''
+---+
|
|
|
|    
=======''')
        case 4:
            print('''
+---+
|   |
|
|
|   
=======''')
        case 3:
            print('''
+---+
|   |
|   0
|
|    
=======''')
        case 2:
            print('''
+---+
|   |
|   0
|   |
|    
=======''')
        case 1:
            print('''
+---+
|   |
|   0
|   |
|   |
=======''')
        case 0:
            print('''
+---+
|   |
|   0
|   |
|   |
=======''')
             
    if len(guess) != 1 or not guess.isalpha():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\ninvalid input. please enter a single letter.")
        input("\nplease hit [enter] to continue...")
        continue
    if guess in letters_guessed:
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\nyou have already guessed that letter. please try again.", end="")
        print(f"\nletters previously guessed: {letters_guessed}\n\n\n")
        input("\nplease hit [enter] to continue...")
        continue
    letters_guessed.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                board[i] = guess
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\ngood guess! {guess} is in the word!")
    else:
        bad_guesses.append(guess)
        remaining_guesses -= 1
        if remaining_guesses == 1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
            print(f"sorry, {guess} is not in the word.", end=" ")
            print(f"you have {remaining_guesses} guess left.")
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
            print(f"sorry, {guess} is not in the word.", end=" ")
            print(f"you have {remaining_guesses} guesses left.")

    print(f"\nWord: {' '.join(board)}")
    print(f"\nBad guesses: {', '.join(bad_guesses)}\n")

    if "_" not in board:
        print(f"Congratulations! ~{word}~ Is Correct! You Win! ^-^\n")
        break
    if remaining_guesses == 0:
        print(f"Boo Hiss! Game Over! The Word Was ~{word}~ >_<\n")
        break









