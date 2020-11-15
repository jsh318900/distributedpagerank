import random
from get_links import get_graph, get_graph_in_pipes
from multiprocessing import Process, SimpleQueue

# start_num_walks is a constant, title is the key of the dictionary, neighbors is the value of the dictionary
def nodeEffort(start_num_walks, title, neighbors):
    coupon_count = start_num_walks
    visit_count = start_num_walks
    if coupon_count != 0:
        walks_to_neighbors = []
        for x in range(coupon_count):
            if random.random() < (1 - reset_probability):
                walks_to_neighbors[random.randrange(0, len(nodes[i].neighbors))]++
                #at this point, I need to send the walks_to_neighbors data to the neighbors.
    #at this point, I need to receive the received_visits number from neighbors. Then, I need to set coupon_count = received_visits and visit_count += received_visits.
    
                
    
def main():
    # TODO setup GUI
    word = "Albert Einstein"
    start_num_walks = 50 #TODO: this number should be changed to K, which is c*log(number_nodes)
    num_rounds = 50 #TODO: this number should be changed to B*log(number_nodes/reset_probability)
    num_nodes = 50

    graph = get_graph(word, num_nodes)
    send_pipes, recv_pipes = get_graph_in_pipes(graph)
    results_queue = SimpleQueue()
    processes = []
    
    for x in range(num_rounds):
        for node in graph.keys():
            """
            Starts randomwalks on each node
            Each node should put their calculated pagerank in queue in the form of tuple (node_name, pagerank)
            """
            p = Process(target=page_rank_algorithm, args=(node, graph, send_pipes[node], recv_pipes[node], results_queue)) #TODO change arguments to function accordingly
            processes.append(p)
            p.start()


    #Waiting for all processes to finish
    for p in processes:
        p.join()

    """
    TODO find node with greates pagerank value and update GUI
    """Repalced
    while not results_queue.empty():
        print(results_queue.get())
