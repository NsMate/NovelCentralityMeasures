import networkx as nx


class ReadGraph:

    def __init__(self):
        self.graph = nx.Graph()

    def read_graph(self, network_name):
        self.read_from_mtx(network_name)

        return self.graph

    def read_from_mtx(self, network_name):
        self.graph = nx.Graph()
        with open("./networks/"+network_name, encoding="utf-8") as file:
            for line in file:
                splitted = line.split(' ')
                if splitted[0].isnumeric():
                    if splitted[0] not in self.graph:
                        self.graph.add_node(int(splitted[0].rstrip()))
                    elif splitted[1] not in self.graph:
                        self.graph.add_node(int(splitted[1].rstrip()))
                    if int(splitted[0].rstrip()) != int(splitted[1].rstrip()):
                        self.graph.add_edge(int(splitted[0].rstrip()), int(splitted[1].rstrip()))

