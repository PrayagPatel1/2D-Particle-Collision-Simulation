""" Celluar Automata Hash Engine 

This module provides a celluar automata engine that defines what a cell is and
a manager to coordinate a collection of cells organized in a grid. Additionally, 
it contains different rules that defines behaviours of celluar automata. As well
, this engine will be used to hash a password. 

Exported Classes:
Cell: a single unit with a binary state of "alive" or "dead". 
CaHashEngine: a global manager of a collection of Cells that uses elementary 
              celluar automata to hash a password.
"""
# Python Built-In Imports and thrid-party libraries
import random
import matplotlib.pyplot as plt

# Custom Imports
from elem_rule_set import ElementaryRule

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

    def __init__(self, state=None) -> None:
        if state == None:
            self._state = random.randint(CELL_DEAD, CELL_ALIVE)
        else:
            self._state = state
    
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

    Methods
    -------
    update
        Updates the inital array of cells using a specific ruleset. 
    render
        Renders a 2D image representing how each cell has evolved through
        the rulesets. Each row represents a new generation of the previous
        cells. 
    """

    def __init__(self, array_length: int, num_of_gen: int) -> None:

        # TODO: Would it be a good design choice to completely limit the client
        #       from being able to create more than one instance of 
        #       CaHashEngine?

        self.array_length = array_length
        self.num_of_gen = num_of_gen

        cell_array = [Cell() for _ in range(self.array_length)]
        self._cell_matrix = [cell_array if i == 0 else [0] * self.array_length 
                             for i in range(self.num_of_gen)]
    
    def _apply_rule_set(self, old_arr: list[Cell], 
                        rule_tble: dict[list[int], int]) -> list[Cell]:
        new_arr = []
        new_state = 0
        for cell_idx in range(self.array_length):
            if cell_idx == 0: 
                new_state = rule_tble[(CELL_DEAD, 
                                       old_arr[cell_idx].get_state(), 
                                       old_arr[cell_idx + 1].get_state())]
                new_arr.append(Cell(new_state))
            elif cell_idx == self.array_length - 1:
                new_state = rule_tble[(old_arr[cell_idx - 1].get_state(), 
                                       old_arr[cell_idx].get_state(), 
                                       CELL_DEAD)]
                
                new_arr.append(Cell(new_state))
            else:
                new_state = rule_tble[(old_arr[cell_idx - 1].get_state(), 
                                       old_arr[cell_idx].get_state(), 
                                       old_arr[cell_idx + 1].get_state())]
                new_arr.append(Cell(new_state))

        return new_arr 
    
    def update(self, rule: ElementaryRule) -> None:
        """Updates the previous array of cells using a ruleset."""
        for gen_idx in range(1, self.num_of_gen):
            self._cell_matrix.pop(gen_idx)
            new_arr = self._apply_rule_set(self._cell_matrix[gen_idx - 1], 
                                           rule.rule_table)
            self._cell_matrix.insert(gen_idx, new_arr)

    def render_to_terminal(self) -> None:
        """
        Renders every array of cells which has evolved to the terminal where a 
        "dead cell" is represented by a space character and an "alive" cell is 
        represented by a block character.  
        """
        for gen_idx in range(self.num_of_gen):
            for cell_idx in range(self.array_length):
                if self._cell_matrix[gen_idx][cell_idx].get_state() == CELL_ALIVE:
                    print(" ", end="")
                elif self._cell_matrix[gen_idx][cell_idx].get_state() == CELL_DEAD:
                    print("\u2588", end="")

            print("\n")
    
    def render_matplotlib(self) -> None:
        """
        Renders every array of cells which has evolved on a matplotlib graph, 
        where the x-axis represents the space the cellular automata has filled
        out and the y-axis which represents the time or generations the initial
        cell of array has gone through. 
        """
        # Convert the cell matrix to a 2D array of cell states
        state_matrix = [[self._cell_matrix[gen_idx][cell_idx].get_state() 
                         for cell_idx in range(self.array_length)] 
                         for gen_idx in range(self.num_of_gen)]
        
        plt.figure(figsize=(10, 6))
        plt.imshow(state_matrix, cmap='binary', interpolation='nearest')
        plt.title(f"Cellular Automata of {self.num_of_gen} Generations")
        plt.colorbar()
        plt.show()

if __name__ == "__main__":
    engine = CaHashEngine(101, 50)
    rule30 = ElementaryRule([0, 0, 0, 1, 1, 1, 1, 0])
    engine.update(rule30)
    # engine.render_to_terminal()
    engine.render_matplotlib()

    