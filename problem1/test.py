import sys


def readfile(input_file):
    graph = {}
    heuristic = {}
    i = 0

    with open(input_file, 'r') as file:
        #the file read as a list split on misplaced
        file_list = [line.split() for line in file]
        #skipping the comments
        while(file_list[i][0] == '#'):
            i += 1
        #making the graph
        while(file_list[i][0] != '#'):
            if(file_list[i][2] == '<>'):
                if(graph.get(file_list[i][1], -1) == -1):
                    graph[file_list[i][1]] = {}
                graph[file_list[i][1]][file_list[i][0]] = file_list[i][3]
            if(graph.get(file_list[i][0], -1) == -1):
                graph[file_list[i][0]] = {}
            graph[file_list[i][0]][file_list[i][1]] = file_list[i][3]
            i += 1
        #start and goal
        start = file_list[i+1][0]
        goal = file_list[i+1][1]
        #heuristics
        heuristic = {h[0]:h[1] for h in file_list[i+3:]}

    return start, goal, graph, heuristic

if __name__ == '__main__':

    input_file = sys.argv[1]
    search_algo_str = sys.argv[2]

    start, goal, graph, heuristic = readfile(input_file)
    print('start = ', start)
    print('goal = ', goal)
    print('graph \n', graph)
    print('heuristic \n', heuristic)
