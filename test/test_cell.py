import pytest
from src.ca_engine import Cell

def test_cell_random_init() -> None:
    random_cell = Cell()
    assert random_cell.get_state() in (0, 1)

def test_cell_state_init() -> None:
    cell_alive = Cell(state=1)
    cell_dead = Cell(state=0)

    assert cell_alive.get_state() == 1
    assert cell_dead.get_state() == 0
