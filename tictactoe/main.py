from temp import is_board_complete, was_won
from predict_moves import predict_best_move
# consume api
# alternate turns
# human vs human
# human vs machine
def welcome_message():
    print("""
Welcome to TicTactoe

Do you want play with?
  [0] - Human  
  [1] - Machine  
""")

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
valid_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
values = [0, 1, 2]
running = True

welcome_message()
while True:
    choice = int(input())
    if choice == 0 or choice == 1:
        break


def print_board():
    print("---------")
    print("%d - %d - %d" % (board[0], board[1], board[2]) )
    print("%d - %d - %d" % (board[3], board[4], board[5]) )
    print("%d - %d - %d" % (board[6], board[7], board[8]) )
    print("---------")

def human_vs_human():
    played_moves = []
    print("Pick a position: ")
    while(True):
        player1 = -1
        player2 = -1
        while(True):
            player1 = int(input("Player 1: "))
            if valid_moves.count(player1) != 0 and played_moves.count(player1) == 0:
                board[player1] = values[1]
                played_moves.append(player1)
                break
       
        print_board()
        if was_won(board, values):
            print("Player 1 won!")
            break
        elif is_board_complete(board, values):
            print("Draw!")
            break
      
        while(True):
            player2 = int(input("Player 2: "))
            if valid_moves.count(player2) != 0 and played_moves.count(player2) == 0:
                board[player2] = values[2]
                played_moves.append(player2)
                break
        print_board()
        if was_won(board, values):
            print("Player 2 won!")
            break
        elif is_board_complete(board, values):
            print("Draw!")
            break
    
        

def human_vs_machine():
    played_moves = []
    print("Pick a position: ")
    while(True):
        player1 = -1
        player2 = -1
        
        while(True):
            player1 = int(input("Player: "))
            if valid_moves.count(player1) != 0 and played_moves.count(player1) == 0:
                board[player1] = values[1]
                played_moves.append(player1)
                break
       
        print_board()
        if was_won(board, values):
            print("You won!")
            break
        elif is_board_complete(board, values):
            print("Draw! The mankind was spared.")
            break
        while(True):
            player2 = predict_best_move(board, values)
            print(player2)
            if valid_moves.count(player2) != 0 and played_moves.count(player2) == 0:
                board[player2] = values[2]
                played_moves.append(player2)
                break
        print_board()
    
        if was_won(board, values):
            print("The machine won! Bip bop.")
            break
        elif is_board_complete(board, values):
            print("Draw! The mankind was spared.")
            break
        
        
#1 - 0 - 0
#2 - 1 - 0
#0 - 0 - 2
if choice == 0:
    human_vs_human()
else:
    human_vs_machine()


