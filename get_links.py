import requests


def get_graph(word, node_number):
    S = requests.Session()
    graph = {}
    # while len(graph)<node_number:

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



get_graph("Albert Einstein",50)
