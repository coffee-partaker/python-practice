# win scenarios
scenarios = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def was_won(board, values):

    for scenario in scenarios:
        #print(scenario, "%d == %d == %d" % (board[scenario[0]], board[scenario[1]], board[scenario[2]]))
        #print(scenario, "%d == %d == %d" % (board[scenario[0]], board[scenario[1]], board[scenario[2]]))
        if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
            if board[scenario[0]] != 0:
                return True
    
    return False

def is_board_complete(board, values):
    for position in board:
        if position == values[0]:
            return False
    return True