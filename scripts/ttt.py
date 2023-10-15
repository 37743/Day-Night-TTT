# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Tic-Tac-Toe Board Code
# ---
import numpy as np
import collections

BOARD_X = 3
BOARD_Y = 3
BOARD_DIMENSIONS = (BOARD_X, BOARD_Y)
# Current state of the game.
state = {"DRAW" : 0,
        "X_WIN" : 1,
        "O_WIN" : 2,
        "NOT_OVER" : 3}

# X/O Symbols to populate the matrix with.
MARK_EMPTY = 0
MARK_X = 1
MARK_O = 2
# Current turn, X always starts first.
TURN = 1

empty_board = np.zeros(BOARD_DIMENSIONS, dtype = int).flatten()
# print(empty_board)

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
    
    def get_result(self):
        ''' Get current state of the match'''
        for sym in[MARK_X,MARK_O]:
            if self.check_rows_cols_diags(sym):
                return sym
        if MARK_EMPTY not in self.board_2d:
            return state['DRAW']
        return state['NOT_OVER']
    
    def get_valid_indexes(self):
        ''' Get all valid indexes that could potentially be marked'''
        return ([i for i in range(self.board.size)
                 if self.board[i] == MARK_EMPTY])
    
    def is_over(self):
        ''' Returns True if game has ended'''
        return self.get_result() != state['NOT_OVER']
    
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
    
    def get_player(self):
        ''' Returns which player's turn'''
        # X always starts first
        return MARK_X if (TURN%2 != 0) else MARK_O
    
    def get_turn(self):
        ''' Returns count of turns'''
        return TURN
    
    def play(self, move):
        ''' Marks the board with given index if it is a valid move'''
        temp_board = self.board
        if move not in self.get_valid_indexes():
            return TTT(temp_board)
        temp_board[move] = self.get_player()
        # TO DO: Multithreading, locking this part of the code vvv
        global TURN
        TURN = TURN + 1
        # ^^^
        return TTT(temp_board)
    
    def reset(self):
        ''' Reset to a blank board'''
        self.board = np.copy(empty_board)
        self.board_2d = self.board.reshape(BOARD_DIMENSIONS)