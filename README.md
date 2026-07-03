# Celluar Automata Research

[!Warning]

> This isn't a professional research project. I was just curious about using CA for password hashing and led me to code my version from my understadning on the topic through notes and reading about the topic manner. This shouldn't be used as a source for organization or post-secondary research purposes.

Can celluar automata produce cryptographic like properties similar to hash functions? That is the main question
that this repository will try to answer. Note that this is just an experiment on this idea that I was thinking
about and is not meant to be research for a organization or post-secondary instituion. This is a personal
task for me to challenge my own thinking and understanding on celluar automata and basic cryptography.

This project uses Python 3.14.4 as the primary programing language and uses matplotlib for statistical output
and visualizing the image created using different rule sets.

# Build / Installation Instructions

## Prerequisites

1. Python 3.14.4
2. pip 26.0.1
3. git 2.49.0.windows.1

First, clone the repository and change directories:

```bash
git clone https://github.com/PrayagPatel1/Ca-Password-Research.git
cd Ca-Password-Research
```

Then you want to create a virtual environment by entering the following in your
terminal:

```bash
python -m venv myenv
```

Activating the virtual environment depends on what your operating system is. For
Windows its going to be the following,

```bash
myenv\scripts\activate
```

For Linux/macOs its going to be

```bash
source myenv/bin/activate
```

To install all dependcies used by this project, simply enter the following,

```bash
pip isntall -r requirements.txt
```

To run the project do,

```bash
python main.py
```

# Elementary Cellular Automaton

The first hase of this project was to implement a simple elementary CA simulator with some preloaded Wolfram rule sets like
rule 30, rule 90, rule 110, and rule 150. The simulator that was implemented follows the traditional elementary cellular automaton
setup with having a inital array of cells that are either randomized or has one alive state. By applying a rule set on that initial
multiple times, called generations, you get an image where every row of that image is a new generation and every column represents
cells, either alive or dead. Below is a gallery of how these images with different rule sets applied.

<table>
<tr>
<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule_30_with_one_alive_inital_cell.png" width="600"><br>
<b>Figure 1.</b> Time-space diagram of Rule 30 with one "alive" cell in an inital row of cells.
</td>

<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule30_with_random_initial_values.png" width="600"><br>
<b>Figure 2.</b> Time-space diagram of Rule 30 with random inital row of cells.
</td>
</tr>

<tr>
<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule90_with_one_alive_inital_cell.png" width="600"><br>
<b>Figure 3.</b> Time-space diagram of Rule 90 with one "alive" cell in an inital row of cells.
</td>

<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule90_with_random_inital_values.png" width="600"><br>
<b>Figure 4.</b> Time-space diagram of Rule 90 with random inital row of cells.
</td>
</tr>

<tr>
<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule110_with_one_alive_inital_cell.png" width="600"><br>
<b>Figure 5.</b> Time-space diagram of Rule 110 with one "alive" cell in an inital row of cells.
</td>

<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule110_with_random_initial_values.png" width="600"><br>
<b>Figure 6.</b> Time-space diagram of Rule 110 with random inital row of cells.
</td>
</tr>

<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule150_with_one_alive_inital_cell.png" width="600"><br>
<b>Figure 7.</b> Time-space diagram of Rule 150 with one "alive" cell in an inital row of cells.
</td>

<td align="center">
<img src="/docs/elementary_cellular_auotmata_img/rule150_with_random_inital_values.png " width="600"><br>
<b>Figure 8.</b> Time-space diagram of Rule 150 with random inital row of cells.
</td>
</table>

# Use of AI

AI will be used to timeline this entire project, but the coding and architecture design of the project will be
done not using any AI tools / chatbot / agent / LLM.

# References

1. The Nature of Code: Simulating Natural Systems with JavaScript by Daniel Shiffman [https://natureofcode.com/]
2. Elementary cellular automaton by Wikipedia [https://en.wikipedia.org/wiki/Elementary_cellular_automaton#Rule_150]
