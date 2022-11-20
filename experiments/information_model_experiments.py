from centrality_measures.local_fuzzy_information_centrality import LocalFuzzyInformationTechnology
from centrality_measures.local_clustering_h_index import LocalClusteringHIndexCentrality
from utils.read_graph import ReadGraph

import networkx as nx
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc


class InformationModelExperiments:

    def __init__(self):
        self.graph = nx.Graph()
        self.reader = ReadGraph()

    def read_graph_get_starting_nodes(self, graph_name):
        self.graph = self.reader.read_graph(graph_name)

        self.local_hindex = LocalClusteringHIndexCentrality(self.graph)

        self.local_hindex_starting_nodes = self.local_hindex.get_centrality_values()
        self.local_hindex_starting_nodes = sorted(self.local_hindex_starting_nodes.items(), key=lambda x: x[1])
        self.local_hindex_starting_nodes = self.local_hindex_starting_nodes[0:10]
        self.local_hindex_starting_nodes = [node[0] for node in self.local_hindex_starting_nodes]

        self.local_fuzzy = LocalFuzzyInformationTechnology(self.graph)
        """
        self.local_fuzzy_starting_nodes = self.local_fuzzy.get_centrality_values()
        self.local_fuzzy_starting_nodes = sorted(self.local_fuzzy_starting_nodes.items(), key=lambda x: x[1])
        self.local_fuzzy_starting_nodes = self.local_fuzzy_starting_nodes[0:10]
        self.local_fuzzy_starting_nodes = [node[0] for node in self.local_fuzzy_starting_nodes]
        """

    def run_SIR_model_on_starting_nodes(self):
        #Define model
        model = ep.SIModel(self.graph)
        cfg = mc.Configuration()
        cfg.add_model_parameter('beta', 0.01)
        cfg.add_model_parameter('gamma', 0.05)

        cfg.add_model_initial_configuration("Infected", self.local_hindex_starting_nodes)
        model.set_initial_status(cfg)

        hindex_iterations = model.iteration_bunch(200)

        print("Hindex after 50 iterations: " + str(hindex_iterations[50]["node_count"]))

        cfg.add_model_initial_configuration("Infected", self.local_fuzzy_starting_nodes)
        model.set_initial_status(cfg)

        local_fuzzy_iterations = model.iteration_bunch(200)

    def run_threshold_model_on_starting_nodes(self):
        model = ep.ThresholdModel(self.graph)

        config = mc.Configuration()
        config.add_model_initial_configuration("Infected", self.local_hindex_starting_nodes)

        threshold = 0.25
        for i in self.graph.nodes():
            config.add_node_configuration("threshold", i, threshold)

        model.set_initial_status(config)

        hindex_iterations = model.iteration_bunch(200)

        print(hindex_iterations[50]["node_count"])

    def run_cascade_model_on_starting_nodes(self):
        model = ep.IndependentCascadesModel(self.graph)
        config = mc.Configuration()
        config.add_model_initial_configuration("Infected", self.local_hindex_starting_nodes)

        threshold = 0.001
        for i in self.graph.edges():
            config.add_edge_configuration("threshold", i, threshold)

        model.set_initial_status(config)

        hindex_iterations = model.iteration_bunch(400)

        print(hindex_iterations[200]["node_count"])

