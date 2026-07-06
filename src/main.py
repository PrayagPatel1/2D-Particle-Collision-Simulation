from ca_engine import *
from ca_visualizer import *
from txt_to_cell_enc import *
from cell_to_txt_enc import *
import matplotlib.pyplot as plt

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
    passwords = generate_ascii_passwords(200, 8)
    
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

if __name__ == "__main__":
    freq_map = generate_frequency_map()
    hashed_pwds = run_experiment(RULE_150, 500)

    for pwd_str in hashed_pwds:
        for char in pwd_str:
            freq_map[ord(char)] += 1
    
    # print("\n")

    # for key in freq_map:
    #     print(f"{key}: {freq_map[key]}")

    ascii_chars = list(freq_map.keys())
    char_freq = list(freq_map.values())

    plt.bar(ascii_chars, char_freq)
    plt.title("Frequency of ASCII Characters of 200 CA Hashed Passwords using Rule 150 for 500 generations")
    plt.xlabel("ASCII Characters in Decimal Form")
    plt.ylabel("Frequency")
    plt.show()
