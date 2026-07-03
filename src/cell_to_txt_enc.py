"""Cell-to-Text Encode

This module provides functions / constants that encodes an array of Cell objects
into a sequence of ASCII standard characters. 

Exported Functions
cell_to_bin : Converts an array of Cell objects into a string of binary values. 
bin_to_txt : Converts the string of binary to ASCII text. 
"""
from ca_engine import *

def cell_to_bin(cell_matrix: list[list[Cell]]) -> str:
    """
    Returns a string containing binary data of the last Cell object array
    within the <cell_matrix>.
    """
    final_cell_arr = cell_matrix[len(cell_matrix)]
    binary_str = ""
    for cell in final_cell_arr:
        if cell.get_state() == CELL_ALIVE:
            binary_str+="1"
        elif cell.get_state() == CELL_DEAD:
            binary_str+="0"
    
    return binary_str

def bin_to_txt(binary_str: str) -> str:
    """Returns a string containing the text eqivalent of <binary_str>."""
    binary_int = int(binary_str, 2)
    byte_num = (binary_int.bit_length() + 7) // 8
    ascii_str = binary_int.to_bytes(byte_num, byteorder="big").decode("ascii")
    return ascii_str