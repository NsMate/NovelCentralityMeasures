from itertools import combinations, groupby

from experiments.centrality_frequency import CentralityFrequency
from experiments.spread_experiment import SpreadExperiment
from experiments.coverage_experiment import CoverageExperiment

import networkx as nx
import random
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc


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

    spread = SpreadExperiment()
    spread.threshold_model_spread()
    """
    # Network topology
    g = nx.erdos_renyi_graph(1000, 0.1)

    # Model selection
    model = ep.IndependentCascadesModel(g)

    # Model Configuration
    config = mc.Configuration()
    config.add_model_parameter('fraction_infected', 0.01)

    # Setting the edge parameters
    threshold = 0.01
    for e in g.edges():
        config.add_edge_configuration("threshold", e, threshold)

    model.set_initial_status(config)

    # Simulation execution
    iterations = model.iteration_bunch(3)

    print("Susceptible " + str(iterations[-1]["node_count"][0]))
    print("Infected " + str(iterations[-1]["node_count"][1]))
    print("Removed " + str(iterations[-1]["node_count"][2]))
    
    for i in range(0, 50, 1):

        # Network topology
        g = nx.erdos_renyi_graph(1000, 0.1)

        # Model selection
        model = ep.ThresholdModel(g)

        # Model Configuration
        config = mc.Configuration()
        config.add_model_parameter('fraction_infected', 0.01)

        # Setting node parameters
        threshold = 0.045
        for node in g.nodes():
            config.add_node_configuration("threshold", node, threshold)

        model.set_initial_status(config)

        # Simulation execution
        iterations_thr = model.iteration_bunch(5)

        print("Susceptible " + str(iterations_thr[-1]["node_count"][0]))
        print("Infected " + str(iterations_thr[-1]["node_count"][1]))
        #print("Removed " + str(iterations[-1]["node_count"][2]))
        """

