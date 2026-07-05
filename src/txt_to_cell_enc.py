"""Text-to-Cell Encoding

This module provides functions and constants for encoding an ASCII password into
an array of Cell objects and convert that array of Cell objects to the initial
parameters of the CaHashEngine.

Exported Functions / Constants:
txt_to_bin : Converts an ASCII password to its binary equivalent in a 
                     string format.
bin_to_cell : Converts a string representing binary information into an
                      array of Cell objects whose states reperesents the binary
                      information.
"""

from .ca_engine import *

def txt_to_bin(passwrd: str) -> str:
    """Returns a string that represents the binary equivalent of <passwrd>."""
    binary_str = ''.join(format(ord(char), '08b') for char in passwrd)
    return binary_str

def bin_to_cell(binary_str: str) -> list[Cell]:
    """
    Returns an array of Cell objects that represents <binary_str>, where the
    the state of the Cell represents either 1 for "alive" or 0 for "dead". 
    """
    cell_arr = []
    for bit in binary_str:
        if bit == "1":
            cell_arr.append(Cell(CELL_ALIVE))
        elif bit == "0":
            cell_arr.append(Cell(CELL_DEAD))
    
    return cell_arr

