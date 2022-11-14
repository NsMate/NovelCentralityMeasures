import copy

class KShell:

    def __init__(self, graph):
        self.graph = graph

    def k_nodes(self, graph, k):
        nodes = []
        for node in graph.nodes():
            if graph.degree(node) <= k:
                nodes.append(node)
        return nodes

    # Check if there is any node left with degree d
    def are_there_nodes(self, graph, k):
        flag = 0  # there is no node of deg <= d
        for i in graph.nodes():
            if graph.degree(i) <= k:
                flag = 1
                break
        return flag

    def assign_k_shell_numbers(self):
        # Copy the graph
        graph = copy.deepcopy(self.graph)
        k = 1

        # Bucket being filled currently
        tmp = []

        # list of lists of buckets
        buckets = []
        while 1:
            flag = self.are_there_nodes(graph, k)
            if flag == 0:
                k += 1
                buckets.append(tmp)
                tmp = []
            if flag == 1:
                node_set = self.k_nodes(graph, k)
                for each in node_set:
                    self.graph.nodes[each]["k-shell"] = k
                    graph.remove_node(each)
                    tmp.append(each)
            if graph.number_of_nodes() == 0:
                buckets.append(tmp)
                break
        return self.graph

