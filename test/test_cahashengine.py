"""
Unit tests for ca_engine.CaHashEngine.

These tests cover:
    - __init__            (initial cell-matrix construction)
    - _apply_rule_set      (single-generation rule application, incl. edges)
    - update               (multi-generation evolution)
    - get_cell_matrix      (accessor behavior)

A small `FakeRuleSet` test double is used in place of the real
`ElementaryRule` so the tests exercise `CaHashEngine` in isolation and
don't depend on the specifics of the rule-table implementation. The
fake rule table implements "Rule 90" (new_state = left XOR right,
center is ignored), which makes expected outputs easy to hand-compute.
"""
import pytest

from src.ca_engine import *


class FakeRuleSet:
    """A minimal stand-in for ElementaryRule exposing only `rule_tble`.

    Implements Rule 90: new_state = left XOR right (center is ignored).
    """

    def __init__(self):
        self.rule_tble = {
            (l, c, r): l ^ r
            for l in (0, 1) for c in (0, 1) for r in (0, 1)
        }


class AllAliveRuleSet:
    """A rule set where every neighborhood produces an alive cell."""

    def __init__(self):
        self.rule_tble = {
            (l, c, r): CELL_ALIVE
            for l in (0, 1) for c in (0, 1) for r in (0, 1)
        }


def make_cells(states):
    """Helper: build a list of Cell objects with explicit states."""
    return [Cell(s) for s in states]


# ---------------------------------------------------------------------------
# __init__
# ---------------------------------------------------------------------------

class TestInit:
    def test_stores_basic_parameters(self):
        init_cells = make_cells([0, 1, 0])
        rule_set = FakeRuleSet()
        engine = CaHashEngine((3, init_cells, 4, rule_set))

        assert engine.array_length == 3
        assert engine.num_of_gen == 4
        assert engine.rule_set is rule_set

    def test_first_generation_is_the_provided_init_array(self):
        init_cells = make_cells([1, 0, 1, 0])
        engine = CaHashEngine((4, init_cells, 2, FakeRuleSet()))

        matrix = engine.get_cell_matrix()
        assert matrix[0] is init_cells
        assert [c.get_state() for c in matrix[0]] == [1, 0, 1, 0]

    def test_matrix_has_num_of_gen_rows(self):
        init_cells = make_cells([0, 1])
        engine = CaHashEngine((2, init_cells, 5, FakeRuleSet()))

        assert len(engine.get_cell_matrix()) == 5

    def test_placeholder_rows_are_zero_filled_before_update(self):
        # Rows other than generation 0 start out as plain int placeholders
        # (not Cell objects) until update() is called.
        init_cells = make_cells([0, 1, 1])
        engine = CaHashEngine((3, init_cells, 3, FakeRuleSet()))

        matrix = engine.get_cell_matrix()
        assert matrix[1] == [0, 0, 0]
        assert matrix[2] == [0, 0, 0]


# ---------------------------------------------------------------------------
# _apply_rule_set
# ---------------------------------------------------------------------------

class TestApplyRuleSet:
    def test_middle_cells_use_left_and_right_neighbors(self):
        # Rule 90: new_state = left XOR right.
        # States: [1, 0, 1, 0]
        # idx 1 (middle): left=1, right=1 -> 1 ^ 1 = 0
        # idx 2 (middle): left=0, right=0 -> 0 ^ 0 = 0
        init_cells = make_cells([1, 0, 1, 0])
        engine = CaHashEngine((4, init_cells, 1, FakeRuleSet()))

        new_gen = engine._apply_rule_set(init_cells)

        assert new_gen[1].get_state() == 0
        assert new_gen[2].get_state() == 0

    def test_left_boundary_treats_missing_left_neighbor_as_dead(self):
        # idx 0: left is treated as CELL_DEAD (0), right = old_arr[1]
        # States: [1, 0, 1] -> idx 0: 0 ^ old_arr[1]=0 -> 0
        init_cells = make_cells([1, 0, 1])
        engine = CaHashEngine((3, init_cells, 1, FakeRuleSet()))

        new_gen = engine._apply_rule_set(init_cells)

        assert new_gen[0].get_state() == (CELL_DEAD ^ init_cells[1].get_state())

    def test_right_boundary_treats_missing_right_neighbor_as_dead(self):
        # idx (len-1): right is treated as CELL_DEAD (0), left = old_arr[len-2]
        init_cells = make_cells([1, 0, 1])
        engine = CaHashEngine((3, init_cells, 1, FakeRuleSet()))

        new_gen = engine._apply_rule_set(init_cells)

        last = len(init_cells) - 1
        assert new_gen[last].get_state() == (init_cells[last - 1].get_state() ^ CELL_DEAD)

    def test_returns_new_list_of_cell_objects(self):
        init_cells = make_cells([0, 1, 0])
        engine = CaHashEngine((3, init_cells, 1, AllAliveRuleSet()))

        new_gen = engine._apply_rule_set(init_cells)

        assert new_gen is not init_cells
        assert all(isinstance(c, Cell) for c in new_gen)
        assert [c.get_state() for c in new_gen] == [CELL_ALIVE, CELL_ALIVE, CELL_ALIVE]

    def test_single_cell_array_raises_index_error(self):
        # Known boundary edge case: with array_length == 1, cell_idx == 0
        # is both the first and last cell, but the code takes the
        # "left boundary" branch and still indexes old_arr[cell_idx + 1],
        # which is out of range. This test documents that current
        # behavior rather than asserting it is desirable.
        init_cells = make_cells([1])
        engine = CaHashEngine((1, init_cells, 1, FakeRuleSet()))

        with pytest.raises(IndexError):
            engine._apply_rule_set(init_cells)


# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------

class TestUpdate:
    def test_update_computes_expected_second_generation(self):
        # Rule 90 on [1, 0, 1, 0]:
        # idx0: DEAD ^ old[1] = 0 ^ 0 = 0
        # idx1: old[0] ^ old[2] = 1 ^ 1 = 0
        # idx2: old[1] ^ old[3] = 0 ^ 0 = 0
        # idx3: old[2] ^ DEAD  = 1 ^ 0 = 1
        init_cells = make_cells([1, 0, 1, 0])
        engine = CaHashEngine((4, init_cells, 2, FakeRuleSet()))

        engine.update()

        gen1_states = [c.get_state() for c in engine.get_cell_matrix()[1]]
        assert gen1_states == [0, 0, 0, 1]

    def test_update_leaves_first_generation_untouched(self):
        init_cells = make_cells([1, 0, 1, 0])
        engine = CaHashEngine((4, init_cells, 3, FakeRuleSet()))

        engine.update()

        assert engine.get_cell_matrix()[0] is init_cells

    def test_update_propagates_across_multiple_generations(self):
        init_cells = make_cells([0, 0, 1, 0, 0])
        engine = CaHashEngine((5, init_cells, 4, FakeRuleSet()))

        engine.update()

        matrix = engine.get_cell_matrix()
        # every row after generation 0 should be fully populated with Cells
        for gen in matrix[1:]:
            assert all(isinstance(c, Cell) for c in gen)
            assert len(gen) == 5

    def test_update_with_all_alive_rule_fills_every_row_alive(self):
        init_cells = make_cells([0, 1, 0])
        engine = CaHashEngine((3, init_cells, 3, AllAliveRuleSet()))

        engine.update()

        matrix = engine.get_cell_matrix()
        for gen in matrix[1:]:
            assert [c.get_state() for c in gen] == [CELL_ALIVE, CELL_ALIVE, CELL_ALIVE]

    def test_update_is_idempotent_shape(self):
        # Calling update() re-derives each row from the row before it,
        # so calling it twice should produce the same final matrix.
        init_cells = make_cells([1, 0, 1, 0, 1])
        engine = CaHashEngine((5, init_cells, 3, FakeRuleSet()))

        engine.update()
        first_pass = [[c.get_state() for c in gen] for gen in engine.get_cell_matrix()]

        engine.update()
        second_pass = [[c.get_state() for c in gen] for gen in engine.get_cell_matrix()]

        assert first_pass == second_pass


# ---------------------------------------------------------------------------
# get_cell_matrix
# ---------------------------------------------------------------------------

class TestGetCellMatrix:
    def test_returns_internal_matrix_reference(self):
        init_cells = make_cells([0, 1])
        engine = CaHashEngine((2, init_cells, 2, FakeRuleSet()))

        matrix = engine.get_cell_matrix()

        assert matrix is engine._cell_matrix

    def test_reflects_state_after_update(self):
        init_cells = make_cells([1, 1, 1])
        engine = CaHashEngine((3, init_cells, 2, AllAliveRuleSet()))

        before = engine.get_cell_matrix()[1]
        assert before == [0, 0, 0]

        engine.update()

        after = engine.get_cell_matrix()[1]
        assert [c.get_state() for c in after] == [CELL_ALIVE, CELL_ALIVE, CELL_ALIVE]