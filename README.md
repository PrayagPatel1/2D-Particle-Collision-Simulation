# Celluar Automata as Hash Function

> [!Warning]
> This way of hashing a password isn't safe at all and requires extensive
> cryptanalysis done to make sure its safe.

Can celluar automata produce cryptographic like properties similar to hash
functions? That is the main question this repository will try to answer showcase some statistics of this engine without any optimizations done (may change in the future).

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
7. Statistic functions that measure the performance of the cellular automata
   based hash engine.

# Cellular Automaton Hash Engine Performance

## Initial Setup

The initial setup used through the meausre of how well a cellular based hash
engine worked was to generate 10,000 random printable ASCII character passwords, use Rule 30 for its pseudorandom behaviour, and have varying generations that the input passwords will have to go through (from 8 to 256).

The type of statistics that were collected is histogram plots of the ASCII character frequency from generation 8 to generation 256, heatmaps that showed how frequency certain byte pair occurs within the hash passwords, and the chi-square goodness of fit distribution.

## ASCII Character Frequency

Having collected the frequency of every ASCII character from ordinal values of
0 to 256 and used a histogram to plot out the frequency at every generations we have the following below,

<table>
  <!-- Row 1 -->
  <tr>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/ASCII Character Frequency Plots/rule_30_gen_8.png" alt="First Image Description" width="100%">
        <figcaption><b>Figure 1:</b> ASCII character frequency count of 10,000 hashed passwords, using Rule 30, for 8 generations.</figcaption>
      </figure>
    </td>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/ASCII Character Frequency Plots/rule_30_gen_16.png" alt="Second Image Description" width="100%">
        <figcaption><b>Figure 2:</b> ASCII character frequency count of 10,000 hashed passwords, using Rule 30, for 16 generations.</figcaption>
      </figure>
    </td>
  </tr>

  <!-- Row 2 -->
  <tr>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/ASCII Character Frequency Plots/rule_30_gen_32.png" alt="Third Image Description" width="100%">
        <figcaption><b>Figure 3:</b> ASCII character frequency count of 10,000 hashed passwords, using Rule 30, for 32 generations.</figcaption>
      </figure>
    </td>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/ASCII Character Frequency Plots/rule_30_gen_64.png" alt="Fourth Image Description" width="100%">
        <figcaption><b>Figure 4:</b> ASCII character frequency count of 10,000 hashed passwords, using Rule 30, for 64 generations.</figcaption>
      </figure>
    </td>
  </tr>
  
  <!-- Row 3 -->
  <tr>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/ASCII Character Frequency Plots/rule_30_gen_128.png" alt="Fifth Image Description" width="100%">
        <figcaption><b>Figure 5:</b> ASCII character frequency count of 10,000 hashed passwords, using Rule 30, for 128 generations.</figcaption>
      </figure>
    </td>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/ASCII Character Frequency Plots/rule_30_gen_256.png" alt="Sixth Image Description" width="100%">
        <figcaption><b>Figure 6:</b> ASCII character frequency count of 10,000 hashed passwords, using Rule 30, for 256 generations.</figcaption>
      </figure>
    </td>
  </tr>
</table>

From the six figures above, we can see that the count are slowly approaching an
equalibrium state where almost all characters are occuring at the same count. This indicates that for a long enough time as you increase the generation, the
count of the characters will occur 50% of the time. This indicates that the hash engine allocates all bins evenly when generating a hash.

## Byte Pair Heatmap

To get another perspective of the ASCII character frequency, the byte pair heatmap allows to count the number of times that a byte pair occurs within every hashed password. Since each password is 8 characters long, which is equivalent to 8 bytes on most systems, there will be 7 byte pairs that needs to be considered for every hash password. Running 10,000 input passwords, to get 10,000 hash passwords, a total of 70,000 byte pairs will need to be accounted for. The dimensions of the heatmap is 256 bytes by 256 bytes to account for all ASCII character values (in decimal form).

Below are the siz heatmaps collected for all six generation variations,

<table>
  <!-- Row 1 -->
  <tr>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/Byte-Pair Heatmap Plot/rule_30_gen_8.png" alt="First Image Description" width="100%">
        <figcaption><b>Figure 1:</b> Byte pair heatmap for 10,000 hashed passwords for 8 generations.</figcaption>
      </figure>
    </td>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/Byte-Pair Heatmap Plot/rule_30_gen_16.png" alt="Second Image Description" width="100%">
        <figcaption><b>Figure 2:</b> Byte pair heatmap for 10,000 hashed passwords for 16 generations.</figcaption>
      </figure>
    </td>
  </tr>

  <!-- Row 2 -->
  <tr>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/Byte-Pair Heatmap Plot/rule_30_gen_32.png" alt="Third Image Description" width="100%">
        <figcaption><b>Figure 3:</b> Byte pair heatmap for 10,000 hashed passwords for 32 generations.</figcaption>
      </figure>
    </td>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/Byte-Pair Heatmap Plot/rule_30_gen_64.png" width="100%">
        <figcaption><b>Figure 4:</b> Byte pair heatmap for 10,000 hashed passwords for 64 generations.</figcaption>
      </figure>
    </td>
  </tr>
  
  <!-- Row 3 -->
  <tr>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/Byte-Pair Heatmap Plot/rule_30_gen_128.png" alt="Fifth Image Description" width="100%">
        <figcaption><b>Figure 5:</b> Byte pair heatmap for 10,000 hashed passwords for 128 generations.</figcaption>
      </figure>
    </td>
    <td align="center" valign="top" width="50%">
      <figure>
        <img src="./images/Byte-Pair Heatmap Plot/rule_30_gen_256.png" alt="Sixth Image Description" width="100%">
        <figcaption><b>Figure 6:</b> Byte pair heatmap for 10,000 hashed passwords for 256 generations.</figcaption>
      </figure>
    </td>
  </tr>
</table>

The data here suggests that even on the 8th generation, Rule 30 acheives the avalanche / uniformity properties you would want from a hash-design perspective. The generation count can then be reduced a substantial amount to get a uniform hash behaviour.

## Chi-Square Goodness of Fit Distribution

The chi-square statistic here gives a more qunatifiable backing to the heatmap statistics which by eye can be seen to be more or less uniform. Below is the distribution and the shaded orange area represents the p-value:

![Chi-Square Distribution](./images/Chi-Square%20Distribution%20Plot/chi_square_dstribution_for_10,000_pwds.png)

As one can see that the shaded reegion starts roughly around $\chi^s = 261$ and ends up at the tail of $\chi^2 = 320$. The shaded region sits near the mean of this distribution and covers roughly 35% to 40% meaning that it fails to reject the null hypothesis that the hash byte values are uniformly distributed.

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

Claude Sonnet 5 was used to timeline this project and used to implement the
CaHashEngine Unit tests.

# References

1. The Nature of Code: Simulating Natural Systems with JavaScript by Daniel
   Shiffman [https://natureofcode.com/]
2. Elementary cellular automaton by Wikipedia
   [https://en.wikipedia.org/wiki/Elementary_cellular_automaton#Rule_150]
