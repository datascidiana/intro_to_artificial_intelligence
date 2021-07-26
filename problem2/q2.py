# TODO import the necessary classes and methods
import sys
import q1
from q1 import NewTicTacToe, readfile
import utils
import game
from game import GameState, minmax_decision
import copy
import itertools
import random
from collections import namedtuple
import numpy as np

win = 0
draw = 0
loss = 0
non_terminal = 1
g_win = 0
g_loss = 0
g_draw = 0

def minmax_decision_x(state, game):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states. [Figure 5.3]"""
    global win
    global draw
    global loss
    global non_terminal
    global g_win
    global g_loss
    global g_draw
    player = game.to_move(state)

    def max_value(state):
        global win
        global draw
        global loss
        global non_terminal
        global g_win
        global g_loss
        global g_draw
        if game.terminal_test(state):
            if(game.utility(state, player) == 1):
                win += 1
            elif(game.utility(state, player) == -1):
                loss += 1
            else:
                draw += 1
            return game.utility(state, player)
        non_terminal += 1
        v = -np.inf
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a)))
        if(v == 1):
            g_win += 1
        elif(v == -1):
            g_loss += 1
        else:
            g_draw += 1
        return v

    def min_value(state):
        global win
        global draw
        global loss
        global non_terminal
        global g_win
        global g_loss
        global g_draw
        if game.terminal_test(state):
            if(game.utility(state, player) == 1):
                win += 1
            elif(game.utility(state, player) == -1):
                loss += 1
            else:
                draw += 1
            return game.utility(state, player)
        non_terminal += 1
        v = np.inf
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a)))
        if(v == 1):
            g_win += 1
        elif(v == -1):
            g_loss += 1
        else:
            g_draw += 1
        return v

    # Body of minmax_decision:
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a)))

def play_game(game):
    state = game.initial
    while not game.terminal_test(state):
        player = state.to_move
        move = minmax_decision(state, game)
        state = game.result(state, move)
        #print('move: ', move, ' to move: ', player)
    return state

if __name__ == '__main__':

    input_file = sys.argv[1]
    next_turn, initial_board, moves, k = readfile(input_file)
    game = NewTicTacToe(k, k, k, initial_board, next_turn, moves)
    # TODO implement
    #play_game(game)
    state = game.initial
    player = state.to_move
    move = minmax_decision_x(state, game)
    utility = play_game(game).utility
    if(player == 'O'):
        win, loss = loss, win
        g_win, g_loss = g_loss, g_win
    if(utility == 0):
        g_draw += 1
    elif(utility == 1):
        g_win += 1
    else:
        g_loss += 1
    # TODO implement
    # Starting from this state, populate the full game tree.
    # The leaf nodes are the terminal states.
    # The terminal state is terminal if a player wins or there are no empty squares.
    # If a player wins, the state is considered terminal, even if there are still empty squares.
    # Answer the following questions for this game tree.
    print('How many terminal states are there?')
    # TODO print the answer
    print(win+loss+draw)
    print('In how many of those terminal states does X win?')
    # TODO print the answer
    print(win)
    print('In how many of those terminal states does X lose?')
    # TODO print the answer
    print(loss)
    print('In how many of those terminal states does X draw?')
    # TODO print the answer
    print(draw)
    print('How many non-terminal states are there?')
    # TODO print the answer
    print(non_terminal)
    print('In how many of those non-terminal states does X have a guranteed win?')
    # TODO print the answer
    print(g_win)
    print('In how many of those non-terminal states does X have a guranteed loss?')
    # TODO print the answer
    print(g_loss)
    print('In how many of those non-terminal states does X have a guranteed draw?')
    # TODO print the answer
    print(g_draw)
