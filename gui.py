import tkinter as tk
import requests

# Function to check the GUI works by printing out the graph
def print_graph():
    title = titleEntry.get()
    numNodes = numNodesEntry.get()
    graph = get_graph(title, int(numNodes))
    text.config(state=tk.NORMAL)
    text.delete(1.0, tk.END)
    text.insert(tk.END, graph)
    text.config(state=tk.DISABLED)
    
    
def get_graph(word, node_number):
    S = requests.Session()
    graph = {}
    URL = "https://en.wikipedia.org/w/api.php"
    relate=set()
    relate.add(word)

    count=0
    while(len(graph)<node_number):
        if len(relate)>0:
            w=relate.pop()

        else:
            return graph
        if w not in graph:
            graph[w]=[]
            PARAMS = {
                "action": "query",
                "format": "json",
                "titles": w,
                "prop": "links"
            }

            R = S.get(url=URL, params=PARAMS)
            DATA = R.json()

            PAGES = DATA["query"]["pages"]
            for k, v in PAGES.items():
                if "links" in v:

                    for l in v["links"]:
                        if l["title"] in relate or l["title"] in graph:
                            count=count+1

                        graph[w].append(l["title"])
                        relate.add(l["title"])
                        if count>=node_number:
                            print(graph)
                            return graph

    print(graph)
    return graph


# Create the main window
window = tk.Tk()
window.title("Distributed PageRank")
window.columnconfigure([0, 1, 2], minsize=150)
window.rowconfigure([0, 1, 2, 3], minsize=50)

# Create a label asking for the title
titleLabel = tk.Label(text="Enter the title of the page: ")
titleLabel.grid(row=0, column=0)
 
titleEntry = tk.Entry()
titleEntry.grid(row=0, column=1, sticky='WE', padx=15, columnspan=2)

# Create a label asking for the number of nodes
numNodesLabel = tk.Label(text="Enter the number of nodes: ")
numNodesLabel.grid(row=1, column=0)

numNodesEntry = tk.Entry()
numNodesEntry.grid(row=1, column=1, sticky='WE', padx=15, columnspan=2)

# Create a button to start the program
button = tk.Button(text="Start", command=print_graph)
button.grid(row=2, column=1)

# Create a text box to display the output
textframe = tk.Frame(master=window)
textframe.grid(row=3, column=0, sticky="WE", columnspan=3)
text = tk.Text(master=textframe, wrap=tk.WORD)
text.pack()
text.insert(tk.END, 'Results will show up here')

window.mainloop()