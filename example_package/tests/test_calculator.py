"""Tests for the calculator module."""

import pytest

from example_package import Calculator


def test_calculator_add() -> None:
    """Test addition operation."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0.5, 0.3) == pytest.approx(0.8)


def test_calculator_subtract() -> None:
    """Test subtraction operation."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(10.5, 0.5) == pytest.approx(10.0)


def test_calculator_multiply() -> None:
    """Test multiplication operation."""
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0.5, 4) == pytest.approx(2.0)


def test_calculator_divide() -> None:
    """Test division operation."""
    calc = Calculator()
    assert calc.divide(6, 2) == pytest.approx(3.0)
    assert calc.divide(5, 2) == pytest.approx(2.5)
    assert calc.divide(-10, 2) == pytest.approx(-5.0)


def test_calculator_divide_by_zero() -> None:
    """Test division by zero raises ValueError."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


def test_calculator_history() -> None:
    """Test calculation history tracking."""
    calc = Calculator()

    calc.add(2, 3)
    calc.multiply(4, 5)

    history = calc.get_history()
    assert len(history) == 2
    assert "2 + 3 = 5" in history
    assert "4 * 5 = 20" in history


def test_calculator_clear_history() -> None:
    """Test clearing calculation history."""
    calc = Calculator()

    calc.add(1, 1)
    calc.subtract(5, 3)
    assert len(calc.get_history()) == 2

    calc.clear_history()
    assert len(calc.get_history()) == 0


@pytest.fixture
def calculator() -> Calculator:
    """Provide a calculator instance for tests."""
    return Calculator()


def test_with_fixture(calculator: Calculator) -> None:
    """Test using pytest fixture."""
    result = calculator.add(10, 20)
    assert result == 30
