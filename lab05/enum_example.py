wordlist = ["python"]

# board is python
board = [
      '-',
      '-',
      '-',
      '-',
      '-',
      '-',
]
word = wordlist[0]
guess = "t"

# with each iteration of the loop...
# enumerate returns (0,p)
# developer assigns these variables 
for idx, letter in enumerate(word, start = 0):
        print(f"Index: {idx}; Letters: {letter}")
        if letter == guess:
            print(f"match found at index {idx}; letter: {letter}")
            board[2] = letter
            print(f"{board}")