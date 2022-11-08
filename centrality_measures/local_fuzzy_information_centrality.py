import math
from itertools import combinations, groupby
import networkx as nx
import random


class LocalFuzzyInformationTechnology:

    def __init__(self):
        # Network Definition
        self.g = self.gnp_random_connected_graph(40, 0.0001)

    def find_maximum_shortest_path(self, source):
        path_lengths = nx.shortest_path_length(self.g, source=source)

        return math.floor(path_lengths.get(next(reversed(path_lengths))) / 2)

    def classify_nodes_from_center(self, source):
        max_class = self.find_maximum_shortest_path(2)
        path_lengths = nx.shortest_path_length(self.g, source=source)

        for k, v in path_lengths.items():
            if v <= max_class:
                self.g.nodes[k]["class"] = v

    def gnp_random_connected_graph(self, n, p):
        """
        Generates a random undirected graph, similarly to an Erdős-Rényi
        graph, but enforcing that the resulting graph is conneted
        """
        edges = combinations(range(n), 2)
        G = nx.Graph()
        G.add_nodes_from(range(n))
        if p <= 0:
            return G
        if p >= 1:
            return nx.complete_graph(n, create_using=G)
        for _, node_edges in groupby(edges, key=lambda x: x[0]):
            node_edges = list(node_edges)
            random_edge = random.choice(node_edges)
            G.add_edge(*random_edge)
            for e in node_edges:
                if random.random() < p:
                    G.add_edge(*e)
        return G

