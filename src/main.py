from ca_engine import *
from ca_visualizer import *
from txt_to_cell_enc import *

""" Entry Point """
if __name__ == "__main__":
    password = "hi1235"

    init_cell_arr = bin_to_cell(binary_str=(txt_to_bin(passwrd=password)))
    init_cell_len = len(init_cell_arr)
    num_of_gen = 50
    rule_set = RULE_30

    engine = CaHashEngine((init_cell_len, init_cell_arr, num_of_gen, rule_set))
    engine.update()

    visualizer = CaVisualizer(engine.get_cell_matrix(), True, False)
    visualizer.render_to_terminal()