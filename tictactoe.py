"""
Tic Tac Toe Player
"""

import enum
import math

import numpy as np


X = "X"
O = "O"
EMPTY = None


def initial_state(): # returns the initial state of the board
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def player(board):
    """
    Returns player who has the next turn on a board.
    """
    print("running player")
    b = []
    for values in board:
        b.extend(values)
    print('player over')
    if b.count(X) > b.count(O):
        return O
    else:
        return X


def actions(board): # returns a list of all possible actions
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = []
    for x_index, x in enumerate(board):
        for y_index, y in enumerate(x):
            if y == EMPTY:
                options.append((x_index, y_index))
    return set(options)


def result(board, action, player): # returns the board that results from making action on board
    """
    Returns the board that results from making move (i, j) on the board.
    """
    brd = []
    for value in board:
        if value == action[0]: # if row now is same as action[0]
            vlu = []
            for val in value:
                if val == action[1]:
                    vlu.append(player)
                else:
                    vlu.append(val)
            brd.append(vlu)
        else:
            brd.append(value)
    return brd
    

    
# when does X or O win?
# X or O wins when there is a row, column, or diagonal of 3 of the same symbol

# how to determine if X or O wins?
# write a function function that determine if there is a row, column, or diagonal of 3 of the same symbol

def utility(board): # returns the utility of the board
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # get all the rows and columns of board
    matrix = np.array(board)
    rows = []
    columns = []
    for row in board:
        rows.append(row)
    for index in range(3):
        # print(index)
        cols = []
        for row in rows:
            cols.append(row[index])
        columns.append(cols)
    # get diagonals from rows and columns of 3x3 list
    diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
    diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
    diagonals = [n.tolist() for n in diags]
    totals = rows + columns + diagonals
    for line in totals:
        if line.count(X) == 3: # if there are 3 Xs in a row
            return 1
        elif line.count(O) == 3: # if there are 3 Os in a row
            return -1
    return 0 # otherwise return 0 as the utility of the board

def minimax(board): # returns the optimal action for the current player on the board
    """
    Returns the optimal action for the current player on the board.
    """
    return (1, 1)


def terminal(board): # returns true if the game is over
    """
    Returns True if game is over, False otherwise.
    """
    value = utility(board)
    if value == 1 or value == -1:
        return True


def winner(board): # returns the winner of the game, or None if there is no winner
    """
    Returns the winner of the game, if there is one.
    """
    value = utility(board)
    if value == 1:
        return X
    elif value == -1:
        return O