#https://itsmybot.com/how-to-make-tic-tac-toe-game-in-python/



def create_board():
    """Initialize an empty 3x3 game board"""
    return [' ' for _ in range(9)]

def display_board(board):
    """Print the game board in a 3x3 grid format"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def player_move(board, player):
    """Get player input and update the board"""
    while True:
        try:
            position = int(input(f"Player {player}, choose your position (1-9): "))
            position -= 1
            
            if position < 0 or position > 8:
                print("Position must be between 1 and 9!")
                continue
                
            if board[position] == ' ':
                board[position] = player
                break
            else:
                print("That position is already taken! Choose another.")
        except ValueError:
            print("Please enter a valid number!")

def check_winner(board, player):
    """Check if the current player has won"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for condition in win_conditions:
        if (board[condition[0]] == player and 
            board[condition[1]] == player and 
            board[condition[2]] == player):
            return True
    return False

def check_draw(board):
    """Check if the game is a draw"""
    return ' ' not in board

def play_game():
    """Main game loop"""
    board = create_board()
    current_player = 'X'
    game_over = False
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    
    while not game_over:
        display_board(board)
        player_move(board, current_player)
        
        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()


# AGAIN THIS IS NOT MY WORK I am not able to figure this out