import random
from get_links import get_graph, get_graph_in_pipes
from multiprocessing import Process, SimpleQueue

# start_num_walks is a constant, title is the key of the dictionary, neighbors is the value of the dictionary
def nodeEffort(coupon_count, title, neighbors, results_queue, reset_probability):
    #If coupon_count is 0 this node is finished for this round
    if coupon_count == 0:
        return

    #initializing counts
    new_coupon_cnt = 0
    visit_counts = {}
    for neighbor in neighbors:
        visit_counts[neighbor] = 0

    #perform random walks
    for x in range(coupon_count):
        if len(neighbors) > 0 and random.random() < (1 - reset_probability):
            visit_counts[neighbors[random.randint(0, len(neighbors) - 1)]] += 1

    for neighbor in neighbors:
        results_queue.put((neighbor, visit_counts[neighbor]))
    

def pagerank(num_rounds, initial_coupon_count, graph, reset_probability):
	
	# Initial Setup
    coupon_count = {}
    num_visits = {}
    for node in graph.keys():
        coupon_count[node] = initial_coupon_count
        num_visits[node] = initial_coupon_count


	#Outer loop for each round
    while num_rounds > 0:
		#Parallel process
        processes = []
        results_queue = SimpleQueue()
        for node in graph.keys():
            if node in coupon_count and coupon_count[node] > 0:
                p = Process(target=nodeEffort, args=(coupon_count[node], node, graph[node], results_queue, reset_probability))
                processes.append(p)
                p.start()

        #Wait for each process to be done
        for p in processes:
            p.join()

        #reset coupon count for each node
        for node in coupon_count.keys():
            coupon_count[node] = 0

        #compute new coupon count and visits
        while not results_queue.empty():
            node, count = results_queue.get()
            if node not in coupon_count:
                coupon_count[node] = 0
            if node not in num_visits:
                num_visits[node] = 0

            coupon_count[node] += count
            num_visits[node] += count
        
        num_rounds -= 1
        print(num_rounds)

    max_node = None
    max_visits = -1
    for node in num_visits.keys():
        if max_visits < num_visits[node]:
            max_node = node
            max_visits = num_visits[node]

    return max_node


                
    
def main():
    # TODO setup GUI
    # Constants
    word = "Computational complexity"
    start_num_walks = 100 #TODO: this number should be changed to K, which is c*log(number_nodes)
    num_rounds = 100 #TODO: this number should be changed to B*log(number_nodes/reset_probability)
    num_nodes = 100
    reset_probability = 0.05

    graph = get_graph(word, num_nodes)
    
    print(pagerank(num_rounds, start_num_walks, graph, reset_probability))


if __name__ == '__main__':
    main()
