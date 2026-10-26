#python
wordlist = [
    "llama",
    "python"
]

word = wordlist[1]


##############################
# Without Enumeration

board = [
    '-',
    '-',
    '-',
    '-',
    '-',
    '-'
]


print("WITH ENUMERATION\n")

GUESS = "p"
idx = 0
for letter in word:
    print(f"Letter: {letter}")

    if GUESS == word[idx]:
        print("MATCH FOUND!")
        board[idx] = word[idx]

    idx += 1
print(board)


##############################
# With Enumeration
print("WITH ENUMERATION\n")

board = [
    '-',
    '-',
    '-',
    '-',
    '-',
    '-'
]

GUESS = "t"
for idx, letter in enumerate(word):
    # With each iteratation of the loop...
    # enumerate == RETURNS (KEY, VALUE) ==> (0, "p")
    # developer ASSIGNS THESE VARIABLES (idx, letter) = (0, "p")
    print(f"Index: {idx}; Letter: {letter}")
    if letter == GUESS:
        print(f"MATCH FOUND AT Index: {idx}; Letter: {letter}")
        board[idx] = word[idx]
print(board)