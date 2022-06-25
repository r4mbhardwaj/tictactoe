"""
Tic Tac Toe Player
"""

import enum
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
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
    b = []
    for values in board:
        b.extend(values)
    print(b)
    return True
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    rules = [[0, 1, 2], [0, 0, 0], [1, 1, 1], [2, 2, 2]]
    passed = True
    for rule in rules:
        print(rule)
        passed = True
        for index, value in enumerate(rule):
            print(board[index][index])
            # print(index, value)
            if board[index][index] != value:
                passed = False
        if not passed:
            for index, value in enumerate(list(reversed(rule))):
                if index != value:
                    passed = False
    return passed
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
