from utils.read_graph import ReadGraph

import networkx as nx
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc


class SpreadExperiment:

    def __init__(self):
        self.reader = ReadGraph()
        self.graphs = ["high_degree.mtx", "low_degree.mtx", "high_kcore.mtx", "low_kcore.mtx", "high_triangle.mtx",
              "low_triangle.mtx"]
        self.local_h_cores = []
        self.local_fuzzy_cores = []
        self.global_structure_model_cores = []
        self.degree_centrality_nodes = []
        self.betweenness_centrality_nodes = []

    def sir_model_spread(self):
        i = 0
        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            model = ep.SIRModel(read_graph)
            cfg = mc.Configuration()
            cfg.add_model_parameter('beta', 0.01)
            cfg.add_model_parameter('gamma', 0.05)

            cfg.add_model_initial_configuration("Infected", self.local_h_cores[i])
            model.set_initial_status(cfg)

            local_h_iteration = model.iteration_bunch(200)
            model.reset()

            cfg.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])
            model.set_initial_status(cfg)

            local_fuzzy_iteration = model.iteration_bunch(200)
            model.reset()

            cfg.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])
            model.set_initial_status(cfg)

            global_structure_iteration = model.iteration_bunch(200)
            model.reset()

            cfg.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])
            model.set_initial_status(cfg)

            degree_centrality_iteration = model.iteration_bunch(200)
            model.reset()

            cfg.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])
            model.set_initial_status(cfg)

            betweenness_iteration = model.iteration_bunch(200)

            i += 1
            print(local_h_iteration)

    def threshold_model_spread(self):
        i = 0
        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)
            model = ep.ThresholdModel(read_graph)

            config = mc.Configuration()

            threshold = 0.25
            for i in read_graph.nodes():
                config.add_node_configuration("threshold", i, threshold)

            config.add_model_initial_configuration("Infected", self.local_h_cores[i])

            model.set_initial_status(config)

            local_h_iteration = model.iteration_bunch(200)
            model.reset()

            config.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])

            model.set_initial_status(config)

            local_fuzzy_iteration = model.iteration_bunch(200)
            model.reset()

            config.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])

            model.set_initial_status(config)

            global_structure_iteration = model.iteration_bunch(200)
            model.reset()

            config.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])

            model.set_initial_status(config)

            degree_iteration = model.iteration_bunch(200)
            model.reset()

            config.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])

            model.set_initial_status(config)

            between_iteration = model.iteration_bunch(200)

    def cascade_model_spread(self):
        i = 0
        for graph in self.graphs:
            read_graph = self.reader.read_graph(graph)

            model = ep.IndependentCascadesModel(read_graph)
            config = mc.Configuration()
            threshold = 0.001
            for i in self.graph.edges():
                config.add_edge_configuration("threshold", i, threshold)

            config.add_model_initial_configuration("Infected", self.local_h_cores[i])

            model.set_initial_status(config)

            local_h_iteration = model.iteration_bunch(400)
            model.reset()

            config.add_model_initial_configuration("Infected", self.local_fuzzy_cores[i])

            model.set_initial_status(config)

            local_fuzzy_iteration = model.iteration_bunch(400)
            model.reset()

            config.add_model_initial_configuration("Infected", self.global_structure_model_cores[i])

            model.set_initial_status(config)

            global_structure_iteration = model.iteration_bunch(400)
            model.reset()

            config.add_model_initial_configuration("Infected", self.degree_centrality_nodes[i])

            model.set_initial_status(config)

            degree_iteration = model.iteration_bunch(400)
            model.reset()

            config.add_model_initial_configuration("Infected", self.betweenness_centrality_nodes[i])

            model.set_initial_status(config)

            between_iteration = model.iteration_bunch(400)
            model.reset()

