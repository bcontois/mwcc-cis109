#Brian J Contois
#04 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#hangman_two_point_oh.py

import random

#constants & variables needed to run the game
wordlist = ["python", "program", "computer", "science", "algorithm",]
random_number = random.randint(0, len(wordlist) - 1)
word = wordlist[random_number].strip()
letters_guessed = []
bad_guesses = []
remaining_guesses = 6
board = list("_" * len(word))

#greetings!
print(f"Welcome to Hangman, Presented to You by Brian Joseph Contois!!", end="")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
print(f"\nthe word to guess is: {board}\n")

#main loop of game
while True:
    guess = input("guess a letter: ").lower()

#It is now 12:35AM on 05 October 2026. trying something for ascii artwork
#This is where the ASCII artwork with case commands are supposed to go
#I cannot get them to work
#I think the rest of this seems to function

    if(remaining_guesses == 6):
        pass
    elif(remaining_guesses == 5):
        print("+---+")
        print("|")
        print("|")
        print("|")
        print("|")
        print("=======")
    elif(remaining_guesses == 4):
        print("+---+")
        print("|   |")
        print("|")
        print("|")
        print("|")
        print("=======")
    elif(remaining_guesses == 3):
        print("+---+")
        print("|   |")
        print("|")
        print("|")
        print("|")
        print("=======")
    elif(remaining_guesses == 2):
        print("+---+")
        print("|   |")
        print("|   0")
        print("|")
        print("|")
        print("=======")
    elif(remaining_guesses == 1):
        print("+---+")
        print("|   |")
        print("|   0")
        print("|  /|\\")
        print("|")
        print("|")
        print("=======")
    elif(remaining_guesses == 0):
        print("+---+")
        print("|   |")
        print("|   0")
        print("|  /|\\ ")
        print("|  / \\ ")
        print("=======")

    #input validation             
        if len(guess) != 1 or not guess.isalpha():
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
            print("\ninvalid input. please enter a single letter.")
            input("\nplease hit [enter] to continue...")
            continue

    #tally of all letters guessed
        if guess in letters_guessed:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", end="")
            print("\nyou have already guessed that letter. please try again.", end="")
            print(f"\nletters previously guessed: {letters_guessed}\n\n\n")
            input("\nplease hit [enter] to continue...")
            continue

    #recording of good or bad guess, guesses left
    #progrss statemtents, and updating of the board 
        letters_guessed.append(guess)
        if guess in word:
            for i, letter in enumerate(word, start=0):
                if letter == guess:
                    board[i] = word[i]
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

    #victory conditions met or failed
        if "_" not in board:
            print(f"Congratulations! ~{word}~ Is Correct! You Win! ^-^\n")
            break
        if remaining_guesses == 0:
            print(f"Boo Hiss! Game Over! The Word Was ~{word}~ >_<\n")
            break