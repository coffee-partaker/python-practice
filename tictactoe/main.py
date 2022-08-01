from temp import Board
from predict_moves import predict_best_move
# consume api
# alternate turns
# human vs human
# human vs machine
def welcome_message():
    print("""
Welcome to TicTactoe

Who do you want play against?
  [0] - The Human
  [1] - The Machine
  [2] - Watch Mode
""")

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
valid_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
values = [0, 1, 2]
running = True

machine = Board(values)

welcome_message()
while True:
    choice = int(input())
    if choice >= 0 and  choice < 3:
        break


def print_board():
    print("---------")
    print("%d - %d - %d" % (board[0], board[1], board[2]) )
    print("%d - %d - %d" % (board[3], board[4], board[5]) )
    print("%d - %d - %d" % (board[6], board[7], board[8]) )
    print("---------")

def human_vs_human():
    played_moves = []
    print("Contemplation of human inferiority: ")
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
        if  machine.was_won(board):
            print("Player 1 won!")
            break
        elif machine.is_board_complete(board):
            print("Draw!")
            break
      
        while(True):
            player2 = int(input("Player 2: "))
            if valid_moves.count(player2) != 0 and played_moves.count(player2) == 0:
                board[player2] = values[2]
                played_moves.append(player2)
                break
        print_board()
        if  machine.was_won(board):
            print("Player 2 won!")
            break
        elif machine.is_board_complete(board):
            print("Draw!")
            break
    
        

def human_vs_machine():
    played_moves = []
    print("Prepare thyselves for annihilation: ")
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
        if  machine.was_won(board):
            print("You won! The machines were outsmarted")
            break
        elif machine.is_board_complete(board):
            print("Draw! The humankind was spared.")
            break
        while(True):
            player2 = machine.best_move(board)
            print(player2)
            if valid_moves.count(player2) != 0 and played_moves.count(player2) == 0:
                board[player2] = values[2]
                played_moves.append(player2)
                break
        print_board()
        if  machine.was_won(board):
            print("The machine won! Bip bop.")
            break
        elif machine.is_board_complete(board):
            print("Draw! The humankind was spared.")
            break
        

def machine_vs_machine():
    played_moves = []
    print("Behold the evolution: ")
    while(True):
        player1 = -1
        player2 = -1
        
        while(True):
            player1 = machine.best_move(board)
            if valid_moves.count(player1) != 0 and played_moves.count(player1) == 0:
                board[player1] = values[1]
                played_moves.append(player1)
                break
       
        print_board()
        if  machine.was_won(board):
            print("The machine won! Exactly as predicted.")
            break
        elif machine.is_board_complete(board):
            print("Draw! There are no room for improvement.")
            break
        while(True):
            player2 = machine.best_move(board)
            print(player2)
            if valid_moves.count(player2) != 0 and played_moves.count(player2) == 0:
                board[player2] = values[2]
                played_moves.append(player2)
                break
        print_board()
        if  machine.was_won(board):
            print("The machine won! The axiom has been proven truthful.")
            break
        elif machine.is_board_complete(board):
            print("Draw! There are no room for improvement.")
            break
        
if choice == 0:
    human_vs_human()
elif choice == 1:
    human_vs_machine()
else:
    machine_vs_machine()
