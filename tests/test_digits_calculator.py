"""
Integration tests for digits_calculator module.

These tests verify that the Rust functions are properly exposed to Python
and work correctly with Python data types. Tests use pytest best practices
with parametrization, fixtures, and proper exception handling.
"""

import math

import pytest

import digits_calculator


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def pi_actual():
    """Fixture providing the actual value of pi."""
    return math.pi


# ============================================================================
# Test Suite: calculate_pi
# ============================================================================


class TestCalculatePi:
    """Test suite for the calculate_pi function."""

    @pytest.mark.parametrize("iterations,expected_range", [
        (0, (0.0, 0.0)),
        (1, (3.5, 4.5)),
        (10, (2.0, 4.0)),
        (100, (2.5, 3.5)),
    ])
    def test_calculate_pi_ranges(self, iterations, expected_range):
        """Test calculate_pi returns values in expected ranges for various iteration counts."""
        result = digits_calculator.calculate_pi(iterations)
        assert isinstance(result, float), "Result should be a float"
        assert expected_range[0] <= result <= expected_range[1], (
            f"Pi({iterations}) should be between {expected_range[0]} and {expected_range[1]}"
        )

    @pytest.mark.parametrize("iterations,max_error", [
        (1_000, 0.01),
        (10_000, 0.001),
        (1_000_000, 0.001),
    ])
    def test_calculate_pi_accuracy(self, iterations, max_error, pi_actual):
        """Test calculate_pi accuracy improves with iterations."""
        result = digits_calculator.calculate_pi(iterations)
        error = abs(result - pi_actual)
        assert error < max_error, (
            f"{iterations} iterations: error {error} exceeds max {max_error}"
        )

    def test_calculate_pi_consistency(self):
        """Test that multiple calls with same input produce same result."""
        result1 = digits_calculator.calculate_pi(10000)
        result2 = digits_calculator.calculate_pi(10000)
        assert result1 == result2, "Same input should produce identical output"

    def test_calculate_pi_returns_float(self):
        """Test that calculate_pi always returns a float."""
        result = digits_calculator.calculate_pi(100)
        assert isinstance(result, float), "Result should be float type"

    def test_calculate_pi_improves_with_iterations(self, pi_actual):
        """Test that accuracy improves as iterations increase."""
        errors = []
        for iterations in [100, 1_000, 10_000]:
            result = digits_calculator.calculate_pi(iterations)
            error = abs(result - pi_actual)
            errors.append(error)

        # Each successive result should be more accurate
        assert errors[0] > errors[1] > errors[2], (
            f"Errors should decrease: {errors}"
        )




# ============================================================================
# Test Suite: sum_as_string
# ============================================================================


class TestSumAsString:
    """Test suite for the sum_as_string function."""

    @pytest.mark.parametrize("a,b,expected", [
        (10, 20, "30"),
        (0, 0, "0"),
        (5, 0, "5"),
        (0, 10, "10"),
        (1_000_000, 2_000_000, "3000000"),
    ])
    def test_sum_as_string_results(self, a, b, expected):
        """Test sum_as_string with various input pairs."""
        result = digits_calculator.sum_as_string(a, b)
        assert result == expected, f"sum_as_string({a}, {b}) should return '{expected}'"

    def test_sum_as_string_returns_string(self):
        """Test that sum_as_string always returns a string."""
        result = digits_calculator.sum_as_string(10, 20)
        assert isinstance(result, str), "Result should be string type"

    def test_sum_as_string_consistency(self):
        """Test that multiple calls produce consistent results."""
        result1 = digits_calculator.sum_as_string(100, 200)
        result2 = digits_calculator.sum_as_string(100, 200)
        assert result1 == result2 == "300", "Consistent results for same inputs"

    def test_sum_as_string_commutative(self):
        """Test that addition is commutative."""
        result1 = digits_calculator.sum_as_string(10, 20)
        result2 = digits_calculator.sum_as_string(20, 10)
        assert result1 == result2 == "30", "Addition should be commutative"


# ============================================================================
# Test Suite: Module Integration
# ============================================================================


class TestModuleIntegration:
    """Test suite for module integration and attributes."""

    @pytest.mark.parametrize("function_name", [
        "calculate_pi",
        "sum_as_string",
        "divide",
        "safe_sqrt",
        "factorial",
    ])
    def test_module_exports_function(self, function_name):
        """Test that module exports all expected functions."""
        assert hasattr(digits_calculator, function_name), (
            f"Module should have {function_name} function"
        )

    @pytest.mark.parametrize("function_name", [
        "calculate_pi",
        "sum_as_string",
        "divide",
        "safe_sqrt",
        "factorial",
    ])
    def test_exported_functions_are_callable(self, function_name):
        """Test that all exported functions are callable."""
        func = getattr(digits_calculator, function_name)
        assert callable(func), f"{function_name} should be callable"


# ============================================================================
# Test Suite: Exception Handling
# ============================================================================


class TestDivide:
    """Test suite for divide function with exception handling."""

    @pytest.mark.parametrize("a,b,expected", [
        (10.0, 2.0, 5.0),
        (7.0, 2.0, 3.5),
        (-10.0, 2.0, -5.0),
        (10.0, -2.0, -5.0),
        (-10.0, -2.0, 5.0),
    ])
    def test_divide_valid_operations(self, a, b, expected):
        """Test divide with various valid inputs."""
        result = digits_calculator.divide(a, b)
        assert abs(result - expected) < 1e-10, (
            f"divide({a}, {b}) should equal {expected}"
        )

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            digits_calculator.divide(10.0, 0.0)

    def test_divide_by_zero_message(self):
        """Test that division by zero error contains proper message."""
        with pytest.raises(ZeroDivisionError, match="Division by Zero"):
            digits_calculator.divide(10.0, 0.0)


class TestSafeSqrt:
    """Test suite for safe_sqrt function with exception handling."""

    @pytest.mark.parametrize("x,expected", [
        (0.0, 0.0),
        (1.0, 1.0),
        (4.0, 2.0),
        (9.0, 3.0),
        (16.0, 4.0),
        (2.0, math.sqrt(2.0)),
    ])
    def test_safe_sqrt_valid_inputs(self, x, expected):
        """Test safe_sqrt with valid positive inputs."""
        result = digits_calculator.safe_sqrt(x)
        assert abs(result - expected) < 1e-10, (
            f"safe_sqrt({x}) should equal {expected}"
        )

    def test_safe_sqrt_negative_raises_error(self):
        """Test that sqrt of negative number raises ValueError."""
        with pytest.raises(ValueError):
            digits_calculator.safe_sqrt(-9.0)

    def test_safe_sqrt_negative_message(self):
        """Test that negative sqrt error contains proper message."""
        with pytest.raises(ValueError, match="negative"):
            digits_calculator.safe_sqrt(-1.0)


class TestFactorial:
    """Test suite for factorial function with exception handling."""

    @pytest.mark.parametrize("n,expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (10, 3628800),
        (20, 2432902008176640000),
    ])
    def test_factorial_valid_inputs(self, n, expected):
        """Test factorial with various valid inputs."""
        result = digits_calculator.factorial(n)
        assert result == expected, f"factorial({n}) should equal {expected}"

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError):
            digits_calculator.factorial(-5)

    def test_factorial_negative_message(self):
        """Test that negative factorial error contains proper message."""
        with pytest.raises(ValueError, match="negative"):
            digits_calculator.factorial(-1)

