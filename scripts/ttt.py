# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Tic-Tac-Toe Board Code
# ---
import numpy as np
import scripts.datastructures.stack as stack
import scripts.datastructures.queue as queue
import scripts.analysis as analysis
import collections

AI_CELL = 0
BOARD_X = 3
BOARD_Y = 3
BOARD_DIMENSIONS = (BOARD_X, BOARD_Y)
# Current state of the game.
state = {"DRAW" : 0,
        "X WON" : 1,
        "O WON" : 2,
        "ONGOING" : 3}

# X/O Symbols to populate the matrix with.
MARK_EMPTY = 0
MARK_X = 1
MARK_O = 2
# Current turn, X always starts first.
TURN_PVP = 1
TURN_PVA = 1

COST = [1,1,1,
        1,0,1,
        1,1,1]

empty_board = np.zeros(BOARD_DIMENSIONS, dtype = int).flatten()
# print(empty_board)

def pvp_mod(reset=False):
    ''' Reset PVP turn counter or increment it'''
    global TURN_PVP
    if (reset):
        TURN_PVP = 1
    else:
        TURN_PVP += 1


def pva_mod(reset=False):
    ''' Reset PVP turn counter or increment it'''
    global TURN_PVA
    if (reset):
        TURN_PVA = 1
    else:
        TURN_PVA += 1

def rand_optimal_move(board, cturn, depth=0):
    ''' Find the best possible move for the A.I. DEFAULT: RANDOM'''
    bestmove = np.random.choice(board.get_valid_indices(), 1)[0]
    if (depth<10):
        for move in board.get_valid_indices():
            # Test if A.I. move is best
            depth = depth+1
            bestmove = rand_optimal_move(board, cturn, depth)
            player = MARK_O if (cturn%2 == 0) else MARK_X
            # Try A.I. move
            board.board[move] = player
            # Change turn to IRL player
            cturn += 1
            # Revert A.I. move
            tempresult = board.get_result()
            board.board[move] = 0
            # Check if A.I. player wins on this move.
            if (player==MARK_O and (tempresult==state['O WON']) or\
                     (player==MARK_X and (tempresult==state['X WON']))):
                bestmove = move
                break
    return bestmove

def dfs_move(boards, cboard, cturn, best_move, pbest_move):
    ''' Function for best move using Depth-First-Search technique'''
    for mv in cboard.get_valid_indices():
        player = MARK_O if (cturn%2 ==0) else MARK_X
        cboard.board[mv] = player
        boards.push(cboard, mv)
        cturn += 1
        temp_result = boards.top().get_result()
        pbest_move = dfs_move(boards, boards.top(), cturn, best_move, pbest_move)
        cboard.board[mv] = 0
        # print(cboard.board)
        if (player==MARK_O and (temp_result==state['O WON']) or\
            (player==MARK_X and (temp_result==state['X WON']))):
            return mv
    while not (boards.is_empty()):
        # Previous best move, since at last step we pop the parent node.
        pbest_move = best_move
        best_move = boards.pop()
    return pbest_move

def dfs_optimal_move(board, cturn):
    ''' Find the best optimal move using Depth-First-Search technique'''
    boards = stack.Stack()
    boards.push(board)
    best_move = dfs_move(boards, boards.top(), cturn, best_move=0, pbest_move=0)
    return best_move

def bfs_move(boards, cboard, cturn, best_move):
    ''' Function for best move using Breadth-First-Search technique'''
    for mv in cboard.get_valid_indices():
        player = MARK_O if (cturn%2 ==0) else MARK_X
        cboard.board[mv] = player
        boards.enqueue(cboard, mv)
        cturn += 1
        best_move = bfs_move(boards, boards.top(), cturn, best_move)
        cboard.board[mv] = 0
    while not (boards.is_empty()): 
        player = MARK_O if (cturn%2 ==0) else MARK_X
        temp_result = boards.top().get_result()
        if (player==MARK_O and (temp_result==state['O WON']) or\
        (player==MARK_X and (temp_result==state['X WON']))):
            return boards.dequeue()
        # print(boards.top().board)
        boards.dequeue()
    return best_move

def bfs_optimal_move(board, cturn):
    ''' Find the best optimal move using Breadth-First-Search technique'''
    boards = queue.Queue()
    boards.enqueue(board)
    best_move = bfs_move(boards, boards.top(), cturn, best_move=0)
    return best_move

def gs_move(board, cost):
    ''' Function for best move using Greedy-Search technique'''
    min_value = 99
    best_move = 0
    for idx in board.get_valid_indices():
        if (cost[idx] < min_value):
            best_move = idx
        min_value = min(min_value, cost[idx])
    # print(board.board)
    print(min_value)
    return best_move

def gs_optimal_move(board):
    ''' Find the best optimal move using Greedy-Search technique'''
    best_move = gs_move(board, analysis.analyse_board(board, COST))
    return best_move

def ucs_move(boards, cboard, cturn, best_move, min_value, cost):
    ''' Function for best move using Uniform-Cost-Search technique'''
    for mv in cboard.get_valid_indices():
        player = MARK_O if (cturn%2 ==0) else MARK_X
        cboard.board[mv] = player
        boards.push(cboard, mv)
        cturn += 1
        temp_result = boards.top().get_result()
        best_move = ucs_move(boards, boards.top(), cturn, best_move, min_value, cost)
        cboard.board[mv] = 0
        if (player==MARK_O and (temp_result==state['O WON']) or\
            (player==MARK_X and (temp_result==state['X WON']))):
            return mv
    while not (boards.is_empty()):
        cost = analysis.analyse_board(boards.top(), cost)
        print(boards.top().board)
        for mv in boards.top().get_valid_indices():
            if (cost[mv] < min_value):
                best_move = mv
                min_value = cost[mv]
        boards.pop()
    return best_move

def ucs_optimal_move(board, cturn):
    ''' Find the best optimal move using Uniform-Cost-Search technique'''
    boards = stack.Stack()
    boards.push(board)
    best_move = ucs_move(boards, boards.top(), cturn, best_move=0,\
                         min_value=99, cost=analysis.analyse_board(board, COST))
    return best_move

class TTT():
    ''' Class that contains Tic-Tac-Toe's game logic'''
    def __init__(self, new_board=None):
        if new_board is None:
            self.board = np.copy(empty_board)
        else:
            self.board = new_board
        # Transform from 1 dimensional to 2 dimensional.
        self.board_2d = self.board.reshape(BOARD_DIMENSIONS)
        print(self.board_2d)
    
    def __str__(self):
        return str(self.board)

    def get_result(self):
        ''' Get current state of the match'''
        for sym in[MARK_X,MARK_O]:
            if self.check_rows_cols_diags(sym):
                return sym
        if MARK_EMPTY not in self.board_2d:
            return state['DRAW']
        return state['ONGOING']
    
    def get_valid_indices(self):
        ''' Get all valid indexes that could potentially be marked'''
        return ([i for i in range(self.board.size) if self.board[i] == MARK_EMPTY])
    
    def is_over(self):
        ''' Returns True if game has ended'''
        return self.get_result() != state['ONGOING']
    
    def check_rows_cols_diags(self, sym):
        ''' Check if there exists a winning condition for symbol \'sym\' '''
        # Rotate to get columns.
        temp_board = np.rot90(np.copy(self.board_2d))
        return self.check_rows(self.board_2d, sym) or\
            self.check_rows(temp_board, sym) or\
            self.check_diags(self.board_2d, sym)

    def check_rows(self, board, sym):
        ''' Check rows for a winning combination'''
        test = collections.Counter([sym,sym,sym])
        for i in board:
            if collections.Counter(i) == test:
                return True
        return False
        
    def check_diags(self, board, sym):
        ''' Check diagonals for a winning combination'''
        test = collections.Counter([sym,sym,sym])
        if collections.Counter(board.diagonal()) == test\
        or collections.Counter(np.fliplr(board).diagonal()) == test:
            return True
        return False
    
    def get_player(self, pvp=True):
        ''' Returns which player's turn'''
        # X always starts first
        turn = TURN_PVP if pvp else TURN_PVA
        return MARK_X if (turn%2 != 0) else MARK_O
    
    def get_turn(self, pvp=True):
        ''' Returns count of turns'''
        return TURN_PVP if pvp else TURN_PVA
    
    def play(self, move, pvp=True):
        ''' Marks the board with given index if it is a valid move'''
        temp_board = self.board
        if move not in self.get_valid_indices():
            return TTT(temp_board)
        temp_board[move] = self.get_player()
        pvp_mod() if pvp else pva_mod()
        return TTT(temp_board)
    
    def play_ai(self, type='UCS'):
        ''' A.I. plays generates moves recursively and picks the best option'''
        # Choose search/solve technique:
        match type:
            case 'DFS':
                aimove = dfs_optimal_move(self, self.get_turn(pvp=False))
            case 'BFS':
                aimove = bfs_optimal_move(self, self.get_turn(pvp=False))
            case 'UCS': 
                aimove = ucs_optimal_move(self, self.get_turn(pvp=False))
            case 'GS':
                aimove = gs_optimal_move(self)
            case _: # DEFAULT (RND)
                aimove = rand_optimal_move(self, self.get_turn(pvp=False))
        global AI_CELL
        AI_CELL = aimove
        # It's O but its so I can change this later to reverse play order.
        # vvv
        self.board[aimove] = self.get_player(pvp=False)
        # Turn gets incremented in the IRL player's code.
        pva_mod()
        return TTT(self.board)
            
    def get_ai_cell(self):
        global AI_CELL
        return AI_CELL

    def reset(self, pvp=True):
        ''' Reset to a blank board'''
        self.board = np.copy(empty_board)
        self.board_2d = self.board.reshape(BOARD_DIMENSIONS)
        global COST
        COST = [1,1,1,
                1,0,1,
                1,1,1]
        if (pvp):
            pvp_mod(reset=True)
        else:
            pva_mod(reset=True)
        return