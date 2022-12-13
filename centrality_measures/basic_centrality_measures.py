import networkx as nx


class BasicCentralityMeasures:

    def __init__(self, graph):
        self.graph = graph

    def set_graph(self, graph):
        self.graph = graph

    def get_degree_centrality_values(self):
        return nx.degree_centrality(self.graph)

    def get_betweenness_centrality(self):
        return nx.betweenness_centrality(self.graph)

