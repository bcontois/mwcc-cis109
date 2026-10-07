#Brian J Contois
#07 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#hangman.py

import random

#constants & variables needed to run the game
wordlist = ["python", "program", "computer", "science", "algorithm",]
random_number = random.randint(0, len(wordlist) - 1)
word = wordlist[random_number].strip()
letters_guessed = []
bad_guesses = []
remaining_guesses = 6
board = list("_" * len(word))

#ASCII Artwork for hangman
artwork = ["""\n\n\n\n\n\n""",
"""
+---+
|   
|
|
|   
=======""",
"""
+---+
|   |
|   
|
|    
=======""",
"""
+---+
|   |
|   0
|   
|   
=======""",
"""
+---+
|   |
|   0
|   | 
|
=======""",
"""
+---+
|   |
|   0
|  /|\\ 
| 
=======""",
"""
+---+
|   |
|   0
|  /|\\ 
|  / \\
======="""
]

#greetings!
print(f"Welcome to Hangman, Presented to You by Brian Joseph Contois!!", end="")
print("\n", end="")
print(f"\nThe word to guess is: {board}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#main loop of game
while True:       

    guess = input("guess a letter: ").lower()

#input validation             
    if len(guess) != 1 or not guess.isalpha():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\ninvalid input. please enter a single letter.\n\n\n\n\n\n")
        input("\nplease hit [enter] to continue...")
        continue

#tally of all letters guessed
    if guess in letters_guessed:
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
        print("\nyou have already guessed that letter. please try again.", end="")
        print(f"\nletters previously guessed: {letters_guessed}\n\n\n\n\n")
        input("\nplease hit [enter] to continue...")
        continue

#recording of good or bad guess, guesses left
#progrss statemtents, and updating of the board 
    letters_guessed.append(guess)
    if guess in word:
        for i, letter in enumerate(word, start=0):
            if letter == guess:
                board[i] = word[i]
        print(f"\n\ngood guess! {guess} is in the word!")
    else:
        bad_guesses.append(guess)
        remaining_guesses -= 1
        if remaining_guesses == 1:
            print("\n\n", end="")
            print(f"sorry, {guess} is not in the word.", end=" ")
            print(f"you have {remaining_guesses} guess left.")
        else:
            print("\n\n", end="")
            print(f"sorry, {guess} is not in the word.", end=" ")
            print(f"you have {remaining_guesses} guesses left.")

#printing of the current board with correct letters 
#and letters of bad guesses
    print(f"\nWord: {' '.join(board)}")
    print(f"\nBad guesses: {', '.join(bad_guesses)}\n\n\n\n\n")

#ASCII artwork for hangman gallows printout
    match (remaining_guesses):
        case 0:
            print(artwork[6])
        case 1:
            print(artwork[5])
        case 2:
            print(artwork[4])
        case 3:
            print(artwork[3])
        case 4:
            print(artwork[2])
        case 5:
            print(artwork[1])
        case 6:
            print(artwork[0]) 

#victory conditions met or failed
    if "_" not in board:
        print(f"Congratulations! ~{word}~ Is Correct! You Win! ^-^\n")
        break
    if remaining_guesses == 0:
        print(f"Boo Hiss! Game Over! The Word Was ~{word}~ >_<\n")
        break