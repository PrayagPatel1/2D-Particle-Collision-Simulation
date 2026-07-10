""" Experiment Setup

This module provides functions to setup a simple experiment of passing a number
of input passwords into the CaHashEngine and get back a list of hashed passwords
based in ASCII form 0 to 255.

Exported Functions:
generate_frequency_map : Generates an empty frequency map of the number of times
                         that a certain ordinal ASCII value has occured in the 
                         hash passwords.
generate_ascii_passwords : Generates a uniform size list of input passwords to 
                           hash given the number of passwords to generate and 
                           how long should each password be. 
run_experiment : Generates a list of hash passwords that have been outputed 
                 directly from the CaHashEngine using a specific rule set and a 
                 number of generations.
"""

# Custom Implemented Imports
from ca_engine import *
from txt_to_cell_enc import *
from cell_to_txt_enc import *

def generate_frequency_map() -> dict[int, int]:
    """
    Returns an empty dictionary that is used to count the frequency of ordinal 
    values of ASCII characters.

    Parameter
    ---------
    None

    Return
    ------
    dict[int, int]
        Represents the frequency map where the keys are the ordinal values and 
        the values are the frequency count of these values.
    """
    ascii_freq_map = {}
    for num in range(0, 256):
        ascii_freq_map[num] = 0
    
    return ascii_freq_map

def generate_ascii_passwords(num_of_passwrd: int, num_of_char: int) -> list[str]:
    """
    Returns a list of strings of size <num_of_passwrd>, with each element having
    <num_of_char> printable ASCII characters. Randomly generated.

    Parameters
    ----------
    num_of_password : int
        The length that the list of passwords should be.
    num_of_char : int
        The length that each password must be within the output list.
    
    Returns
    -------
    list[str]
        A list of randomly generated passwords.
    """
    ascii_passwords = []
    for _ in range(num_of_passwrd):
        element = ""
        for _ in range(num_of_char):
            ascii_dec = random.randint(32, 127)
            element+=chr(ascii_dec)
        ascii_passwords.append(element)
    
    return ascii_passwords

def run_experiment(input_pwds: list[str], rule_set: ElementaryRule, 
                   num_of_gen: int) -> list[str]:
    """
    Runs the input passwords, <input_pwd>, through the CaHashEngine given the 
    rule set, <rule_set>, and the number of generation that the input passwords
    must go through, <num_of_gen>.

    Parameters
    ----------
    input_pwds : list[str]
        An array of passwords to be fed through the hash engine.
    rule_set : ElementaryRule
        A rule set that will determine the new generation of array of cells.
    num_of_gen: int
        The number of times that the rule set must be applied to an input 
        password.
    
    Return
    ------
    list[str]
        A list of hashed passwords.
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