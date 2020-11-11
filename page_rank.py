import random

def page_rank_algorithm(number_nodes, reset_probability):
    start_walks = 50 #TODO: this number should be changed to K, which is c*log(number_nodes)
    num_rounds = 50 #TODO: this number should be changed to B*log(number_nodes/reset_probability)
    nodes = build_graph(number_nodes, start_walks)
    
    for x in range(num_rounds):
        #TODO split into threads here, one for each node (ideally with each thread holding the index of the node in the nodes list
        i = 0 #TODO: temporary index, should be removed once threads are done)
        if nodes[i].coupon_count != 0:
            walks_to_neighbors = []
            for count in nodes[i].coupon_count:
                if random.random() < (1 - reset_probability):
                    walks_to_neighbors[random.randrange(0, len(nodes[i].neighbors))]++
            #TODO: send walks_to_neighbors info to neighbors using pipes
            received_count = 0 #TODO: receive walks_to_neighbors info from neighbors using pipes here and adds it to received_count
        nodes[i].update_node_counters(received_count)
        
            
#TODO parse through links dictionary here? adjust graph maker? need to add the correct information to the nodes
def build_graph(number_nodes, start_walks):
    nodes = []
    for x in range(number_nodes):
        newNode = node(start_walks, start_walks)
        #newNode.name = 
        #newNode.neighbors = 
        nodes.append(newNode)
    return nodes

    
class node:
    def __init__(self, coupon_count, coupon_count):
        self.coupon_count = coupon_count
        self.visit_count = visit_count
    
    def update_node_counters(received_visits):
        self.coupon_count = received_visits
        self.visit_count += received_visits
        
#    def get_page_rank():
#        return (self.coupon_count/(

