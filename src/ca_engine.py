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

# Custom Imports
from elem_rule_set import *

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
        return f"Cell(state={self._state})"
    
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
    rule_set : ElementaryRule
        Represents the rule set that is going to be used to simulate the 
        elementary cellular automata.

    Methods
    -------
    update
        Updates the inital array of cells using a specific ruleset. 
    render
        Renders a 2D image representing how each cell has evolved through
        the rulesets. Each row represents a new generation of the previous
        cells. 
    """

    def __init__(self, engine_param: tuple[int, list[Cell], int, ElementaryRule]) -> None:

        # TODO: Would it be a good design choice to completely limit the client
        #       from being able to create more than one instance of 
        #       CaHashEngine?

        self.array_length, init_cell_arr, self.num_of_gen, self.rule_set = engine_param 

        self._cell_matrix = [init_cell_arr if i == 0 else [0] * self.array_length 
                             for i in range(self.num_of_gen)]
    
    def _apply_rule_set(self, old_arr: list[Cell]) -> list[Cell]:
        new_arr = []
        new_state = 0
        for cell_idx in range(self.array_length):
            if cell_idx == 0: 
                new_state = self.rule_set.rule_tble[(old_arr[len(old_arr) - 1].get_state(), 
                                       old_arr[cell_idx].get_state(), 
                                       old_arr[cell_idx + 1].get_state())]
                new_arr.append(Cell(new_state))
            elif cell_idx == self.array_length - 1:
                new_state = self.rule_set.rule_tble[(old_arr[cell_idx - 1].get_state(), 
                                       old_arr[cell_idx].get_state(), 
                                       old_arr[0].get_state())]
                
                new_arr.append(Cell(new_state))
            else:
                new_state = self.rule_set.rule_tble[(old_arr[cell_idx - 1].get_state(), 
                                       old_arr[cell_idx].get_state(), 
                                       old_arr[cell_idx + 1].get_state())]
                new_arr.append(Cell(new_state))

        return new_arr 
    
    def update(self) -> None:
        """Updates the previous array of cells using a ruleset."""
        for gen_idx in range(1, self.num_of_gen):
            self._cell_matrix.pop(gen_idx)
            new_arr = self._apply_rule_set(self._cell_matrix[gen_idx - 1])
            self._cell_matrix.insert(gen_idx, new_arr)

    def get_cell_matrix(self) -> list[list[Cell]]:
        """Returns the cell matrix."""
        return self._cell_matrix

# Different Ways to Initialize the first generation of cells

def init_cell_arr_random(array_length: int) -> list[Cell]:
    cell_array = [Cell() for _ in range(array_length)]
    return cell_array

def init_cell_array_one_alive(array_length: int) -> list[Cell]:
        cell_array = []
        for idx in range(array_length):
            if idx == ((array_length - 1) // 2):
                cell_array.append(Cell(CELL_ALIVE))
            cell_array.append(Cell(CELL_DEAD))
        return cell_array