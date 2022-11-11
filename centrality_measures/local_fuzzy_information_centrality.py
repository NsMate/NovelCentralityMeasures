import math
import networkx as nx


class LocalFuzzyInformationTechnology:

    def __init__(self, graph):
        # Network Definition
        self.g = graph

        self.top_nodes = [0] * 3

    def find_maximum_shortest_path(self, source):
        path_lengths = nx.shortest_path_length(self.g, source=source)

        return math.floor(path_lengths.get(next(reversed(path_lengths))) / 2)

    def classify_nodes_from_center(self, source):
        fuzzy_numbers = dict()
        max_class = self.find_maximum_shortest_path(source)
        path_lengths = nx.shortest_path_length(self.g, source=source)

        for k, v in path_lengths.items():
            if v <= max_class:
                self.g.nodes[k]["class"] = v
                self.g.nodes[k]["weight"] = math.exp(-(v*v / max_class * max_class))
                if v in fuzzy_numbers:
                    fuzzy_numbers[v] = fuzzy_numbers[v] + 1
                elif v != 0:
                    fuzzy_numbers[v] = 1

        self.calculate_total_fuzzy_number_of_nodes(fuzzy_numbers, max_class)

    def calculate_total_fuzzy_number_of_nodes(self, fuzzy_numbers, max_class):
        total_fuzzy_numbers = 0
        for k, v in fuzzy_numbers.items():
            fuzzy_numbers[k] = v * math.exp(-((k*k)/(max_class*max_class)))
            total_fuzzy_numbers = total_fuzzy_numbers + (v * math.exp(-((k*k)/(max_class*max_class))))


        self.obtain_adjusted_probability(fuzzy_numbers, total_fuzzy_numbers)

    def obtain_adjusted_probability(self, fuzzy_numbers, total_fuzzy_number):
        probability_of_nodes = dict()
        for k, v in fuzzy_numbers.items():
            probability_of_nodes[k] = (1 / math.e) * (v / total_fuzzy_number)

        self.get_node_lfic_value(probability_of_nodes)

    def check(self):
        for node in self.g.nodes:
            self.classify_nodes_from_center(node)

        print("")
        print("")
        print("")
        print("Best lfic values: ")
        print(self.top_nodes)

    def get_node_lfic_value(self, probability_of_nodes):
        lfic_value = 0
        for k, v in probability_of_nodes.items():
            lfic_value = lfic_value + (-v * math.log(v)) / (k*k)

        for i in range(0, 3):
            if self.top_nodes[i] < lfic_value:
                self.top_nodes[i] = lfic_value

