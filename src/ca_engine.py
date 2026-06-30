""" Celluar Automata Engine 

This module provides a celluar automata engine that defines what a cell is and
a manager to coordinate a collection of cells organized in a grid. Additionally, 
it contains different rules that defines behaviours of celluar automata. 

Exported Classes:

Cell: a single unit with a binary state of "alive" or "dead". 
CAEngine: a global manager of a collection of Cells and defines different rules.
"""

import random

CELL_ALIVE = 1
CELL_DEAD = 0

class Cell:
    """ 
    A single bit that lives in a one dimension array with a binary state of 
    "dead" or "alive".

    Attributes
    ----------
    None

    Methods
    -------
    get_state() -> int
        Returns the state for the current cell. One represents the cell is 
        "alive" and zero represents the cell is "dead".
    """

    def __init__(self) -> None:
        self._state = random.randint(CELL_DEAD, CELL_ALIVE)
    
    def get_state(self) -> int:
        """Returns the state of the current Cell object."""
        return self._state

    def __repr__(self) -> str:
        return f"Cell(state={self._state}, neighbors={self._neighbors}, pos={self._pos})"
    
    def __str__(self):
        self.__repr__

class CaHashEngine:
    """
    A celluar automaton engine that coordinates Cell objects arranged in a 
    one dimension array using rule sets for hashing a password. 

    Attributes
    ----------
    array_length : int
        The length of an array of Cell objects.
    num_of_gen : int
        Number of total times for the inital array of cells to evolve. 
    """

    def __init__(self, array_length: int, num_of_gen: int) -> None:
        self.array_length = array_length
        self.num_of_gen = num_of_gen

        cell_array = [Cell() for _ in range(self.array_length)]
        self._cell_matrix = [cell_array if i == 0 else [0] * self.array_length for i in range(self.num_of_gen)]
    
    def rule_set_30(self, cell1: Cell, cell2: Cell, cell3: Cell) -> int:
        return cell1.get_state() ^ (cell2.get_state() | cell3.get_state())
    
    

    def render(self) -> None:
        for gen_idx in range(self.num_of_gen):
            for cell_idx in range(self.array_length):
                if self._cell_matrix[gen_idx][cell_idx].get_state() == CELL_ALIVE:
                    print("O", end="")
                elif self._cell_matrix[gen_idx][cell_idx].get_state() == CELL_DEAD:
                    print(".", end="")

            print("\n")

if __name__ == "__main__":
    engine = CaHashEngine(10, 1)
    engine.render()

    