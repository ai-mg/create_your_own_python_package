"""Calculator module providing basic arithmetic operations."""

from typing import Union

Number = Union[int, float]


class Calculator:
    """A simple calculator class demonstrating type hints and docstrings.

    This calculator provides basic arithmetic operations with type safety
    and comprehensive documentation.

    Example:
        >>> calc = Calculator()
        >>> result = calc.add(5, 3)
        >>> print(result)
        8
    """

    def __init__(self) -> None:
        """Initialize the calculator."""
        self.history: list[str] = []

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Example:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a.

        Args:
            a: Number to subtract from
            b: Number to subtract

        Returns:
            Difference of a and b
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Number, b: Number) -> float:
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self) -> list[str]:
        """Get calculation history.

        Returns:
            List of calculation strings
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
