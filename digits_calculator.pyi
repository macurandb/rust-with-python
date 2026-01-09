"""Type stubs for digits_calculator module.

This file provides type annotations for the Rust extension module
to resolve basedpyright/pylsp type checking issues.
"""


def calculate_pi(iterations: int) -> float:
    """
    Calculates a high-precision approximation of Pi using optimized algorithms.

    Args:
        iterations: Number of iterations to perform

    Returns:
        High-precision approximation of π
    """
    ...

def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Multiplies two matrices.

    Args:
        a: First matrix as List[List[float]]
        b: Second matrix as List[List[float]]

    Returns:
        The resulting matrix

    Raises:
        ValueError: If dimensions are incompatible or matrices are malformed
    """
    ...

def divide(a: float, b: float) -> float:
    """
    Divides two numbers with proper error handling.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Result of a / b

    Raises:
        ZeroDivisionError: If b is zero
    """
    ...

def safe_sqrt(x: float) -> float:
    """
    Calculates the square root with validation.

    Args:
        x: Number to get square root of

    Returns:
        Square root of x

    Raises:
        ValueError: If x is negative
    """
    ...

def factorial(n: int) -> int:
    """
    Calculates factorial with boundary checking.

    Args:
        n: Number to calculate factorial for

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative
        OverflowError: If result is too large
    """
    ...

def sum_as_string(a: int, b: int) -> str:
    """
    Adds two integers and returns the result as a string.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Sum formatted as a string
    """
    ...
