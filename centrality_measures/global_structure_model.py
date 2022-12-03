from utils.k_shell import KShell
import math


class GlobalStructureModel:

    def __init__(self, graph):
        k_shell = KShell(graph)

        self.graph = k_shell.assign_k_shell_numbers()
        self.centrality_values = dict()
        self.calculate_influences()

    def calculate_influences(self):
        for node in self.graph.nodes:
            influence = math.pow(math.e, (self.graph.nodes[node]["k-shell"] / len(self.graph.nodes)))

            self.graph.nodes[node]["self-influence"] = influence
            print(str(node) + " :" + str(influence))

