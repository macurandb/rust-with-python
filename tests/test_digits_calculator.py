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
def pi_actual() -> float:
    """Fixture providing the actual value of pi."""
    return math.pi


# ============================================================================
# Test Suite: calculate_pi
# ============================================================================


class TestCalculatePi:
    """Test suite for the calculate_pi function."""

    @pytest.mark.parametrize(
        "iterations,expected_range",
        [
            (0, (0.0, 0.0)),
            (1, (3.5, 4.5)),
            (10, (2.0, 4.0)),
            (100, (2.5, 3.5)),
        ],
    )
    def test_calculate_pi_ranges(
        self, iterations: int, expected_range: tuple[float, float]
    ) -> None:
        """Test calculate_pi returns values in expected ranges for various iteration counts."""
        result: float = digits_calculator.calculate_pi(iterations)
        assert isinstance(result, float), "Result should be a float"
        assert expected_range[0] <= result <= expected_range[1], (
            f"Pi({iterations}) should be between {expected_range[0]} and {expected_range[1]}"
        )

    @pytest.mark.parametrize(
        "iterations,max_error",
        [
            (1_000, 0.01),
            (10_000, 0.001),
            (1_000_000, 0.001),
        ],
    )
    def test_calculate_pi_accuracy(
        self, iterations: int, max_error: float, pi_actual: float
    ) -> None:
        """Test calculate_pi accuracy improves with iterations."""
        result: float = digits_calculator.calculate_pi(iterations)
        error: float = abs(result - pi_actual)
        assert error < max_error, f"{iterations} iterations: error {error} exceeds max {max_error}"

    def test_calculate_pi_consistency(self) -> None:
        """Test that multiple calls with same input produce same result."""
        result1: float = digits_calculator.calculate_pi(10000)
        result2: float = digits_calculator.calculate_pi(10000)
        assert result1 == result2, "Same input should produce identical output"

    def test_calculate_pi_returns_float(self) -> None:
        """Test that calculate_pi always returns a float."""
        result: float = digits_calculator.calculate_pi(100)
        assert isinstance(result, float), "Result should be float type"

    def test_calculate_pi_improves_with_iterations(self, pi_actual: float) -> None:
        """Test that accuracy improves as iterations increase."""
        errors: list[float] = []
        for iterations in [100, 1_000, 10_000]:
            result: float = digits_calculator.calculate_pi(iterations)
            error: float = abs(result - pi_actual)
            errors.append(error)

        # Each successive result should be more accurate
        assert errors[0] > errors[1] > errors[2], f"Errors should decrease: {errors}"


# ============================================================================
# Test Suite: matrix_multiply
# ============================================================================


class TestMatrixMultiply:
    """Test suite for the matrix_multiply function."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (
                [[1.0, 2.0], [3.0, 4.0]],
                [[5.0, 6.0], [7.0, 8.0]],
                [[19.0, 22.0], [43.0, 50.0]],
            ),
            (
                [[1.0, 0.0], [0.0, 1.0]],
                [[5.0, 6.0], [7.0, 8.0]],
                [[5.0, 6.0], [7.0, 8.0]],
            ),
            ([[1.0, 2.0, 3.0]], [[4.0], [5.0], [6.0]], [[32.0]]),
        ],
    )
    def test_matrix_multiply_valid(
        self, a: list[list[float]], b: list[list[float]], expected: list[list[float]]
    ) -> None:
        """Test matrix multiplication with valid matrices."""
        result: list[list[float]] = digits_calculator.matrix_multiply(a, b)
        assert result == expected, f"Matrix multiplication failed for {a} × {b}"

    def test_matrix_multiply_rectangular_matrices(self) -> None:
        """Test multiplication with rectangular matrices (3x2 × 2x3)."""
        a: list[list[float]] = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
        b: list[list[float]] = [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
        result: list[list[float]] = digits_calculator.matrix_multiply(a, b)

        assert len(result) == 3, "Result should have 3 rows"
        assert len(result[0]) == 3, "Result should have 3 columns"
        assert result[0] == [27.0, 30.0, 33.0], "First row calculation incorrect"

    def test_matrix_multiply_with_negative_numbers(self) -> None:
        """Test matrix multiplication with negative values."""
        a: list[list[float]] = [[-1.0, 2.0], [3.0, -4.0]]
        b: list[list[float]] = [[5.0, -6.0], [-7.0, 8.0]]
        result: list[list[float]] = digits_calculator.matrix_multiply(a, b)

        assert result[0][0] == -19.0, "Calculation with negatives failed"
        assert result[1][1] == -50.0, "Calculation with negatives failed"

    def test_matrix_multiply_with_zeros(self) -> None:
        """Test multiplication with zero matrix."""
        a: list[list[float]] = [[0.0, 0.0], [0.0, 0.0]]
        b: list[list[float]] = [[5.0, 6.0], [7.0, 8.0]]
        result: list[list[float]] = digits_calculator.matrix_multiply(a, b)

        expected: list[list[float]] = [[0.0, 0.0], [0.0, 0.0]]
        assert result == expected, "Zero matrix multiplication failed"

    def test_matrix_multiply_floating_point(self) -> None:
        """Test matrix multiplication with floating point numbers."""
        a: list[list[float]] = [[0.1, 0.2], [0.3, 0.4]]
        b: list[list[float]] = [[0.5, 0.6], [0.7, 0.8]]
        result: list[list[float]] = digits_calculator.matrix_multiply(a, b)

        # [0][0] = 0.1*0.5 + 0.2*0.7 = 0.05 + 0.14 = 0.19
        assert abs(result[0][0] - 0.19) < 1e-10, "Floating point calculation failed"

    def test_matrix_multiply_incompatible_dimensions(self) -> None:
        """Test that incompatible dimensions raise ValueError."""
        a: list[list[float]] = [[1.0, 2.0], [3.0, 4.0]]  # 2x2 matrix
        b: list[list[float]] = [[5.0, 6.0, 7.0], [8.0, 9.0, 10.0], [11.0, 12.0, 13.0]]  # 3x3 matrix

        with pytest.raises(ValueError):
            digits_calculator.matrix_multiply(a, b)

    def test_matrix_multiply_empty_matrix(self) -> None:
        """Test that empty matrices raise ValueError."""
        a: list[list[float]] = []
        b: list[list[float]] = [[1.0, 2.0], [3.0, 4.0]]

        with pytest.raises(ValueError):
            digits_calculator.matrix_multiply(a, b)

    def test_matrix_multiply_inconsistent_row_length(self) -> None:
        """Test that inconsistent row lengths raise ValueError."""
        a: list[list[float]] = [[1.0, 2.0], [3.0]]
        b: list[list[float]] = [[5.0, 6.0], [7.0, 8.0]]

        with pytest.raises(ValueError):
            digits_calculator.matrix_multiply(a, b)

    def test_matrix_multiply_identity_property(self) -> None:
        """Test that multiplying by identity matrix returns original matrix."""
        identity: list[list[float]] = [[1.0, 0.0], [0.0, 1.0]]
        matrix: list[list[float]] = [[5.0, 6.0], [7.0, 8.0]]

        result: list[list[float]] = digits_calculator.matrix_multiply(identity, matrix)
        assert result == matrix, "Identity matrix multiplication failed"


# ============================================================================
# Test Suite: sum_as_string
# ============================================================================


class TestSumAsString:
    """Test suite for the sum_as_string function (deprecated, kept for compatibility)."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (10, 20, "30"),
            (0, 0, "0"),
            (5, 0, "5"),
            (0, 10, "10"),
            (1_000_000, 2_000_000, "3000000"),
        ],
    )
    def test_sum_as_string_results(self, a: int, b: int, expected: str) -> None:
        """Test sum_as_string with various input pairs."""
        result: str = digits_calculator.sum_as_string(a, b)
        assert result == expected, f"sum_as_string({a}, {b}) should return '{expected}'"

    def test_sum_as_string_returns_string(self) -> None:
        """Test that sum_as_string always returns a string."""
        result: str = digits_calculator.sum_as_string(10, 20)
        assert isinstance(result, str), "Result should be string type"

    def test_sum_as_string_consistency(self) -> None:
        """Test that multiple calls produce consistent results."""
        result1: str = digits_calculator.sum_as_string(100, 200)
        result2: str = digits_calculator.sum_as_string(100, 200)
        assert result1 == result2 == "300", "Consistent results for same inputs"

    def test_sum_as_string_commutative(self) -> None:
        """Test that addition is commutative."""
        result1: str = digits_calculator.sum_as_string(10, 20)
        result2: str = digits_calculator.sum_as_string(20, 10)
        assert result1 == result2 == "30", "Addition should be commutative"


# ============================================================================
# Test Suite: Module Integration
# ============================================================================


class TestModuleIntegration:
    """Test suite for module integration and attributes."""

    @pytest.mark.parametrize(
        "function_name",
        [
            "calculate_pi",
            "matrix_multiply",
            "divide",
            "safe_sqrt",
            "factorial",
        ],
    )
    def test_module_exports_function(self, function_name: str) -> None:
        """Test that module exports all expected functions."""
        assert hasattr(digits_calculator, function_name), (
            f"Module should have {function_name} function"
        )

    @pytest.mark.parametrize(
        "function_name",
        [
            "calculate_pi",
            "sum_as_string",
            "divide",
            "safe_sqrt",
            "factorial",
        ],
    )
    def test_exported_functions_are_callable(self, function_name: str) -> None:
        """Test that all exported functions are callable."""
        func = getattr(digits_calculator, function_name)
        assert callable(func), f"{function_name} should be callable"


# ============================================================================
# Test Suite: Exception Handling
# ============================================================================


class TestDivide:
    """Test suite for divide function with exception handling."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (10.0, 2.0, 5.0),
            (7.0, 2.0, 3.5),
            (-10.0, 2.0, -5.0),
            (10.0, -2.0, -5.0),
            (-10.0, -2.0, 5.0),
        ],
    )
    def test_divide_valid_operations(self, a: float, b: float, expected: float) -> None:
        """Test divide with various valid inputs."""
        result: float = digits_calculator.divide(a, b)
        assert abs(result - expected) < 1e-10, f"divide({a}, {b}) should equal {expected}"

    def test_divide_by_zero_raises_error(self) -> None:
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            digits_calculator.divide(10.0, 0.0)

    def test_divide_by_zero_message(self) -> None:
        """Test that division by zero error contains proper message."""
        with pytest.raises(ZeroDivisionError, match="Division by Zero"):
            digits_calculator.divide(10.0, 0.0)


class TestSafeSqrt:
    """Test suite for safe_sqrt function with exception handling."""

    @pytest.mark.parametrize(
        "x,expected",
        [
            (0.0, 0.0),
            (1.0, 1.0),
            (4.0, 2.0),
            (9.0, 3.0),
            (16.0, 4.0),
            (2.0, math.sqrt(2.0)),
        ],
    )
    def test_safe_sqrt_valid_inputs(self, x: float, expected: float) -> None:
        """Test safe_sqrt with valid positive inputs."""
        result: float = digits_calculator.safe_sqrt(x)
        assert abs(result - expected) < 1e-10, f"safe_sqrt({x}) should equal {expected}"

    def test_safe_sqrt_negative_raises_error(self) -> None:
        """Test that sqrt of negative number raises ValueError."""
        with pytest.raises(ValueError):
            digits_calculator.safe_sqrt(-9.0)

    def test_safe_sqrt_negative_message(self) -> None:
        """Test that negative sqrt error contains proper message."""
        with pytest.raises(ValueError, match="negative"):
            digits_calculator.safe_sqrt(-1.0)


class TestFactorial:
    """Test suite for factorial function with exception handling."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (5, 120),
            (10, 3628800),
            (20, 2432902008176640000),
        ],
    )
    def test_factorial_valid_inputs(self, n: int, expected: int) -> None:
        """Test factorial with various valid inputs."""
        result: int = digits_calculator.factorial(n)
        assert result == expected, f"factorial({n}) should equal {expected}"

    def test_factorial_negative_raises_error(self) -> None:
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError):
            digits_calculator.factorial(-5)

    def test_factorial_negative_message(self) -> None:
        """Test that negative factorial error contains proper message."""
        with pytest.raises(ValueError, match="negative"):
            digits_calculator.factorial(-1)
