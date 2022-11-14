from utils.k_shell import KShell

import networkx as nx


class NodeCorrelationMethod:

    def __init__(self, graph):
        k_shell = KShell(graph)

        self.graph = k_shell.assign_k_shell_numbers()

        for n in self.graph.nodes:
            self.graph.nodes[n]["h_index"] = self.calculate_h_index(n)
            self.graph.nodes[n]["c_coefficient"] = nx.clustering(self.graph, n)

        self.local_clustering_h_index()

    def calculate_h_index(self, node):
        sorted_neighbor_degrees = sorted((self.graph.degree(v) for v in self.graph.neighbors(node)), reverse=True)
        h = 0
        for i in range(1, len(sorted_neighbor_degrees) + 1):
            if sorted_neighbor_degrees[i - 1] < i:
                break
            h = i

        return h

    def local_clustering_h_index(self):
        avg_h_index = 0
        avg_degree = 0

        for node in self.graph:
            avg_h_index += self.graph.nodes[node]["h_index"]
            avg_degree += self.graph.degree[node]
        avg_h_index = avg_h_index / len(self.graph.nodes)
        avg_degree = avg_degree / len(self.graph.nodes)

        mu = avg_h_index / avg_degree

        for node in self.graph:
            lchi = 0
            neighbor_influence = 0
            for n in self.graph.neighbors(node):
                neighbor_influence += self.graph.nodes[n]["h_index"] / (1 + self.graph.nodes[n]["c_coefficient"]) \
                            + mu * self.graph.degree(n)

            lchi = self.graph.nodes[node]["h_index"] / (1 + self.graph.nodes[node]["c_coefficient"]) \
                            + neighbor_influence

            self.graph.nodes[node]["lchi"] = lchi
            print(lchi)

