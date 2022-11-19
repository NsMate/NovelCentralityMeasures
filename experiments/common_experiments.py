from utils.read_graph import ReadGraph
from centrality_measures.local_fuzzy_information_centrality import LocalFuzzyInformationTechnology
from centrality_measures.local_clustering_h_index import LocalClusteringHIndexCentrality

import networkx as nx


class CommonExperiments:

    def __init__(self):
        self.reader = ReadGraph()
        self.graph = nx.Graph()

    def read_graph(self, graph_name):
        self.graph = self.reader.read_graph(graph_name)

        self.local_hindex = LocalClusteringHIndexCentrality(self.graph)
        self.local_fuzzy = LocalFuzzyInformationTechnology(self.graph)

    def get_centralities(self):
        hindex_values = self.local_hindex.get_centrality_values()
        hindex_values = sorted(hindex_values.items(), key=lambda x: x[1], reverse=True)

        print("Best local clustering h index nodes on graph: ")
        for i in range(0, 5):
            print(str(hindex_values[i][0]) + ": " + str(hindex_values[i][1]))

        local_fuzzy_values = self.local_fuzzy.get_centrality_values()
        local_fuzzy_values = sorted(local_fuzzy_values.items(), key=lambda x: x[1], reverse=True)

        print("Best local fuzzy information centrality nodes on graph: ")
        for i in range(0, 5):
            print(str(local_fuzzy_values[i][0]) + ": " + str(local_fuzzy_values[i][1]))

        degree_centrality_values = nx.degree_centrality(self.graph)
        degree_centrality_values = sorted(degree_centrality_values.items(), key=lambda x: x[1], reverse=True)

        print("Best degree centrality nodes on graph: ")
        for i in range(0, 5):
            print(str(degree_centrality_values[i][0]) + ": " + str(degree_centrality_values[i][1]))

        closeness_centrality = nx.closeness_centrality(self.graph)
        closeness_centrality = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)

        print("Best closeness centrality nodes on graph: ")
        for i in range(0, 5):
            print(str(closeness_centrality[i][0]) + ": " + str(closeness_centrality[i][1]))

