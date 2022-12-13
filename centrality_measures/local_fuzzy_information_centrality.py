import math
import networkx as nx


class LocalFuzzyInformationTechnology:

    def __init__(self, graph):
        self.g = graph

        self.centrality_values = dict()

    def set_graph(self, graph):
        self.g = graph

    def classify_nodes_from_center(self, source):
        fuzzy_numbers = dict()
        path_lengths = nx.shortest_path_length(self.g, source=source)
        max_class = math.ceil(path_lengths.get(next(reversed(path_lengths))) / 2)

        for k, v in path_lengths.items():
            if v <= max_class and v != 0:
                self.g.nodes[k]["class"] = v
                self.g.nodes[k]["weight"] = math.exp(-(v*v / max_class * max_class))
                if v in fuzzy_numbers:
                    fuzzy_numbers[v] = fuzzy_numbers[v] + 1
                elif v != 0:
                    fuzzy_numbers[v] = 1
        self.calculate_total_fuzzy_number_of_nodes(source, fuzzy_numbers, max_class)

    def calculate_total_fuzzy_number_of_nodes(self, source, fuzzy_numbers, max_class):
        total_fuzzy_numbers = 0
        for k, v in fuzzy_numbers.items():
            fuzzy_numbers[k] = v * math.exp(-((k*k)/(max_class*max_class)))
            total_fuzzy_numbers = total_fuzzy_numbers + (v * math.exp(-((k*k)/(max_class*max_class))))

        self.obtain_adjusted_probability(source, fuzzy_numbers, total_fuzzy_numbers)

    def obtain_adjusted_probability(self, source, fuzzy_numbers, total_fuzzy_number):
        probability_of_nodes = dict()
        for k, v in fuzzy_numbers.items():
            probability_of_nodes[k] = (1 / math.e) * (v / total_fuzzy_number)

        self.get_node_lfic_value(source, probability_of_nodes)

    def get_centrality_values(self):
        for node in self.g:
            self.classify_nodes_from_center(node)

        return self.centrality_values

    def get_node_lfic_value(self, source, probability_of_nodes):
        lfic_value = 0
        for k, v in probability_of_nodes.items():
            lfic_value += -v * math.log(v) / (k*k)
            self.centrality_values[source] = lfic_value

