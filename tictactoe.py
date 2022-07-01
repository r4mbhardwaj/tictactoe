"""
Tic Tac Toe Player
"""

import enum
import math
import random
import numpy as np
import copy

X = "X"
O = "O"
EMPTY = None


def get_opposite_player(player):
    if player == X:
        return O
    else:
        return X


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
    if b.count(X) > b.count(O): # if there are more Xs than Os
        print(f"{O}'s turn") # then its O's turn
        return O
    else: # if there are more Os than Xs
        print(f"{X}'s turn") # then its X's turn
        return X


def actions(board): # returns a list of all possible actions
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = [] # create a list of all possible actions
    for x_index, x in enumerate(board): # for each row
        for y_index, y in enumerate(x): # for each element in the row
            if y == EMPTY: # if the element is empty
                options.append((x_index, y_index)) # add the action to the list
    options.sort() # sort the list
    return options # return the list


def result(board, action): # returns the board that results from making action on board
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result

    
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



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move
    return v, move

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