from utils.read_graph import ReadGraph
from centrality_measures.local_clustering_h_index import LocalClusteringHIndexCentrality
from centrality_measures.local_fuzzy_information_centrality import LocalFuzzyInformationTechnology
from centrality_measures.effective_distance_centrality import EffectiveDistanceBasedCentrality


class GraphAttributeExperiments:

    def __init__(self):
        self.reader = ReadGraph()

    def run_centralities_on_avg_triangle_graphs(self):
        high_triangle_graph = self.reader.read_graph("high_avg_triangle_graph.mtx")
        low_triangle_graph = self.reader.read_graph("low_avg_triangle_graph.mtx")

        local_fuzzy = LocalFuzzyInformationTechnology(high_triangle_graph)
        local_hindex = LocalClusteringHIndexCentrality(high_triangle_graph)

        local_fuzzy_high_triangle_nodes = local_fuzzy.get_centrality_values()
        local_hindex_high_triangle_nodes = local_hindex.get_centrality_values()

        # TODO here evaluate which nodes have the best centrality value

        local_fuzzy = LocalFuzzyInformationTechnology(low_triangle_graph)
        local_hindex = LocalClusteringHIndexCentrality(low_triangle_graph)

        local_fuzzy_low_triangle_nodes = local_fuzzy.get_centrality_values()
        local_hindex_low_triangle_nodes = local_hindex.get_centrality_values()

        # TODO here evaluate which nodes have the best centrality value
        # ADD last centrality measure

    def run_centralities_on_avg_degree_graph(self):
        high_degree_graph = self.reader.read_graph("high_avg_degree_graph.mtx")
        low_degree_graph = self.reader.read_graph("low_avg_degree_graph.edges")

        local_fuzzy = LocalFuzzyInformationTechnology(high_degree_graph)
        local_hindex = LocalClusteringHIndexCentrality(high_degree_graph)

        local_fuzzy_high_degree_nodes = local_fuzzy.get_centrality_values()
        local_hindex_high_degree_nodes = local_hindex.get_centrality_values()

        # TODO here evaluate which nodes have the best centrality value

        local_fuzzy = LocalFuzzyInformationTechnology(low_degree_graph)
        local_hindex = LocalClusteringHIndexCentrality(low_degree_graph)

        local_fuzzy_low_degree_nodes = local_fuzzy.get_centrality_values()
        local_hindex_low_degree_nodes = local_hindex.get_centrality_values()

        # TODO here evaluate which nodes have the best centrality value
        # ADD last centrality measure

    def run_centralities_on_k_core_graph(self):
        high_k_core_graph = self.reader.read_graph("high_max_k_core.edges")
        low_k_core_graph = self.reader.read_graph("low_max_k_core.edges")

        local_fuzzy = LocalFuzzyInformationTechnology(high_k_core_graph)
        local_hindex = LocalClusteringHIndexCentrality(high_k_core_graph)

        local_fuzzy_high_max_k_core_nodes = local_fuzzy.get_centrality_values()
        local_hindex_high_max_k_core_nodes = local_hindex.get_centrality_values()

        # TODO here evaluate which nodes have the best centrality value

        local_fuzzy = LocalFuzzyInformationTechnology(low_k_core_graph)
        local_hindex = LocalClusteringHIndexCentrality(low_k_core_graph)

        local_fuzzy_low_max_k_core_nodes = local_fuzzy.get_centrality_values()
        local_hindex_low_max_k_core_nodes = local_hindex.get_centrality_values()

        # TODO here evaluate which nodes have the best centrality value
        # ADD last centrality measure

