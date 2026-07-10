""" Experiment Setup

This module provides functions to setup a simple experiment of passing a number
of input passwords into the CaHashEngine and get back a list of hashed passwords
based in ASCII form 0 to 255.

Exported Functions:
generate_frequency_map :
generate_ascii_passwords : 
run_experiment : 
"""

from ca_engine import *
from txt_to_cell_enc import *
from cell_to_txt_enc import *

def generate_frequency_map() -> dict[str, int]:
    ascii_freq_map = {}
    for num in range(0, 256):
        ascii_freq_map[num] = 0
    
    return ascii_freq_map

def generate_ascii_passwords(num_of_passwrd: int, num_of_char: int) -> list[str]:
    """
    Returns a list of strings of size <num_of_passwrd>, with each element having
    <num_of_char> printable ASCII characters. 
    """
    ascii_passwords = []
    for _ in range(num_of_passwrd):
        element = ""
        for _ in range(num_of_char):
            ascii_dec = random.randint(32, 127)
            element+=chr(ascii_dec)
        ascii_passwords.append(element)
    
    return ascii_passwords

def run_experiment(input_pwds: list[str], rule_set: ElementaryRule, num_of_gen: int) -> list[str]:
    """
    Runs the experiment.
    """
    hashed_pwds = []

    idx = 0
    for pwd in input_pwds:
        init_cell_arr = bin_to_cell(binary_str=(txt_to_bin(passwrd=pwd)))
        init_cell_len = len(init_cell_arr)

        engine = CaHashEngine((init_cell_len, init_cell_arr, num_of_gen, rule_set))
        engine.update()

        ascii_str = bin_to_txt(binary_str=
                                cell_to_bin(cell_matrix=engine.get_cell_matrix()))
        idx += 1
        hashed_pwds.append(ascii_str)

    return hashed_pwds