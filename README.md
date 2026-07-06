# Celluar Automata Research

> [!Warning]
> This way of hashing a password isn't safe at all and requires extensive
> cryptanalysis done to make sure its safe.

Can celluar automata produce cryptographic like properties similar to hash
functions? That is the main question this repository will try to answer and
compare against the SHA-256 algorithm.

This project uses Python 3.14.4 as the primary programing language and uses
matplotlib for statistical output and visualizing the image created using
different rule sets. Also uses hashlib module to make the comparison.

# Features Implemented

1. Basic wolfram cellular automata engine.
2. Rule 30, Rule 90, Rule 110, and Rule 150.
3. A class to create custom rule sets different from preloaded rule sets.
4. Basic encoder to encode ASCII to initial cellular automata engine state.
5. Basic decoder to decode final cellular automata state to ASCII.
6. A simple cellular automata visualizer for the terminal and matplotlib.

# Features To Be Implemented

1. Basic digest generator that adheres to the following properties:
   - One Way: cannot reverse-engineer to determine the original password.
   - Deterministic: running the exact password through the same formula will
     always produce the same digest.
   - Fixed Length: no matter how long or short a password is, it always creates
     a digest of the same size.
   - Avalanche Effect: making small changes in the password results in darastic
     changes in the digest.
   - Collision Resistant: makes it nearly impossible for two different passwords
     to output the same digest.
   - Salted: adds random characters at the end of the password before it goes
     through the generator.

2. A method in CaHashEngine that uses different rule sets for each generation
   based on a condition that an algorithm decides instead of having only one rule
   set applied over and over again.

3. A statistics visualizer to see how the password is changing through each
   generation and determine some measure to see how much the original password has
   been scrambled by the end.

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

# Use of AI

AI will be used to timeline this entire project, but the coding and architecture design of the project will be
done not using any AI tools / chatbot / agent / LLM.

# References

1. The Nature of Code: Simulating Natural Systems with JavaScript by Daniel
   Shiffman [https://natureofcode.com/]
2. Elementary cellular automaton by Wikipedia
   [https://en.wikipedia.org/wiki/Elementary_cellular_automaton#Rule_150]
