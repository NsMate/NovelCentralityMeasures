from itertools import combinations, groupby
from experiments.lfic_experiments import LficExperiments

import networkx as nx
import random


def gnp_random_connected_graph(n, p):
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


if __name__ == '__main__':
    #graph = gnp_random_connected_graph(45, 0.0001)

    #local_fuzzy = LocalFuzzyInformationTechnology(graph)

    lfic_experiments = LficExperiments("tech-WHOIS.mtx")

    lfic_experiments.read_in_graph()
    lfic_experiments.calculate_node_centralities()

