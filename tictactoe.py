"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_init = 0 # Counter for Xs
    o_init = 0 # Counter for Os

    for i in range(0, len(board)): # Check rows
        for j in range(0, len(board[0])):
            if board[i][j] == X: # If there is an X, increase the counter
                x_init += 1
            elif board[i][j] == O: # If there is an O, increase the counter
                o_init += 1
    # If there are more Xs than Os, O is the player
    if x_init > o_init: # X has more Xs
        return O # O is the player
    else: # O has more Os
        return X # X is the player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create new board, without modifying the original board received as input
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board) # Set the player's move on the board
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]): # Check if all the elements in the first row are the same
        return board[0][0] # Return the element
    elif all(i == board[1][0] for i in board[1]): # Check if all the elements in the second row are the same
        return board[1][0] # Return the element
    elif all(i == board[2][0] for i in board[2]): # Check if all the elements in the third row are the same
        return board[2][0] # Return the element
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]: # Check if the first column is the same
        return board[0][0] # Return the element
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]: # Check if the second column is the same
        return board[0][1] # Return the element
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]: # Check if the third column is the same
        return board[0][2] # Return the element
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]: # Check if the first diagonal is the same
        return board[0][0] # Return the element
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]: # Check if the second diagonal is the same
        return board[0][2] # Return the element
    else: # If there is no winner, return None
        return None # Return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None): # If there is a winner or if there are no empty spaces left
        return True
    else:
        return False # If there is no winner and there are empty spaces left, return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board): # If the board is terminal, return the utility of the board
        if winner(board) == X: # X is the player
            return 1
        elif winner(board) == O: # O is the player
            return -1
        else:
            return 0
    # Check how to handle exception when a non terminal board is received.


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): # If the board is terminal, return the utility of the board
        return None
    else:
        if player(board) == X: # X is the player
            value, move = max_value(board)
            return move
        else: # O is the player
            value, move = min_value(board)
            return move


def max_value(board):
    '''
    Returns the maximum value of the board and the action that leads to it.
    '''
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board): # For each action, get the minimum value of the resulting board
        aux, act = min_value(result(board, action)) # Get the minimum value of the resulting board
        if aux > v: # If the minimum value is greater than the current maximum value, update the maximum value and the action
            v = aux # Update the maximum value
            move = action # Update the action
            if v == 1: # If the maximum value is 1, return the maximum value and the action
                return v, move # Return the maximum value and the action

    return v, move # Return the maximum value and the action


def min_value(board): # Same as max_value, but for the minimum value
    '''
    Returns the minimum value of the board and the action that leads to it.
    '''
    if terminal(board): # If the board is terminal, return the utility of the board
        return utility(board), None # Return the utility of the board

    v = float('inf')
    move = None
    for action in actions(board): # For each action, get the maximum value of the resulting board
        aux, act = max_value(result(board, action))
        if aux < v: # If the maximum value is less than the current minimum value, update the minimum value and the action
            v = aux # Update the minimum value
            move = action # Update the action
            if v == -1: # If the minimum value is -1, return the minimum value and the action
                return v, move # Return the minimum value and the action

    return v, move # Return the minimum value and the action
    