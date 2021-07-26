# TODO import the necessary classes and methods
import sys
import logic
import agents
from logic import *
from agents import *
import csp
import search

def readfile(input_file):
    with open(input_file, 'r') as file:
        file_list = [line for line in file]
        board_x = file_list[2][0]
        board_y = file_list[2][2]
        sentences = []
        for i in range(7, len(file_list)):
            if(file_list[i][0] == '#'):
                break;
            sentences.append(file_list[i][:-1])
        queries = []
        for j in range(i+1, len(file_list)):
            queries.append(file_list[j][:-1])
    return int(board_x), int(board_y), sentences, queries

def rules(kb,x,y,sentences):
    kb.tell(expr('B{}{} <=> (M{}{} | M{}{})'.format(0, 0, 0, 1, 1, 0)))
    kb.tell(expr('B{}{} <=> (M{}{} | M{}{})'.format(x-1, y-1, x-1, y-2, x-2, y-1)))
    kb.tell(expr('B{}{} <=> (M{}{} | M{}{})'.format(x-1, 0, x-1, 1, x-2, 0)))
    kb.tell(expr('B{}{} <=> (M{}{} | M{}{})'.format(0, y-1, 0, y-2, 1, y-1)))
    for j in range(1, y-1):
            kb.tell(expr("B{}{} <=> (M{}{} | M{}{} | M{}{})".format(0, j, 0, j+1, 0, j-1, 1, j)))
            kb.tell(expr("B{}{} <=> (M{}{} | M{}{} | M{}{})".format(x-1, j, x-1, j+1, x-1, j-1, x-2, j)))
    for i in range(1, x-1):
            kb.tell(expr("B{}{} <=> (M{}{} | M{}{} | M{}{})".format(i, 0, i, 1, i-1, 0, i+1, 0)))
            kb.tell(expr("B{}{} <=> (M{}{} | M{}{} | M{}{})".format(i, y-1, i, y-2, i-1, y-1, i+1, y-1)))
    for i in range(1,x-1):
        for j in range(1, y-1):
            kb.tell(expr("B{}{} <=> (M{}{} | M{}{} | M{}{} | M{}{}) ".format(i, j, i, j+1, i, j-1, i+1, j, i-1, j)))
    for k in sentences:
        kb.tell(expr(k))
    return kb

if __name__ == '__main__':
    input_file = sys.argv[1]
    x, y, sentences, queries = readfile(input_file)
    minesweeper_kb = PropKB()
    minesweeper_kb = rules(minesweeper_kb, x, y, sentences)
    for z in queries:
        if(minesweeper_kb.ask_if_true(expr(z))):
            print('Yes')
        else:
            print('No')
# TODO implement
