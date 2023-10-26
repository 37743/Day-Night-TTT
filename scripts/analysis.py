from scripts.ttt import MARK_O

def analyse_board(board, cost=[10,10,10,
                               10,9,10,
                               10,10,10]):
    ''' Calculate cost of the whole board (adjacency)'''
    cost = cost
    for idx,value in enumerate(board.board):
        if value == MARK_O:
            # Rows
            if idx in (0,1,2):
                cost[idx+3] -= 1
            if idx in (3,4,5):
                cost[idx-3] -= 1
                cost[idx+3] -= 1
            if idx in (6,7,8):
                cost[idx-3] -= 1
            # Columns
            if idx in (0,3,6):
                cost[idx+1] -= 1
            if idx in (1,4,7):
                cost[idx-1] -= 1
                cost[idx+1] -= 1
            if idx in (2,5,8):
                cost[idx-1] -= 1
            # Corners
            if idx in (0,2,6,8):
                cost[4] -= 1
    return cost
