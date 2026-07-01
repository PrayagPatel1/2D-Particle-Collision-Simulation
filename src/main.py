from ca_engine import *
from ca_visualizer import *

""" Entry Point """
if __name__ == "__main__":
    engine = CaHashEngine(101, 50, RULE_150)
    engine.update()

    visualizer = CaVisualizer(engine.get_cell_matrix(), True, False)
    visualizer.render_to_terminal()