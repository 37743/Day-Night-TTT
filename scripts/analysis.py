# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Uniform Cost Search's Cost Board Generation and Modification
# ---

def analyse_board(board, cost=[1,1,1,
                               1,0,1, # Center is more valuable by default
                               1,1,1]):
    ''' Calculate cost of the whole board (adjacency)'''
    unit = 2
    for idx,turn in enumerate(board.board):
        if turn == 2:
            # Rows
            if idx in (0,1,2):
                cost[idx+3] -= unit
            if idx in (3,4,5):
                cost[idx-3] -= unit
                cost[idx+3] -= unit
            if idx in (6,7,8):
                cost[idx-3] -= unit
            # Columns
            if idx in (0,3,6):
                cost[idx+1] -= unit
            if idx in (1,4,7):
                cost[idx-1] -= unit
                cost[idx+1] -= unit
            if idx in (2,5,8):
                cost[idx-1] -= unit
            # Corners
            if idx in (0,2,6,8):
                cost[4] -= unit
    string = ""
    for i in cost:
        string += str(i) + " "
    print("COST BOARD: " + string[:-1])
    return cost
