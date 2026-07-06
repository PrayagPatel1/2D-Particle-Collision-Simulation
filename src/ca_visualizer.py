"""Cellular Automaton Visualizer

This module provides a way to be able to visualize elementary cellular automata
either in the terminal or in matplotlib as static 2D images where every new row 
of the image represents a new generation that the automata has evolves by 
applying some rule set. 

Exported Classes:
CaVisualizer : a system to manage cellular automata visuals through the terminal
               or matplotlib.
"""

from ca_engine import *

from matplotlib.pyplot import plot as plt

class CaVisualizer:
    """
    A manager that manages how elementary cellular automata is visualized to the
    client in a static form. Every row within the image represents a new 
    generation of Cell objects. 

    Attributes
    ----------
    cell_matrix : list[list[Cell]]
        Represents the evolution of Cells from an inital array of cells.
    terminal_visual : bool
        Whether the client wants to visualize the cell_matrix in the terminal.
    matplot_visual : bool
        Whether the client wants to visualize the cell_matrix in matplotlib.
    
    Methods
    -------
    render_to_terminal 
        Renders the cell_matrix to the terminal. 
    render_to_matplot
        Renders the cell_matrix to matplot.
    """

    def __init__(self, cell_matrix: list[list[Cell]], terminal_visual: bool, 
                 matplot_visual: bool) -> None:
        self.cell_matrix = cell_matrix
        self.terminal_visual = terminal_visual
        self.matplot_visual = matplot_visual
    
    def render_to_terminal(self) -> None:
        """
        Renders the cell_matrix to the terminal. A Cell object that has a 
        state of 1 will be represented by a space character. A Cell object that
        has a state of 0 will be represented by a block character
        """

        if not self.terminal_visual:
            print("ERROR: Can't render to the terminal as <terminal_visual> is" \
                  "set to False.")
            return
        
        for gen_idx in range(len(self.cell_matrix)):
            for cell_idx in range(len(self.cell_matrix[0])):
                if self.cell_matrix[gen_idx][cell_idx].get_state() == CELL_ALIVE:
                    print(" ", end="")
                elif self.cell_matrix[gen_idx][cell_idx].get_state() == CELL_DEAD:
                    print("\u2588", end="")

            print("\n")
    
    def render_to_matplot(self) -> None:
        """
        Renders the cell_matrix to matplotlib. A Cell object that has a state of
        1 will be represented by a black box. A Cell object that has a state of
        0 will be represented by a white box character. 
        """

        if not self.matplot_visual:
            print("ERROR: Can't render to matplotlib as <matplot_visual> is set" \
                  "to False")
            return
        
        state_matrix = [[self.cell_matrix[gen_idx][cell_idx].get_state() 
                         for cell_idx in range(len(self.cell_matrix[0]))] 
                         for gen_idx in range(len(self.cell_matrix))]
        
        plt.figure(figsize=(10, 6))
        plt.imshow(state_matrix, cmap='binary', interpolation='nearest')
        plt.show()
