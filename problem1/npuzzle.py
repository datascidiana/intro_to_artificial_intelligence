import search
from search import Problem, GraphProblem
import sys

class NPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, goal, n):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)
        self.n = n

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % self.n == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < self.n:
            possible_actions.remove('UP')
        if index_blank_square % self.n == self.n-1:
            possible_actions.remove('RIGHT')
        if index_blank_square >= ((self.n)**2)-self.n:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -self.n, 'DOWN': self.n, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


def readfile(input_file):
    with open(input_file, 'r') as file:
        file_list = [line.split() for line in file]
        file_list = file_list[3:]
        n = len(file_list[0])
        initial = []
        for i in range(len(file_list)):
            for j in range(len(file_list[i])):
                initial.append(int(file_list[i][j]))
        goal = []
        for i in range(n**2):
            goal.append(i)
        return tuple(initial), tuple(goal), n

def UCTS(problem):
    f = lambda node: node.path_cost
    node = search.Node(problem.initial)
    frontier = search.PriorityQueue('min', f)
    frontier.append(node)
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

def ASTS(problem):
    f = lambda node: problem.h(node) + node.path_cost
    node = search.Node(problem.initial)
    frontier = search.PriorityQueue('min', f)
    frontier.append(node)
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

def GBFTS(problem):
    f = lambda node: problem.h(node)
    node = search.Node(problem.initial)
    frontier = search.PriorityQueue('min', f)
    frontier.append(node)
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

def GBFGS(problem):
    return search.best_first_graph_search(problem, problem.h)

if __name__ == '__main__':

    input_file = sys.argv[1]
    search_algo_str = sys.argv[2]
    algo_dict = {
        'DFTS': getattr(search, 'depth_first_tree_search'),
        'DFGS': getattr(search, 'depth_first_graph_search'),
        'BFTS': getattr(search, 'breadth_first_tree_search'),
        'BFGS': getattr(search, 'breadth_first_graph_search'),
        'GBFGS': GBFGS,
        'ASGS': getattr(search, 'astar_search'),
        'UCTS': UCTS,
        'UCGS': getattr(search, 'uniform_cost_search'),
        'ASTS': ASTS,
        'GBFTS': GBFTS
        }
    initial, goal, n = readfile(input_file)
    problem  = NPuzzle(initial, goal, n)
    method_to_call = algo_dict.get(search_algo_str)
    goal_node = method_to_call(problem)

    # Do not change the code below.
    if goal_node is not None:
        print("Solution path", goal_node.solution())
        print("Solution cost", goal_node.path_cost)
    else:
        print("No solution was found.")
