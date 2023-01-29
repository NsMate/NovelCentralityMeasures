from centrality_measures.local_fuzzy_information_centrality import LocalFuzzyInformationTechnology
from centrality_measures.local_clustering_h_index import LocalClusteringHIndexCentrality
from centrality_measures.global_structure_model import GlobalStructureModel
from centrality_measures.basic_centrality_measures import BasicCentralityMeasures

from utils.read_graph import ReadGraph

import networkx as nx


class CentralityFrequency:

    def __init__(self):
        self.reader = ReadGraph()
        self.graphs = ["high_degree.mtx", "low_degree.mtx", "high_kcore.mtx", "low_kcore.mtx", "high_triangle.mtx",
                       "low_triangle.mtx"]

    def local_fuzzy_frequencies(self):
        print("Local Fuzzy Centrality measures: \n")

        file = open('results/frequency_results/local_fuzzy_eredmények', 'w', encoding='utf-8')
        file.write("local fuzzy centrality eredmények: \n")

        for graph in self.graphs:
            centrality_frequencies = dict()
            local_fuzzy = LocalFuzzyInformationTechnology()
            read_graph = self.reader.read_graph(graph)
            local_fuzzy.set_graph(read_graph)

            centralities = local_fuzzy.get_centrality_values()

            centralities_copy = sorted(centralities.items(), key=lambda x: x[1], reverse=True)
            for i in range(10):
                file.write(str(centralities_copy[i]) + "\n")
            file.write("\n")

            for k,v in centralities.items():
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[1], reverse=True)
            print(str(graph) + ":")
            i = 0
            while i < 10 and i < len(centrality_frequencies):
                print(str(centrality_frequencies[i][0]) + ": " + str(centrality_frequencies[i][1]))
                i += 1

        file.close()

    def local_h_cluster_frequencies(self):
        local_h = LocalClusteringHIndexCentrality()
        print("Local H CLuster measures: \n")

        file = open('results/frequency_results/local_h_eredmények', 'w', encoding='utf-8')
        file.write("local h index eredmények: \n")
        for graph in self.graphs:
            centrality_frequencies = dict()
            file.write(str(graph) + "\n")
            read_graph = self.reader.read_graph(graph)
            local_h.set_graph(read_graph)

            centralities = local_h.get_centrality_values()
            centralities_copy = sorted(centralities.items(), key=lambda x: x[1], reverse=True)
            for i in range(10):
                file.write(str(centralities_copy[i]) + "\n")
            file.write("\n")

            for k, v in centralities.items():
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[1], reverse=True)
            print(str(graph) + ":")
            i = 0
            while i < 10 and i < len(centrality_frequencies):
                print(str(centrality_frequencies[i][0]) + ": " + str(centrality_frequencies[i][1]))
                i += 1

        file.close()

    def global_structure_model_frequencies(self):
        global_structure = GlobalStructureModel()
        print("Global Structure Model measures: \n")

        file = open('results/frequency_results/global_structure_eredmények', 'w', encoding='utf-8')
        file.write("global structure model eredmények: \n")

        for graph in self.graphs:
            centrality_frequencies = dict()
            file.write(str(graph) + "\n")
            read_graph = self.reader.read_graph(graph)
            global_structure.set_graph(read_graph)

            centralities = global_structure.get_centrality_values()

            centralities_copy = sorted(centralities.items(), key=lambda x: x[1], reverse=True)
            for i in range(10):
                file.write(str(centralities_copy[i]) + "\n")
            file.write("\n")

            for k, v in centralities.items():
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[1], reverse=True)
            print(str(graph) + ":")
            i = 0
            while i < 10 and i < len(centrality_frequencies):
                print(str(centrality_frequencies[i][0]) + ": " + str(centrality_frequencies[i][1]))
                i += 1

        file.close()

    def basic_centrality_frequencies(self):
        print("Bacic centrality measures: ")

        file = open('results/frequency_results/basic_centrality_eredmények', 'w', encoding='utf-8')

        for graph in self.graphs:
            centrality_frequencies = dict()
            basic_centrality = BasicCentralityMeasures(nx.Graph())
            read_graph = self.reader.read_graph(graph)

            basic_centrality.set_graph(read_graph)

            centralities_degree = basic_centrality.get_degree_centrality_values()
            centralities_between = basic_centrality.get_betweenness_centrality()

            file.write(str(graph) + " : degree \n")
            centralities_degree_copy = sorted(centralities_degree.items(), key=lambda x: x[1], reverse=True)
            for i in range(10):
                file.write(str(centralities_degree_copy[i]) + "\n")
            file.write("\n")

            file.write(str(graph) + " : betweenness")
            centralities_between_copy = sorted(centralities_between.items(), key=lambda x: x[1], reverse=True)
            for i in range(10):
                file.write(str(centralities_between_copy[i]) + "\n")
            file.write("\n")

            for k, v in centralities_degree.items():
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[1], reverse=True)
            print("Degree Centrality measures: " + str(graph) + " \n")
            i = 0
            while i < 10 and i < len(centrality_frequencies):
                print(str(centrality_frequencies[i][0]) + ": " + str(centrality_frequencies[i][1]))
                i += 1

            centrality_frequencies = dict()

            for k, v in centralities_between.items():
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[1], reverse=True)
            print("Betweenness Centrality measures: " + str(graph) + " \n")
            i = 0
            while i < 10 and i < len(centrality_frequencies):
                print(str(centrality_frequencies[i][0]) + ": " + str(centrality_frequencies[i][1]))
                i += 1

        file.close()

