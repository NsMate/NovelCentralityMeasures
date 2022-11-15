from centrality_measures.local_clustering_h_index import LocalClusteringHIndexCentrality

class LocalHIndexExperiments:

    def __init__(self, graph):
        self.graph = graph
        self.lchi = LocalClusteringHIndexCentrality(self.graph)

    def calculate_centrality_values(self):
        self.graph = self.lchi.calculate_h_index()


