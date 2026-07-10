""" Statistics

This module provides functions to record statistics of the performance of the
CaHashEngine class. 

Exported Function: 
count_byte_frequency : 
hist_of_byte_freq :
chi_square_statistc : 
byte_pair_heatmap : 
bit_balance_statistic : 
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

from txt_to_cell_enc import *

def count_byte_frequency(hashed_pwds: list[str], freq_map: dict[str, int]) -> None:
    for pwd_str in hashed_pwds:
        for char in pwd_str:
            freq_map[ord(char)] += 1
    

def hist_of_byte_freq(freq_map: dict[str, int], rule_set_name: str, gen_num: str) -> None:
    
    ascii_chars = list(freq_map.keys())
    char_freq = list(freq_map.values())

    plt.bar(ascii_chars, char_freq)
    plt.title(f"Frequency of ASCII Characters for 10,000 CA Hashed Passwords using Rule {rule_set_name} for {gen_num} generations")
    plt.xlabel("ASCII Characters in Decimal Form")
    plt.ylabel("Frequency")
    plt.show()

def chi_square_statistc(observed_freq: dict[str, int], expected_freq: int) -> None:
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
    byte_map = [[0 for _ in range(256)] for _ in range(256)]

    for pwd in hashed_pwds:
        for char_idx in range(len(pwd) - 1):
            byte_map[ord(pwd[char_idx])][ord(pwd[char_idx + 1])] += 1
    
    plt.imshow(byte_map, cmap='viridis')
    plt.title(f"Byte Pair Heatmap Of 10,000 Hashed Passwords Using Rule 30 For {num_gen} Generations")
    plt.xlabel("Ordinal Values of ASCII Characters (0-255)")
    plt.ylabel("Ordinal Values of ASCII Characters (0-255)")
    plt.colorbar()
    plt.show()

def bit_balance_statistic(hashed_pwds: list[str]) -> tuple[float, float]:
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
    