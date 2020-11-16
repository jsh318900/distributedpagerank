import tkinter as tk
from get_links import get_graph, get_graph_in_pipes
from page_rank import pagerank


class GUI:
    def __init__(self, master):
        # Create the main window
        self.master = master
        master.title("Distributed PageRank")
        master.columnconfigure([0, 1, 2], minsize=150)
        master.rowconfigure([0, 1, 2, 3], minsize=50)
        
        # Create a label asking for the title
        self.titleLabel = tk.Label(text="Enter the title of the page: ")
        self.titleLabel.grid(row=0, column=0, padx=15)
         
        self.titleEntry = tk.Entry()
        self.titleEntry.grid(row=0, column=1, sticky='WE', padx=15, columnspan=2)
        
        # Create a label asking for the number of nodes
        self.numNodesLabel = tk.Label(text="Enter the number of nodes: ")
        self.numNodesLabel.grid(row=1, column=0, padx=15)
        
        self.numNodesEntry = tk.Entry()
        self.numNodesEntry.grid(row=1, column=1, sticky='WE', padx=15, columnspan=2)
        
        # Create a text box to display the output
        self.text = tk.Text(height=2, width=50)
        self.text.grid(row=3, column=0, sticky="WE", columnspan=3, rowspan=1, padx=15)
        self.text.insert(tk.INSERT, 'Result will show up here')
        
        # Create a button to start the program
        self.button = tk.Button(text="Run PageRank", command=self.print_result)
        self.button.grid(row=2, column=1)
    
        
    def print_result(self):
        # Input parameters
        title = self.titleEntry.get()
        numNodes = self.numNodesEntry.get()
        start_num_walks = 100   #TODO: this number should be changed to K, which is c*log(number_nodes)
        num_rounds = 50         #TODO: this number should be changed to B*log(number_nodes/reset_probability)
        reset_probability = 0.1
        
        # Run the algorithm
        graph = get_graph(title, int(numNodes))
        send_pipes, recv_pipes = get_graph_in_pipes(graph)
        max_node = pagerank(num_rounds, start_num_walks, graph, send_pipes, recv_pipes, reset_probability)
        
        # Display the results
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, max_node)
        self.text.config(state=tk.DISABLED)


def main():
    window = tk.Tk()
    GUI(window)
    window.mainloop()
    
if __name__ == "__main__":
    main()