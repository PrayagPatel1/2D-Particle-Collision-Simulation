""" Statistics

This module provides functions to record statistics of the performance of the
CaHashEngine class. 

Exported Function: 
count_byte_frequency : Counts the number of times that the same byte has occured.
hist_of_byte_freq : Plots the contents of a frequency map as a histogram.
chi_square_statistc : Calculates the Chi-Square goodness of fit statistic and 
                      plots the distribution. 
byte_pair_heatmap : Plots the frequency of a pair of consecutive bytes that have
                    occured in the hashed passwords as a heatmap.
bit_balance_statistic : Determines the percentage of howmany times a 1 bit and a
                        0 bit has occured in the array of hashed passwords.0
hash_collision_statistic : Determines the number of times that two seperate 
                           input characters have returned the same hash. 
"""

# Third-party Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

# Custom Implemented Imports
from txt_to_cell_enc import *

def count_byte_frequency(hashed_pwds: list[str], freq_map: dict[int, int]) -> None:
    """
    Counts the number of times that the same byte has occured in <hashed_pwds> 
    and modifies <freq_map>.

    Parameters
    ----------
    hashed_pwds : list[str]
        An array pf hashed passwords.
    freq_map : dict[int, int]
        A dictionary where the keys are the ordinal values of ASCII characters
        and the value is the freqeuncy of that ASCII character to occur.
    
    Return
    -------
    None
    """
    for pwd_str in hashed_pwds:
        for char in pwd_str:
            freq_map[ord(char)] += 1
    

def hist_of_byte_freq(freq_map: dict[int, int], rule_set_name: str, gen_num: str) -> None:
    """
    Plots a histogram to show the data from <freq_map> given the rule set name, 
    <rule_set_name>, and the generation number, <gen_num>. 

    Parameters
    ----------
    freq_map : dict[int, int]
        A dictionary where the keys are the ordinal values of ASCII characters
        and the value is the freqeuncy of that ASCII character to occur.
    rule_set_name : str
        The name of the rule set used during the experiment.
    gen_num : str
        The number of generations in string format.
    
    Return
    -------
    None
    """
    ascii_chars = list(freq_map.keys())
    char_freq = list(freq_map.values())

    plt.bar(ascii_chars, char_freq)
    plt.title(f"Frequency of ASCII Characters for 10,000 CA Hashed Passwords", 
              "using Rule {rule_set_name} for {gen_num} generations")
    plt.xlabel("ASCII Characters in Decimal Form")
    plt.ylabel("Frequency")
    plt.show()

def chi_square_statistc(observed_freq: dict[int, int], expected_freq: int) -> None:
    """
    Determines and plots the chi-square using <observed_freq> and the 
    <expected_freq>. 

    Parameters
    ----------
    observed_freq : dict[int, int]
        A dictionary where the keys are the ordinal values of ASCII characters
        and the value is the freqeuncy of that ASCII character to occur.
    expected_freq : int
        The expected count of ASCII characters for an ideal hash function to 
        produce. 
    
    Return
    -------
    None
    """
    # Calculate Chi-Square statistic for our observed freqency of byte compared
    # to the expected frequency of byte.

    chi_square_stat = 0.0
    for byte in observed_freq:
        numerator = (observed_freq[byte] - expected_freq) ** 2
        chi_square_stat += (numerator / expected_freq)
    
    # Plot the theoretical PDF of chi-square distribution with a degree of 
    # freedom to be 255.

    deg_freedom = 255
    x_axis = np.linspace(200, 320, 10000) 
    y_axis = chi2.pdf(x_axis, deg_freedom)
    plt.figure(figsize=(10, 8))
    plt.plot(x_axis, 
             y_axis, 
             label="Chi-Square PDF ($df = 255$)", 
             color='blue', 
             linewidth=2)
    plt.fill_between(x_axis, 
                     y_axis,
                     where=(x_axis >= chi_square_stat),  
                     color='orange', 
                     alpha=0.4)
    plt.title("Theoretical Chi-Square Distribution ($df = 255$)")
    plt.xlabel("$\chi^2$ Value")
    plt.ylabel("Probability Density")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def byte_pair_heatmap(hashed_pwds: list[str], num_gen: str) -> None:
    """
    Counts the frequency of the number of byte pairs that occur within 
    <hashed_pwds> and plots a heatmap given <num_gen>. 

    Parameters
    ----------
    hashed_pwds : list[str]
        An array pf hashed passwords.
    num_gen: str
        The number of generations that an input password went through in string 
        format.
    
    Return
    -------
    None
    """
    byte_map = [[0 for _ in range(256)] for _ in range(256)]

    for pwd in hashed_pwds:
        for char_idx in range(len(pwd) - 1):
            byte_map[ord(pwd[char_idx])][ord(pwd[char_idx + 1])] += 1
    
    plt.imshow(byte_map, cmap='viridis')
    plt.title(f"Byte Pair Heatmap Of 10,000 Hashed Passwords Using Rule 30 For", 
              "{num_gen} Generations")
    plt.xlabel("Ordinal Values of ASCII Characters (0-255)")
    plt.ylabel("Ordinal Values of ASCII Characters (0-255)")
    plt.colorbar()
    plt.show()

def bit_balance_statistic(hashed_pwds: list[str]) -> tuple[float, float]:
    """
    Returns a tuple of the percentage that a 0 bit occurs within a hashed 
    password and the percentage that a 1 bit occurs.

    Parameter
    ----------
    hashed_pwds : list[str]
        An array of hashed passwords.
    
    Return
    ------
    tuple[float, float]
        Represents the two percentages of the number of times that a 0 bit 
        occurs and a 1 bit occurs respectively.
    """
    binary_hashed_pwd = [txt_to_bin(pwd) for pwd in hashed_pwds]
    bit_freq = {"1": 0, "0": 0}

    for bin_pwd in binary_hashed_pwd:
        for bit in bin_pwd:
            if bit == "1": 
                bit_freq[bit] += 1
            else:
                bit_freq[bit] += 1
    
    bit_one_percentage = bit_freq["1"] / (10 * 8 * 8)
    bit_zero_percentage = 1.0 - bit_one_percentage

    return (bit_zero_percentage, bit_one_percentage)

def hash_collision_statistic(hashed_pwds: list[str]) -> int:
    """
    Returns an integer that represents the number of times that there has been
    a hash collision in <hashed_pwds>. 

    Parameter
    ---------
    hashed_pwds : list[str]
        An array of hashed passwords.
    
    Return
    ------
    int 
        Represents the number of times that a hash collision has occured.
    """
    num_duplicate = 0
    for pwd_idx in range(len(hashed_pwds) - 1):
        if hashed_pwds[pwd_idx] == hashed_pwds[pwd_idx + 1]:
            num_duplicate += 1
    
    return num_duplicate