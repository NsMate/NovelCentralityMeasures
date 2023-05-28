from utils.k_shell import KShell
import math
import networkx as nx


class GlobalStructureModel:

    def __init__(self):
        self.k_shell = KShell()
        self.graph = nx.Graph()

        self.centrality_values = dict()

    def set_graph(self, graph):
        self.centrality_values = dict()
        self.graph = graph

    def get_centrality_values(self):
        self.k_shell.set_graph(self.graph)
        self.graph = self.k_shell.assign_k_shell_numbers()
        for node in self.graph.nodes:
            global_influence = 0
            influence = math.pow(math.e, (self.graph.nodes[node]["k-shell"] / len(self.graph.nodes)))

            self.graph.nodes[node]["self-influence"] = influence

            for next_node in self.graph.nodes:
                if next_node != node and nx.has_path(self.graph, source=node, target=next_node):
                    global_influence += self.graph.nodes[next_node]["k-shell"] / \
                                (len(nx.shortest_path(self.graph, source=node, target=next_node)) - 1)

            self.centrality_values[node] = influence * global_influence

        return self.centrality_values

