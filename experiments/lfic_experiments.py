from centrality_measures.local_fuzzy_information_centrality import LocalFuzzyInformationTechnology
from utils.read_graph import ReadGraph

import ndlib as nd
import networkx as nx


class LficExperiments:

    def __init__(self, network_name):
        self.graph = nx.Graph()
        self.reader = ReadGraph(network_name)

        self.top_nodes = dict()

    def read_in_graph(self):
        self.graph = self.reader.read_graph()

        print(self.graph.number_of_nodes())

        self.lfic = LocalFuzzyInformationTechnology(self.graph)

    def calculate_node_centralities(self):
        self.top_nodes = self.lfic.check()
