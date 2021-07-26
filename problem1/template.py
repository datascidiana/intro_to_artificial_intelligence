from search import ... # TODO import the necessary classes and methods
import sys

if __name__ == '__main__':
	
	input_file = sys.argv[1]
	search_algo_str = sys.argv[2]
	
	# TODO implement
	
	goal_node = ... # TODO call the appropriate search function with appropriate parameters
	
	# Do not change the code below.
	if goal_node is not None:
		print("Solution path", goal_node.solution())
		print("Solution cost", goal_node.path_cost)
	else:
		print("No solution was found.")