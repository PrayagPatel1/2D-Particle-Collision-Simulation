"""Elementary Rule Set 

This module provides elementary rules for a one dimension cellular automaton, 
assigning all eight possible neighborhood congiurations defined in NeighConfig
enum class to either one or zero. One represents the Cell object as being "alive"
and zero represents the Cell object as being "dead". 

Exported Classes:
NeighConfig : an enum class that defines all eight possible neighborhoods for a 
              one dimensional cellular automaton. 
ElementaryRule : a lookup table system that assigns a neighborhood configuration
                 a binary state of 1 for the new Cell object to be "alive" or
                 0 for the new Cell object to be "dead". 
"""

from enum import Enum

# class NeighConfig(Enum):
#     """
#     Constants that represents all eight possible neigborhood configurations of
#     an elementary cellular automaton system (2 states, size 3 neighborhood) as
#     listed below:

#     111 | 110 | 101 | 100 | 011 | 010 | 001 | 000
#     """
#     ALL_ACTIVE = [1, 1, 1]
#     LEFT_CENTER_ACTIVE = [1, 1, 0]
#     LEFT_RIGHT_ACTIVE = [1, 0, 1]
#     LEFT_ACTIVE = [1, 0, 0]
#     CENTER_RIGHT_ACTIVE = [0, 1, 1]
#     CENTER_ACTIVE = [0, 1, 0]
#     RIGHT_ACTIVE = [0, 0, 1]
#     NONE_ACTIVE = [0, 0, 0]

class ElementaryRule:
    """
    A lookup table that takes in three parameters: [left, center, right] which 
    are the positions of the current Cell object and assigns a new state which 
    is either 1 for "alive" or 0 for "dead". 

    Attributes
    ----------
    rule_table : dict(NeighConfig : int)
        A table where every key is a configuration of a cells possible neighbor
        of size 3 (includeing the current cell) and the value is a new state
        for the next generation. The jey are ordered in descending binary 
        values.

    Methods
    -------
    clear_rule_table
        Clears all values within the lookup table. 
    """

    def __init__(self, rule: list[int]) -> None:
        if len(rule) != 8: 
            print("ERROR: The rule list must be of length 8.")
            return
    
        self.rule_table = {
            (1, 1, 1) : rule[0],
            (1, 1, 0) : rule[1],
            (1, 0, 1) : rule[2], 
            (1, 0, 0) : rule[3],
            (0, 1, 1) : rule[4], 
            (0, 1, 0) : rule[5], 
            (0, 0, 1) : rule[6], 
            (0, 0, 0) : rule[7] 
        }
    
    def clear_rule_table(self) -> None:
        """Clears all values from the <rule_table> leaving only the keys."""
        for neigh in self.rule_table.keys:
            self.rule_table[neigh] = None
    
    def __repr__(self) -> str:
        #TODO: Fix the representation of this object. 
        pass
    
    def __str__(self):
        self.__repr__

