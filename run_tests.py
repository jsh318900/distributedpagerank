
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
	x_axis = [10, 50, 100, 150, 200]
	y_axis = []
	
	for round in x_axis:
		graph = get_graph(word, 100)
		send_pipes, recv_pipes = get_graph_in_pipes(graph)
		init_time = time()
		pagerank(round, init_num_walks, graph, send_pipes, recv_pipes, reset_probability)
		y_axis.append(time() - init_time)
		
		#finishing up connections for next test
		for node in send_pipes:
			for neighbor in send_pipes[node]:
				neighbor[1].close()
		for node in recv_pipes:
			for neighbor in recv_pipes[node]:
				neighbor[1].close()

	plt.xlabel("number of rounds")
	plt.ylabel("time in seconds")
	plt.plot(x_axis, y_axis)
	plt.axis([0, 200, 0, (int(y_axis[4] / 10) + 1) * 10])
	plt.savefig('test1.png')

	#Test 2, number of nodes v.s. time
	#Fix number of rounds to 100

	print("Running Test 2")
	x_axis = [10, 50, 100, 150, 200]
	y_axis = []
	num_rounds = 100

	for num_nodes in x_axis:
		graph = get_graph(word, num_nodes)
		send_pipes, recv_pipes = get_graph_in_pipes(graph)
		init_num_walks = int(m.log(num_nodes))
		init_time = time()
		pagerank(num_rounds, init_num_walks, graph, send_pipes, recv_pipes, reset_probability)
		y_axis.append(time() - init_time)

		#finishing up connections for next test
		for node in send_pipes:
			for neighbor in send_pipes[node]:
				neighbor[1].close()
		for node in recv_pipes:
			for neighbor in recv_pipes[node]:
				neighbor[1].close()


	plt.xlabel("number of nodes")
	plt.ylabel("time in seconds")
	plt.plot(x_axis, y_axis)
	plt.axis([0, 200, 0, (int(y_axis[4] / 10) + 1) * 10])
	plt.savefig('test2.png')

	print("Tests done")