
import random
def Display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2]+'|')
    print(board[3] + '|' + board[4] + '|' + board[5]+'|')
    print(board[6] + '|' + board[7] + '|' + board[8]+'|')

def intro():
    user=''
    while user not in ['X','O']:
        user = input('Choose your side X or O: ').upper()
        if user not in ['X','O']:
            print('Invalid input. Please choose X or O.')
        continue
    if user == 'X':
        Player1 = 'X'
        player2 = 'O'
        print('you have choosen X')
    else:
        Player1 = 'O'
        player2 = 'X'
        print('you have choosen O')
    return Player1, player2
def turn():
    return random.choice(['X','O'])

def check_winner(player, board):
    conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                  (0, 4, 8), (2, 4, 6)]   # diagonals
    for check in conditions:
        if board[check[0]] == board[check[1]] == board[check[2]] == player:
            print(f"{player} wins!")
            return True
    else:
            return False
    
def startgame(board):
    Player1, Player2 = intro()
    print("Let's start the game\nTossing the coin to choose who will start first...")
    first_player = turn()
    print(f"{first_player} will start first.")
    if first_player == Player2: 
         Player2,Player1=Player1,first_player
    Display_board(board)
    while True:
        while True:
            try:
                if '-' not in board:
                    print("It's a tie!")
                    return
                player1_option =int(input(f"{Player1}, choose a position from 1-9: ")) #by default input is string
                if player1_option < 1 or player1_option > 9:
                    print("Invalid input. Please choose a position from 1-9.")
                    continue
                if board[(player1_option)-1] == '-':
                    board[(player1_option)-1] = Player1
                    Display_board(board)
                    if check_winner(Player1,board): return
                    break
                else:
                    print("Position already taken. Choose another position.")
                
            except ValueError:
                print("Invalid input. Please enter a number from 1-9.")
                continue
        while True:
            try:
                if '-' not in board:
                    print("It's a tie!")
                    return
                player2_option = int(input(f"{Player2}, choose a position from 1-9: ")) #by default input is string
                if player2_option < 1 or player2_option > 9:
                    print("Invalid input. Please choose a position from 1-9.")
                    continue
                if board[(player2_option)-1] == '-':
                    board[(player2_option)-1] = Player2
                    Display_board(board)
                    if check_winner(Player2,board): return
                    break
                else:
                    print("Position already taken. Choose another position.")
                
            except ValueError:
                print("Invalid input. Please enter a number from 1-9.")
                continue
        
def continue_game():
    board = ['-' for i in range(9)]
    startgame(board)
    while True:
        game_replay = input("Do you want to play again? (yes/no): ").lower()
        if game_replay not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        if game_replay == 'yes':  
            continue_game()
        else:
            print("Thanks for playing!")
            exit()  
continue_game()

    
