from ascii_cards import ascii_cards
import random

suits = ['♥', '♦', '♣','♠']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

def get_deck():
    for suit in suits:
        for i in range(0,13):
            deck.append([values[i], suit])
    return deck
get_deck()

def display_deck():
    for card in deck:
        print(ascii_cards.display_cards([card]))

def shuffle_deck(deck):
    shuffled_deck = []
    while len(deck) > 0:
        card = random.randint(0, len(deck)-1)
        shuffled_deck.append(deck.pop(card))
    return shuffled_deck
        
def play_game(deck):
    player_score = 0
    house_score = 0

    response = 'Y'
    valid_responses = ['Y', 'N']
    while response != 'N' and player_score <= 21:
        #Players Turn
        card = deck.pop()
        if card[0].isdigit():
            player_score = player_score + int(card[0])
        else:
            player_score = player_score + 10

        print(ascii_cards.display_cards([card]))
        print(f"Player Score: {player_score}\n")

        if player_score < 21:
            response = (input("Would you like to hit? (Y/N): ")).upper()



# get_deck()
# deck = shuffle_deck(deck)
# display_deck()





# deck = get_deck()
# # got here!
# print(f"{suits}")
# print(f"{values}")
# #print(ascii_cards.display)
# #print(get_deck())

# #print(ascii_cards.display_cards(deck[2:7]))

# print(ascii_cards.display_cards(deck[3:5]))


