#!/usr/bin/env python
"""
Main entry point for the rust-with-python template project.

This module demonstrates the integration of Python and Rust using PyO3.
It showcases how to call high-performance Rust functions from Python.

Usage:
    python main.py
"""

import digits_calculator


def main() -> None:
    """
    Run demonstration of Python-Rust integration.

    This function calls Rust functions exposed via the digits_calculator module
    and displays the results.
    """
    print("=" * 70)
    print("Welcome to rust-with-python!")
    print("Demonstrating Python and Rust Integration with PyO3")
    print("=" * 70)
    print()

    # Test calculate_pi function from Rust
    print("📊 Testing calculate_pi function (Rust Implementation):")
    print("-" * 70)
    pi_value = digits_calculator.calculate_pi(1_000_000)
    print("π approximation (1,000,000 iterations using Leibniz formula):")
    print(f"  Result:   {pi_value}")
    print("  Expected: 3.141592653589793")
    print(f"  Error:    {abs(3.141592653589793 - pi_value):.10f}")
    print()

    # Test sum_as_string function from Rust
    print("🔢 Testing sum_as_string function (Rust Implementation):")
    print("-" * 70)
    a, b = 10, 20
    result = digits_calculator.sum_as_string(a, b)
    print(f"Sum of {a} + {b} = {result}")
    print()

    print("=" * 70)
    print("✅ All demonstrations completed successfully!")
    print("=" * 70)
    print()
    print("For more examples and documentation, see README.md")


if __name__ == "__main__":
    main()
