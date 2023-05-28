from experiments.coverage_experiment import CoverageExperiment

if __name__ == '__main__':

    coverage = CoverageExperiment()
    coverage.cascade_model_coverages()
    coverage.sir_model_coverages()
    coverage.threshold_model_coverages()

