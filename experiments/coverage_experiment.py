from utils.read_graph import ReadGraph

import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc


class CoverageExperiment:

    def __init__(self):
        self.reader = ReadGraph()
        self.graphs = ["high_degree.mtx", "low_degree.mtx", "high_kcore.mtx", "low_kcore.mtx", "high_triangle.mtx",
                       "low_triangle.mtx"]
        self.local_h_cores = [[1439, 87, 1494, 2610, 156], [265, 340, 90, 67, 56], [1673, 2036, 3525, 1177, 3156],
                              [157, 46, 30, 597, 328], [2565, 1549, 766, 1166, 457], [418, 650, 867, 229, 198]]
        self.local_fuzzy_cores = [[1439, 87, 1494, 2610, 1428], [265, 90, 67, 340, 56], [2008, 3254, 3122, 1673, 2895],
                                  [380, 381, 662, 663, 690], [2304, 2305, 3194, 3195, 3244], [528, 17, 882, 23, 1045]]
        self.global_structure_model_cores = [[1439, 87, 1494, 2610, 3108], [265, 340, 90, 67, 56],
                                             [1673, 2036, 1177, 603, 1595],
                                             [157, 46, 30, 597, 328], [2565, 766, 1549, 457, 1166],
                                             [418, 650, 900, 867, 223]]
        self.degree_centrality_nodes = [[1439, 87, 1494, 2610, 3108], [265, 518, 67, 340, 90],
                                        [2008, 3254, 3525, 1177, 1673],
                                        [157, 46, 597, 30, 328], [2565, 766, 11, 1549, 457], [223, 546, 418, 1093, 518]]
        self.betweenness_centrality_nodes = [[1439, 1494, 2610, 3108, 3117], [265, 31, 518, 618, 35],
                                             [3254, 2008, 819, 2170, 2751],
                                             [157, 46, 597, 30, 232, 328], [2565, 11, 457, 4037, 1549],
                                             [223, 418, 546, 867, 900]]

    def write_result_to_file(self, graph, model, config, algorithm, centrality, graph_name):
        file = open('results/coverage_results/' + str(algorithm) + '/' + str(centrality) + '/' + str(graph_name) + '.txt', 'w', encoding='utf-8')

        model.set_initial_status(config)
        iteration_number = 25
        repeat = 500

        for i in range(0, repeat, 1):
            i = 0
            model.set_initial_status(config)
            iterations = model.iteration_bunch(iteration_number)

            for iteration in iterations:
                i += 1
                file.write(str(i) + ","
                           + str(len(graph.nodes)) + ","
                           + str(iteration["node_count"][0]) + ","
                           + str(iteration["node_count"][1]) + "\n")

        file.close()

    def sir_model_coverages(self):
        i = 0
        algorithm = 'SIR'

        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            model = ep.SIRModel(read_graph)
            cfg = mc.Configuration()
            cfg.add_model_parameter('beta', 0.005)
            cfg.add_model_parameter('gamma', 0.005)

            cfg.add_model_initial_configuration("Infected", self.local_h_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_h', graph)

            cfg.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_fuzzy', graph)

            cfg.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'global_structure_m', graph)

            cfg.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'degree', graph)

            cfg.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'between', graph)

            i += 1

    def threshold_model_coverages(self):
        i = 0
        algorithm = 'THRESHOLD'

        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            model = ep.ThresholdModel(read_graph)
            cfg = mc.Configuration()

            threshold = 0.05
            for node in read_graph.nodes():
                cfg.add_node_configuration("threshold", node, threshold)

            cfg.add_model_initial_configuration("Infected", self.local_h_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_h', graph)

            cfg.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_fuzzy', graph)

            cfg.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'global_structure_m', graph)

            cfg.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'degree', graph)

            cfg.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'between', graph)

            i += 1

    def cascade_model_coverages(self):
        i = 0
        algorithm = 'CASCADE'

        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            model = ep.IndependentCascadesModel(read_graph)
            cfg = mc.Configuration()

            threshold = 0.05
            for e in read_graph.edges():
                cfg.add_edge_configuration("threshold", e, threshold)

            cfg.add_model_initial_configuration("Infected", self.local_h_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_h', graph)

            cfg.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_h', graph)

            cfg.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_h', graph)

            cfg.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_h', graph)

            cfg.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])

            self.write_result_to_file(read_graph, model, cfg, algorithm, 'local_h', graph)

            i += 1
