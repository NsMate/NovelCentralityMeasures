from utils.k_shell import KShell
import math
import networkx as nx


class GlobalStructureModel:

    def __init__(self, graph):
        k_shell = KShell(graph)

        self.graph = k_shell.assign_k_shell_numbers()
        self.centrality_values = dict()
        self.calculate_influences()

    def calculate_influences(self):
        for node in self.graph.nodes:
            global_influence = 0
            influence = math.pow(math.e, (self.graph.nodes[node]["k-shell"] / len(self.graph.nodes)))

            self.graph.nodes[node]["self-influence"] = influence

            for next_node in self.graph.nodes:
                if next_node != node:
                    global_influence += self.graph.nodes[next_node]["k-shell"] / \
                                    (len(nx.shortest_path(self.graph, source=node, target=next_node)) - 1)

            self.centrality_values[node] = influence * global_influence

