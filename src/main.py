from ca_engine import *
from ca_visualizer import *
from txt_to_cell_enc import *
from cell_to_txt_enc import *

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

""" Entry Point """

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

def run_experiment(rule_set: ElementaryRule, num_of_gen: int) -> list[str]:
    """
    Runs the experiment.
    """
    hashed_pwds = []
    passwords = generate_ascii_passwords(10000, 8)
    
    # print("\n")
    # print("=== Inputting Generate Passwords into CaHashEngine ===")

    idx = 0
    for pwd in passwords:
        init_cell_arr = bin_to_cell(binary_str=(txt_to_bin(passwrd=pwd)))
        init_cell_len = len(init_cell_arr)

        engine = CaHashEngine((init_cell_len, init_cell_arr, num_of_gen, rule_set))
        engine.update()

        ascii_str = bin_to_txt(binary_str=
                                cell_to_bin(cell_matrix=engine.get_cell_matrix()))
        idx += 1
        hashed_pwds.append(ascii_str)
       #  print(f"{idx}: {pwd} |-> {ascii_str}")

    return hashed_pwds

""" Uniformity and Distribution Statistics of CaHashEngine """

def hist_of_byte_freq(hashed_pwds: list[str], freq_map: dict[str, int], rule_set_num: str, gen_num: str) -> None:

    for pwd_str in hashed_pwds:
        for char in pwd_str:
            freq_map[ord(char)] += 1
    
    return
    
    ascii_chars = list(freq_map.keys())
    char_freq = list(freq_map.values())

    plt.bar(ascii_chars, char_freq)
    plt.title(f"Frequency of ASCII Characters for 10,000 CA Hashed Passwords using Rule {rule_set_num} for {gen_num} generations")
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
    

if __name__ == "__main__":
    byte_freqs = generate_frequency_map()
    hashed_pwds = run_experiment(RULE_30, 256)
    hist_of_byte_freq(hashed_pwds, byte_freqs, "", "")

    expected_freq = (10000 * 8) / 256
    chi_square_statistc(byte_freqs, expected_freq)
