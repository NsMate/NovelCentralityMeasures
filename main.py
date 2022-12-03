from itertools import combinations, groupby
from centrality_measures.local_clustering_h_index import LocalClusteringHIndexCentrality
from centrality_measures.global_structure_model import GlobalStructureModel
from centrality_measures.local_fuzzy_information_centrality import LocalFuzzyInformationTechnology
from experiments.common_experiments import CommonExperiments
from experiments.information_model_experiments import InformationModelExperiments
from utils.read_graph import ReadGraph

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
    #graph = gnp_random_connected_graph(45, 0.00001)
    reader = ReadGraph()
    graph = reader.read_graph("toy_network_gsm")

    exp = GlobalStructureModel(graph)

