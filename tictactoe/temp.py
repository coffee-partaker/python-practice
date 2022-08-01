
from random import randint
import time
from typing import List, TypeVar
class Board:
    
    T = TypeVar("T")

    values = []

    # win scenarios
    scenarios = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    current_player = -1
    
    def __init__(self, values: List[T] ):
        self.values = values
        pass
    
    '''
    it receives an array with 9 positions
    filled with values between 0 and 2.
    it will be treated like a matrix.
    0 1 2
    3 4 5
    6 7 8
    '''

    def was_won(self, board: List[T]):    
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] != self.values[0]:
                    return True
        
        return False

    def is_board_empty(self, board: List[int]):
        for position in board:
            if position != self.values[0]:
                return False
        return True

    def is_board_complete(self, board: List[T]):
        for position in board:
            if position == self.values[0]:
                return False
        return True

    def evaluate(self, board: List[T]):
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] == self.values[self.current_player]:
                    return 10
                else: 
                    return -10
        return 0

    def minimax(self, board: List[T], depth: int, isMaximizingPlayer: bool):
        score = self.evaluate(board)

        if(self.was_won(board)):
            return score
    
        if self.is_board_complete(board):
            return 0
        
        if isMaximizingPlayer:
            best = -10000
            for i in range(0,9) :
                if board[i] == self.values[0]:
                    board[i] = self.values[self.current_player] if isMaximizingPlayer else self.values[1 if self.current_player == 2 else 2]
                    best = max(best, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]
               
            return best

        else :
            best = 1000 
            for i in range(0,9) :
                if board[i] == self.values[0]:
                    board[i] = self.values[self.current_player] if isMaximizingPlayer else self.values[1 if self.current_player == 2 else 2]
                    best = min(best, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]
               
            return best

    def is_valid_board(self, board: List[T]):
        if len(board) != 9:
            return False
      
        n1 = board.count(self.values[1])
        n2 = board.count(self.values[2])
        
        if n1 == n2 or n1 + 1 == n2 or n2 + 1 == n1:
            return True
        
        return False

    def whoseTurn(self, board: List[int]):
        if len(board) != 9 or self.was_won(board):
            return -1
      
        n1 = board.count(self.values[1])
        n2 = board.count(self.values[2])
        
        if n1 == n2 or n1 + 1 == n2:
            return 1
        elif n2 + 1 == n1:
            return 2
        else:
            return -1     

    def best_move(self, board: List[T]):
        bestVal = -1000
        bestMove = -1
        time.sleep(3)
        if self.is_board_empty(board):
            return {
                0: 0,
                1: 2,
                2: 4,
                3: 6,
                4: 8

            }[randint(0, 4)]

        self.current_player = self.whoseTurn(board)

        if self.current_player == -1:
            return -1      

        for i in range(0, 9) :
            if board[i] == self.values[0]:
                
                board[i] = self.values[self.current_player]
                
                moveVal = self.minimax(board, 0, False)
                
                board[i] = self.values[0]
                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal
                    #print(bestVal)
        
        return bestMove