import random
from get_links import get_graph, get_graph_in_pipes
from multiprocessing import Process, SimpleQueue

# start_num_walks is a constant, title is the key of the dictionary, neighbors is the value of the dictionary
def nodeEffort(coupon_count, title, send_pipes, recv_pipes, results_queue, reset_probability):
    #If coupon_count is 0 this node is finished for this round
    if coupon_count == 0:
        for neighbor, pipe in send_pipes:
            pipe.send(0)
        
        new_coupon_cnt = 0
        for neighbor, pipe in recv_pipes:
            new_coupon_cnt += pipe.recv()
            results_queue.put((title, new_coupon_cnt))
        return

    #initializing counts
    new_coupon_cnt = 0
    visit_counts = {}
    for neighbor, pipe in send_pipes:
        visit_counts[neighbor] = 0

    #perform random walks
    for x in range(coupon_count):
        if len(send_pipes) > 0 and random.random() < (1 - reset_probability):
            visit_counts[send_pipes[random.randint(0, len(send_pipes) - 1)][0]] += 1

    #Send num visits to neighbors
    for neighbor, pipe in send_pipes:
        pipe.send(visit_counts[neighbor])

    #receive num visits from neighbors
    for neighbor, pipe in recv_pipes:
        new_coupon_cnt += pipe.recv()

    #submitting result
    results_queue.put((title, new_coupon_cnt))
    

def pagerank(num_rounds, initial_coupon_count, graph, send_pipes, recv_pipes, reset_probability):
	
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
            p = Process(target=nodeEffort, args=(coupon_count[node], node, send_pipes[node], recv_pipes[node], results_queue, reset_probability))
            processes.append(p)
            p.start()

        #Wait for each process to be done
        for p in processes:
            p.join()

        #compute new coupon count and visits
        while not results_queue.empty():
            node, count = results_queue.get()
            coupon_count[node] = count
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
    send_pipes, recv_pipes = get_graph_in_pipes(graph)
    
    print(pagerank(num_rounds, start_num_walks, graph, send_pipes, recv_pipes, reset_probability))


if __name__ == '__main__':
    main()
