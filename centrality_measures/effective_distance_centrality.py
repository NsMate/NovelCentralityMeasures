import networkx as nx
import math

from utils.k_shell import KShell


class EffectiveDistanceBasedCentrality:

    def __init__(self, graph):
        k_shell = KShell(graph)

        self.graph = k_shell.assign_k_shell_numbers()
        for node in self.graph:
            self.calculate_centrality(node)
        # self.get_centrality_values()

    def calculate_effective_distance(self, source):
        P = 1 / (self.graph.degree[source])

        distance = 1 - math.log(P, 10)
        return distance

    def calculate_centrality(self, source):
        neigbour_centrality = 0
        for node in self.graph.neighbors(source):
            k_power = math.sqrt(self.graph.nodes[source]["k-shell"] + self.graph.nodes[node]["k-shell"])
            neigbour_centrality += (k_power + self.graph.degree[source]) \
                                   / math.pow(self.calculate_effective_distance(source), 2)

            self.graph.nodes[source]["influence"] = neigbour_centrality
            for next_node in self.graph.neighbors(node):
                distance = 0
                if next_node in self.graph.neighbors(source):
                    distance = math.pow(self.calculate_effective_distance(source), 2)
                else:
                    distance = math.pow((self.calculate_effective_distance(source)
                                         + self.calculate_effective_distance(next_node)), 2)
                k_power = math.sqrt(self.graph.nodes[source]["k-shell"] + self.graph.nodes[next_node]["k-shell"])
                neigbour_centrality += (k_power + self.graph.degree[source]) / distance

        print(str(source) + ": " + str(neigbour_centrality))

    def get_centrality_values(self):
        for node in self.graph:
            graph_influence = 0
            for next in self.graph.neighbors(node):
                graph_influence += self.graph.nodes[next]["influence"]

            print(str(node) + ": " + str(graph_influence))
