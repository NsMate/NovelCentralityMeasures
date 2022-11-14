import networkx as nx


class ReadGraph:

    def __init__(self, graph_file_name):
        self.file_name = graph_file_name
        self.graph = nx.Graph()

    def read_graph(self):
        self.read_from_mtx()

        return self.graph

    def read_from_mtx(self):
        with open("./networks/"+self.file_name, encoding="utf-8") as file:
            for line in file:
                splitted = line.split(' ')
                if splitted[0].isnumeric():
                    if splitted[0] not in self.graph:
                        self.graph.add_node(splitted[0])
                    if splitted[0].rstrip() == splitted[1].rstrip():
                        print(splitted[0].rstrip())
                        print("fuck")
                    self.graph.add_edge(splitted[0].rstrip(), splitted[1].rstrip())

