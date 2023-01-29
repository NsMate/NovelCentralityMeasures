from utils.read_graph import ReadGraph

import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc


class SpreadExperiment:

    def __init__(self):
        self.reader = ReadGraph()
        self.graphs = ["high_degree.mtx", "low_degree.mtx", "high_kcore.mtx", "low_kcore.mtx", "high_triangle.mtx",
              "low_triangle.mtx"]
        self.local_h_cores = [[1439, 87, 1494, 2610, 156], [265, 340, 90, 67, 56], [1673, 2036, 3525, 1177, 3156],
                              [157, 46, 30, 597, 328], [2565, 1549, 766, 1166, 457], [418, 650, 867, 229, 198]]
        self.local_fuzzy_cores = [[1439, 87, 1494, 2610, 1428], [265, 90, 67, 340, 56], [2008, 3254, 3122, 1673, 2895],
                                  [380, 381, 662, 663, 690], [2304, 2305, 3194, 3195, 3244], [528, 17, 882, 23, 1045]]
        self.global_structure_model_cores = [[1439, 87, 1494, 2610, 3108], [265, 340, 90, 67, 56], [1673, 2036, 1177, 603, 1595],
                                             [157, 46, 30, 597, 328], [2565, 766, 1549, 457, 1166], [418, 650, 900, 867, 223]]
        self.degree_centrality_nodes = [[1439, 87, 1494, 2610, 3108], [265, 518, 67, 340, 90], [2008, 3254, 3525, 1177, 1673],
                                        [157, 46, 597, 30, 328], [2565, 766, 11, 1549, 457], [223, 546, 418, 1093, 518]]
        self.betweenness_centrality_nodes = [[1439, 1494, 2610, 3108, 3117], [265, 31, 518, 618, 35], [3254, 2008, 819, 2170, 2751],
                                             [157, 46, 597, 30, 232, 328], [2565, 11, 457, 4037, 1549], [223, 418, 546, 867, 900]]

    def write_result_to_file(self, model, config, algorithm, file):
        susceptible = 0
        infected = 0
        removed = 0
        infected_and_removed = 0
        iteration = 25
        repeat = 500
        for i in range(0, repeat, 1):
            model.set_initial_status(config)
            iteration_result = model.iteration_bunch(iteration)
            susceptible += iteration_result[-1]["node_count"][0]
            infected += iteration_result[-1]["node_count"][1]
            if algorithm == ("SIR" or "CASCADE"):
                removed += iteration_result[-1]["node_count"][2]
                infected_and_removed += infected
                infected_and_removed += removed
            model.reset()
        susceptible = susceptible / repeat
        infected = infected / repeat
        file.write("500 AVG susceptible: " + str(susceptible) + " \n")
        file.write("500 AVG infected : " + str(infected) + " \n")
        if algorithm == ("SIR" or "CASCADE"):
            removed = removed / repeat
            infected_and_removed = infected_and_removed / repeat
            file.write("500 AVG removed: " + str(removed) + " \n")
            file.write("500 AVG infected and removed: " + str(infected_and_removed) + " \n\n")
        else:
            file.write("\n")

    def sir_model_spread(self):
        algorithm = "SIR"
        i = 0
        file = open('results/spread_results/sir_eredmények.txt', 'w', encoding='utf-8')
        file.write("SIR model eredmények: \n\n")

        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            file.write(str(graph) + ": \n\n")
            model = ep.SIRModel(read_graph)
            cfg = mc.Configuration()
            cfg.add_model_parameter('beta', 0.005)
            cfg.add_model_parameter('gamma', 0.005)

            cfg.add_model_initial_configuration("Infected", self.local_h_cores[i])
            file.write("Local H Index cores: \n")

            self.write_result_to_file(model, cfg, algorithm, file)

            cfg.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])
            file.write("Local Fuzzy cores: \n")
            
            self.write_result_to_file(model, cfg, algorithm, file)

            cfg.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])
            file.write("Global structure model cores: \n")
            
            self.write_result_to_file(model, cfg, algorithm, file)

            cfg.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])
            file.write("Degree centrality cores: \n")
            
            self.write_result_to_file(model, cfg, algorithm, file)

            cfg.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])
            file.write("Betwenness cores: \n")
            
            self.write_result_to_file(model, cfg, algorithm, file)

            i += 1
        file.close()

    def threshold_model_spread(self):
        algorithm = "THRESHOLD"
        i = 0

        file = open('results/spread_results/threshold_eredmények.txt', 'w', encoding='utf-8')
        file.write("Threshold model eredmények: \n\n")

        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            file.write(str(graph) + ": \n\n")
            model = ep.ThresholdModel(read_graph)

            config = mc.Configuration()

            threshold = 0.12
            for node in read_graph.nodes():
                config.add_node_configuration("threshold", node, threshold)

            config.add_model_initial_configuration("Infected", self.local_h_cores[i])
            file.write("Local H Index cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])
            file.write("Local Fuzzy cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])
            file.write("Global structure model cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])
            file.write("Degree centrality cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])
            file.write("Betwenness centrality cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            i += 1
        file.close()

    def cascade_model_spread(self):
        i = 0
        algorithm = "CASCADE"

        file = open('results/spread_results/cascade_eredmények.txt', 'w', encoding='utf-8')
        file.write("Cascade model eredmények: \n\n")

        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            file.write(str(graph) + ": \n\n")

            model = ep.IndependentCascadesModel(read_graph)
            config = mc.Configuration()
            threshold = 0.12
            for edge in read_graph.edges:
                config.add_edge_configuration("threshold", edge, threshold)

            config.add_model_initial_configuration("Infected", self.local_h_cores[i])
            file.write("Local H Index cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])
            file.write("Local Fuzzy centrality cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])
            file.write("Global Structure model cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])
            file.write("Degree centrality cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            config.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])
            file.write("Betweennes centrality cores: \n")

            self.write_result_to_file(model, config, algorithm, file)

            i += 1
        file.close()

