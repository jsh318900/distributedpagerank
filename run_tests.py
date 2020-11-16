
import math as m
from page_rank import pagerank
from get_links import get_graph, get_graph_in_pipes
from time import time
import matplotlib.pyplot as plt


if __name__ == '__main__':
	# Initializing constants
	word = "Parallel computing"

	reset_probability = 0.05

	#Test 1, number of rounds v.s. time
	#Fix number of nodes to 100

	print("Running Test 1")

	init_num_walks = int(m.log(100))
	x_axis = [100, 150, 200, 300, 400, 500]
	y_axis = []
	graph = get_graph(word, 100)

	
	for round in x_axis:
		init_time = time()
		pagerank(round, init_num_walks, graph, reset_probability)
		y_axis.append(time() - init_time)
		
	for i in range(len(y_axis)):
		y_axis[i] *= 1e3

	plt.xlabel("number of rounds")
	plt.ylabel("time in milliseconds")
	plt.plot(x_axis, y_axis)
	plt.axis([0, 500, 0, y_axis[4]])
	plt.savefig('test1.png')

	#Test 2, number of nodes v.s. time
	#Fix number of rounds to 100

	print("Running Test 2")
	x_axis = [100, 150, 200, 300, 500]
	y_axis = []
	num_rounds = 100

	for num_nodes in x_axis:
		graph = get_graph(word, num_nodes)
		init_num_walks = int(m.log(num_nodes))
		init_time = time()
		pagerank(num_rounds, init_num_walks, graph, reset_probability)
		y_axis.append(time() - init_time)

	for i in range(len(y_axis)):
		y_axis[i] *= 1e3

	plt.xlabel("number of nodes")
	plt.ylabel("time in miliseconds")
	plt.plot(x_axis, y_axis)
	plt.axis([0, 200, 0, y_axis[4] * 1e3])
	plt.savefig('test2.png')

	print("Tests done")