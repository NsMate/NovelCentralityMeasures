import time

from centrality_measures.local_fuzzy_information_centrality import LocalFuzzyInformationTechnology
from centrality_measures.local_clustering_h_index import LocalClusteringHIndexCentrality
from centrality_measures.global_structure_model import GlobalStructureModel
from centrality_measures.basic_centrality_measures import BasicCentralityMeasures

from utils.read_graph import ReadGraph

import networkx as nx


class CentralityFrequency:

    def __init__(self):
        self.reader = ReadGraph()
        self.graphs = ["high_kcore.mtx", "low_kcore.mtx",
                       "low_triangle.mtx"]
        #self.graphs = ["high_degree.mtx", "low_degree.mtx", "high_triangle.mtx"]

    def local_fuzzy_frequencies(self):
        #print("Local Fuzzy Centrality measures: \n")

        #file = open('results/frequency_results/local_fuzzy_eredmények', 'w', encoding='utf-8')
        #file.write("local fuzzy centrality eredmények: \n")
        #centrality_file = open('results/centrality_values/local_fuzzy_eredmeny', 'w', encoding='utf-8')
        #centrality_file.write("local fuzzy eredmények: \n\n")

        for graph in self.graphs:
            centrality_frequencies = dict()
            local_fuzzy = LocalFuzzyInformationTechnology()
            read_graph = self.reader.read_graph(graph)
            local_fuzzy.set_graph(read_graph)

            start = time.time()
            centralities = local_fuzzy.get_centrality_values()
            print("LF " + str(graph) + " " + str(time.time() - start))

            """
            centralities_copy = sorted(centralities.items(), key=lambda x: x[1], reverse=True)

            #centrality_file.write(str(graph) + ": \n\n")
            for k, v in centralities_copy:
                #centrality_file.write(str(k) + " : " + str(v) + "\n")
                v = round(v, 3)
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[0], reverse=True)
            file.write(str(graph) + " : \n\n")
            for k, v in centrality_frequencies:
                file.write(str(k) + " : " + str(v) + "\n")

        file.close()
        #centrality_file.close()
        """

    def local_h_cluster_frequencies(self):
        local_h = LocalClusteringHIndexCentrality()
        #print("Local H CLuster measures: \n")

        #file = open('results/frequency_results/local_h_eredmények', 'w', encoding='utf-8')
        #file.write("local h index eredmények: \n")
        #centrality_file = open('results/centrality_values/local_h_eredmeny', 'w', encoding='utf-8')
        #centrality_file.write("local h eredmények: \n\n")

        for graph in self.graphs:
            centrality_frequencies = dict()
            read_graph = self.reader.read_graph(graph)
            local_h.set_graph(read_graph)

            start = time.time()
            centralities = local_h.get_centrality_values()
            print("Local_H " + str(graph) + " " + str(time.time() - start))

            """
            centralities_copy = sorted(centralities.items(), key=lambda x: x[1], reverse=True)

            #centrality_file.write(str(graph) + ": \n\n")
            for k, v in centralities_copy:
                #centrality_file.write(str(k) + " : " + str(v) + "\n")
                v = round(v, 3)
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[0], reverse=True)
            file.write(str(graph) + " : \n\n")
            for k, v in centrality_frequencies:
                file.write(str(k) + " : " + str(v) + "\n")

        file.close()
        #centrality_file.close()
        """

    def global_structure_model_frequencies(self):
        global_structure = GlobalStructureModel()
        #print("Global Structure Model measures: \n")

        #file = open('results/frequency_results/global_structure_eredmények', 'w', encoding='utf-8')
        #file.write("global structure model eredmények: \n")
        #centrality_file = open('results/centrality_values/global_structure_eredmeny', 'w', encoding='utf-8')
        #centrality_file.write("global structure model eredmények: \n\n")

        for graph in self.graphs:
            centrality_frequencies = dict()
            read_graph = self.reader.read_graph(graph)
            global_structure.set_graph(read_graph)
            start = time.time()
            centralities = global_structure.get_centrality_values()
            print("GSM " + str(graph) + " " + str(time.time() - start))
            """
            centralities_copy = sorted(centralities.items(), key=lambda x: x[1], reverse=True)

            #centrality_file.write(str(graph) + ": \n\n")
            for k, v in centralities_copy:
                #centrality_file.write(str(k) + " : " + str(v) + "\n")
                v = round(v, 3)
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[0], reverse=True)
            file.write(str(graph) + " : \n\n")
            for k, v in centrality_frequencies:
                file.write(str(k) + " : " + str(v) + "\n")

        file.close()
        #centrality_file.close()
        """

    def basic_centrality_frequencies(self):
        #print("Bacic centrality measures: ")

        #file = open('results/frequency_results/basic_centrality_eredmények', 'w', encoding='utf-8')
        #file.write("basic model eredmények: \n\n")
        #centrality_file = open('results/centrality_values/basic_eredmeny', 'w', encoding='utf-8')
        #centrality_file.write("basic model eredmények: \n\n")

        for graph in self.graphs:
            centrality_frequencies = dict()
            basic_centrality = BasicCentralityMeasures(nx.Graph())
            read_graph = self.reader.read_graph(graph)

            basic_centrality.set_graph(read_graph)

            start = time.time()
            centralities_degree = basic_centrality.get_degree_centrality_values()
            print("DC " + str(graph) + " " + str(time.time() - start))
            """
            centralities_copy = sorted(centralities_degree.items(), key=lambda x: x[1], reverse=True)

            #centrality_file.write(str(graph) + "(degree): \n\n")
            for k, v in centralities_copy:
                #centrality_file.write(str(k) + " : " + str(v) + "\n")
                v = round(v, 3)
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[0], reverse=True)
            file.write(str(graph) + " : \n\n")
            for k, v in centrality_frequencies:
                file.write(str(k) + " : " + str(v) + "\n")
            
            centrality_frequencies = dict()
            """
            start = time.time()
            centralities_between = basic_centrality.get_betweenness_centrality()
            print("BC " + str(graph) + " " + str(time.time() - start))
            """
            centralities_copy = sorted(centralities_between.items(), key=lambda x: x[1], reverse=True)

            #centrality_file.write(str(graph) + "(betwenness): \n\n")
            for k, v in centralities_copy:
                #centrality_file.write(str(k) + " : " + str(v) + "\n")
                v = round(v, 3)
                if v in centrality_frequencies:
                    centrality_frequencies[v] += 1
                else:
                    centrality_frequencies[v] = 1

            centrality_frequencies = sorted(centrality_frequencies.items(), key=lambda x: x[0], reverse=True)
            file.write(str(graph) + " : \n\n")
            for k, v in centrality_frequencies:
                file.write(str(k) + " : " + str(v) + "\n")

        file.close()
        #centrality_file.close()
        """

