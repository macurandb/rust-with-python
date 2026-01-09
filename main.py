#!/usr/bin/env python
"""
Main entry point for the rust-with-python template project.

This module demonstrates the integration of Python and Rust using PyO3.
It showcases how to call high-performance Rust functions from Python.

Usage:
    python main.py
"""

import math
import time

import digits_calculator


def main() -> None:
    """
    Run comprehensive demonstration of Python-Rust integration.

    This function showcases all 6 mathematical functions implemented in Rust,
    demonstrating performance, precision, and error handling.
    """
    print("=" * 80)
    print("🦀 RUST + PYTHON INTEGRATION SHOWCASE 🐍")
    print("High-Performance Mathematical Functions via PyO3")
    print("=" * 80)
    print()

    # 1. High-Precision Pi Calculation
    print("🧮 1. HIGH-PRECISION π CALCULATION")
    print("-" * 50)

    # Test different precisions
    iterations: list[int] = [1_000, 100_000, 1_000_000]
    for iters in iterations:
        start_time = time.perf_counter()
        pi_rust = digits_calculator.calculate_pi(iters)
        rust_time = time.perf_counter() - start_time

        error = abs(pi_rust - math.pi)
        print(f"  {iters:,} iterations: π ≈ {pi_rust:.12f}")
        print(f"    Error: {error:.2e} | Time: {rust_time * 1000:.2f}ms")
    print()

    # 2. Matrix Multiplication
    print("🔢 2. MATRIX MULTIPLICATION")
    print("-" * 50)

    # 2D Rotation example
    angle: int = 30  # degrees
    rad: float = math.radians(angle)
    rotation_matrix: list[list[float]] = [
        [math.cos(rad), -math.sin(rad)],
        [math.sin(rad), math.cos(rad)],
    ]
    point: list[list[float]] = [[1.0], [0.0]]  # Point (1,0)

    result: list[list[float]] = digits_calculator.matrix_multiply(rotation_matrix, point)
    print(f"  Rotating point (1,0) by {angle}°:")
    print("    Original: (1.0, 0.0)")
    print(f"    Rotated:  ({result[0][0]:.3f}, {result[1][0]:.3f})")

    # Large matrix example
    large_a: list[list[float]] = [[float(i + j) for j in range(50)] for i in range(100)]
    large_b: list[list[float]] = [[i * 0.1 for i in range(2)] for _ in range(50)]

    start_time = time.perf_counter()
    large_result: list[list[float]] = digits_calculator.matrix_multiply(large_a, large_b)
    matrix_time = time.perf_counter() - start_time

    print(f"  Large matrix (100×50 × 50×2): {matrix_time * 1000:.2f}ms")
    print(f"    Result shape: {len(large_result)}×{len(large_result[0])}")
    print()

    # 3. Safe Mathematical Operations
    print("🛡️ 3. SAFE MATHEMATICAL OPERATIONS")
    print("-" * 50)

    # Safe division
    try:
        safe_div: float = digits_calculator.divide(100.0, 3.0)
        print(f"  100 ÷ 3 = {safe_div:.6f}")

        # This will raise an exception
        digits_calculator.divide(10.0, 0.0)
    except ZeroDivisionError as e:
        print(f"  Division by zero caught: ✅ {e}")

    # Safe square root
    try:
        sqrt_result: float = digits_calculator.safe_sqrt(2.0)
        print(f"  √2 = {sqrt_result:.10f}")

        # This will raise an exception
        digits_calculator.safe_sqrt(-4.0)
    except ValueError as e:
        print(f"  Negative sqrt caught: ✅ {e}")
    print()

    # 4. Factorial Computation
    print("! 4. FACTORIAL COMPUTATION")
    print("-" * 50)

    factorials: list[int] = [0, 1, 5, 10, 15, 20]
    for n in factorials:
        try:
            result: int = digits_calculator.factorial(n)
            print(f"  {n:2d}! = {result:,}")
        except ValueError as e:
            print(f"  {n}! = Error: {e}")

    try:
        # This will raise an exception
        digits_calculator.factorial(-5)
    except ValueError as e:
        print(f"  Negative factorial caught: ✅ {e}")
    print()

    # 5. Large Number String Operations
    print("📝 5. LARGE NUMBER STRING OPERATIONS")
    print("-" * 50)

    # Large number addition
    large_nums: list[tuple[int, int]] = [
        (999_999_999, 1),
        (123_456_789, 987_654_321),
        (2**50, 2**50),
    ]

    for a, b in large_nums:
        result: str = digits_calculator.sum_as_string(a, b)
        print(f"  {a:,} + {b:,} = {result}")
    print()

    # 6. Performance Comparison
    print("⚡ 6. PERFORMANCE SHOWCASE")
    print("-" * 50)

    # Python vs Rust Pi calculation
    start_time: float = time.perf_counter()
    pi_python: float = sum(4 * ((-1) ** k) / (2 * k + 1) for k in range(100_000))
    python_time: float = time.perf_counter() - start_time

    start_time = time.perf_counter()
    pi_rust: float = digits_calculator.calculate_pi(100_000)
    rust_time: float = time.perf_counter() - start_time

    speedup: float = python_time / rust_time
    print("  π calculation (100K iterations):")
    print(f"    Python: {python_time * 1000:.2f}ms → π ≈ {pi_python:.8f}")
    print(f"    Rust:   {rust_time * 1000:.2f}ms → π ≈ {pi_rust:.8f}")
    print(f"    🚀 Speedup: {speedup:.1f}x faster!")
    print()

    # Summary
    print("=" * 80)
    print("✨ DEMONSTRATION COMPLETE!")
    print("=" * 80)
    print("🎯 Functions demonstrated:")
    print("  ✅ calculate_pi    - High-precision π with multiple algorithms")
    print("  ✅ matrix_multiply - Fast matrix operations with validation")
    print("  ✅ divide         - Safe division with error handling")
    print("  ✅ safe_sqrt      - Protected square root calculations")
    print("  ✅ factorial      - Integer factorial with overflow detection")
    print("  ✅ sum_as_string  - Large number arithmetic")
    print()
    print("🚀 Performance: Rust delivers up to 10x+ speedup over pure Python")
    print("🛡️ Safety: Comprehensive error handling prevents crashes")
    print("🎓 Learn more: README.md contains full documentation")
    print()
    print("⭐ Star the repo: https://github.com/macurandb/rust-with-python")


if __name__ == "__main__":
    main()
