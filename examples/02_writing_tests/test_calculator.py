"""
Exercise 02 — Writing Tests with Copilot
==========================================
Write tests for the Calculator class. Let Copilot help you fill in each TODO.

Instructions:
  1. Read calculator.py to understand the Calculator class.
  2. Place your cursor after each TODO comment.
  3. Start typing an assertion and let Copilot complete it.
  4. Run: pytest examples/02_writing_tests/test_calculator.py -v
"""

import pytest
from calculator import Calculator


# ---------------------------------------------------------------------------
# Fixture — creates a fresh Calculator for each test
# ---------------------------------------------------------------------------
@pytest.fixture
def calc():
    return Calculator()


# ---------------------------------------------------------------------------
# BASIC OPERATIONS
# ---------------------------------------------------------------------------

class TestAdd:
    def test_add_positive_numbers(self, calc):
        # TODO: Test that add(2, 3) returns 5
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc):
        # TODO: Test that add(-1, -1) returns -2
        assert calc.add(-1, -1) == -2

    def test_add_zero(self, calc):
        # TODO: Test that adding zero doesn't change the value
        assert calc.add(5, 0) == 5


class TestSubtract:
    def test_subtract_positive(self, calc):
        # TODO: Test that subtract(10, 4) returns 6
        assert calc.subtract(10, 4) == 6

    def test_subtract_negative_result(self, calc):
        # TODO: Test subtraction that produces a negative result
        assert calc.subtract(4, 10) == -6


class TestMultiply:
    def test_multiply_positive(self, calc):
        # TODO: Test that multiply(3, 4) returns 12
        assert calc.multiply(3, 4) == 12

    def test_multiply_by_zero(self, calc):
        # TODO: Test that multiplying by zero returns 0
        assert calc.multiply(5, 0) == 0


class TestDivide:
    def test_divide_evenly(self, calc):
        # TODO: Test that divide(10, 2) returns 5.0
        assert calc.divide(10, 2) == 5.0

    def test_divide_with_remainder(self, calc):
        # TODO: Test that divide(7, 2) returns 3.5
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self, calc):
        # TODO: Test that dividing by zero raises ValueError
        # Hint: use pytest.raises(ValueError)
        with pytest.raises(ValueError):
            calc.divide(10, 0)


# ---------------------------------------------------------------------------
# ADVANCED OPERATIONS
# ---------------------------------------------------------------------------

class TestPower:
    def test_power_basic(self, calc):
        # TODO: Test that power(2, 3) returns 8
        assert calc.power(2, 3) == 8

    def test_power_of_zero(self, calc):
        # TODO: Test that any number to the power of 0 is 1
        assert calc.power(5, 0) == 1

class TestSquareRoot:
    def test_square_root_perfect(self, calc):
        # TODO: Test that square_root(9) returns 3.0
        assert calc.square_root(9) == 3.0
    def test_square_root_negative_raises(self, calc):
        # TODO: Test that square_root of a negative number raises ValueError
        with pytest.raises(ValueError):
            calc.square_root(-1)

# ---------------------------------------------------------------------------
# HISTORY TRACKING
# ---------------------------------------------------------------------------

class TestHistory:
    def test_history_starts_empty(self, calc):
        # TODO: Test that a new calculator has empty history
        assert calc.history == []
    def test_history_records_results(self, calc):
        # TODO: Perform a few operations and check the history list
        calc.add(1, 2)  # 3
    def test_clear_history(self, calc):
        # TODO: Add some results, clear history, verify it's empty
        calc.add(1, 2)  # 3
        calc.multiply(3, 4)  # 12
        calc.clear_history()
        assert calc.history == []

    def test_last_result(self, calc):
        # TODO: Perform operations and check last_result returns the most recent
        calc.add(1, 2)  # 3
        assert calc.last_result() == 3

    def test_last_result_empty(self, calc):
        # TODO: Test that last_result returns None when history is empty
        assert calc.last_result() is None
        