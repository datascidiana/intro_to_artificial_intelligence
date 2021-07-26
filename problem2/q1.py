# TODO import the necessary classes and methods
#from game import TicTacToe
import game
from game import TicTacToe, Game, GameState, alpha_beta_search
import sys

class NewTicTacToe(TicTacToe):
    """Play TicTacToe on an h x v board, with Max (first player) playing 'X'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""

    def __init__(self, h=3, v=3, k=3, board={}, to_move='X', moves={}):
        self.h = h
        self.v = v
        self.k = k
        flag_x = 0
        flag_o = 0
        for key, val in board.items():
            if(val == 'X'):
                x_key = key
                flag_x = 1
            if(val == 'O'):
                o_key = key
                flag_o = 1
            if(flag_o and flag_x):
                break
        utility = 0
        if(not flag_o and flag_x):
            utility = self.compute_utility(board, x_key, 'X')
        elif(not flag_x and flag_o):
            utility = self.compute_utility(board, o_key, 'O')
        elif(flag_x and flag_o):
            x_utility = self.compute_utility(board, x_key, 'X')
            o_utility = self.compute_utility(board, o_key, 'O')
            if(x_utility != 0):
                utility = x_utility
            elif(o_utility != 0):
                utility = o_utility
        self.initial = GameState(to_move=to_move,
                                utility=utility,
                                board=board, moves=moves)

def readfile(input_file):
    with open(input_file, 'r') as file:
        count_x = 0
        count_o = 0
        output = {}
        moves = []
        file_list = [line.split() for line in file]
        k = len(file_list)
        for i in range(len(file_list)):
            for j in range(len(file_list[i])):
                if(file_list[i][j] == 'X'):
                    count_x += 1
                    output[(j+1,i+1)] = 'X'
                elif(file_list[i][j] == 'O'):
                    count_o += 1
                    output[(j+1,i+1)] = 'O'
                else:
                    moves.append((j+1,i+1))
    if(count_o < count_x):
        next_turn = 'O'
    else:
        next_turn = 'X'
    return next_turn, output, moves, k

def play_game(game):
    state = game.initial
    while not game.terminal_test(state):
        player = state.to_move
        move = alpha_beta_search(state, game)
        state = game.result(state, move)
        #print('move: ', move, ' to move: ', player)
    return state

if __name__ == '__main__':

    input_file = sys.argv[1]
    next_turn, initial_board, moves, k = readfile(input_file)
    game = NewTicTacToe(k, k, k, initial_board, next_turn, moves)
    # TODO implement
    utility = play_game(game).utility
    print('Whose turn is it in this state?')
    # TODO: print either X or O
    print(next_turn)
    print('If both X and O play optimally from this state, does X have a guaranteed win, guaranteed loss, or guaranteed draw')
    # TODO: print one of win, loss, draw
    if(utility == 0):
        print('draw')
    elif(utility == 1):
        print('win')
    else:
        print('loss')
