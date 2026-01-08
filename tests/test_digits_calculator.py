"""
Integration tests for digits_calculator module.

These tests verify that the Rust functions are properly exposed to Python
and work correctly with Python data types.
"""

import math

import digits_calculator


class TestCalculatePi:
    """Test suite for the calculate_pi function."""

    def test_calculate_pi_zero_iterations(self):
        """Test that zero iterations returns 0."""
        result = digits_calculator.calculate_pi(0)
        assert result == 0.0, "Zero iterations should return 0"

    def test_calculate_pi_small_iterations(self):
        """Test calculate_pi with small number of iterations."""
        result = digits_calculator.calculate_pi(10)
        assert isinstance(result, float), "Result should be a float"
        assert 2.0 < result < 4.0, "Pi approximation should be between 2 and 4"

    def test_calculate_pi_standard_iterations(self):
        """Test calculate_pi with standard iterations."""
        result = digits_calculator.calculate_pi(1000)
        pi_actual = math.pi
        error = abs(result - pi_actual)
        assert error < 0.01, f"1000 iterations should be accurate within 0.01, got error: {error}"

    def test_calculate_pi_large_iterations(self):
        """Test calculate_pi with large number of iterations."""
        result = digits_calculator.calculate_pi(1_000_000)
        pi_actual = math.pi
        error = abs(result - pi_actual)
        # With 1M iterations, we should be quite accurate
        assert error < 0.001, f"1M iterations should be accurate within 0.001, got error: {error}"

    def test_calculate_pi_consistency(self):
        """Test that multiple calls with same input produce same result."""
        result1 = digits_calculator.calculate_pi(10000)
        result2 = digits_calculator.calculate_pi(10000)
        assert result1 == result2, "Same input should produce same output"

    def test_calculate_pi_type(self):
        """Test that calculate_pi returns a float."""
        result = digits_calculator.calculate_pi(100)
        assert isinstance(result, float), "Result should be a float type"

    def test_calculate_pi_accuracy_improves(self):
        """Test that accuracy improves with more iterations."""
        result_100 = digits_calculator.calculate_pi(100)
        result_1000 = digits_calculator.calculate_pi(1000)
        result_10000 = digits_calculator.calculate_pi(10000)

        pi_actual = math.pi
        error_100 = abs(result_100 - pi_actual)
        error_1000 = abs(result_1000 - pi_actual)
        error_10000 = abs(result_10000 - pi_actual)

        assert error_100 > error_1000 > error_10000, "Error should decrease as iterations increase"


class TestSumAsString:
    """Test suite for the sum_as_string function."""

    def test_sum_as_string_basic(self):
        """Test basic addition conversion to string."""
        result = digits_calculator.sum_as_string(10, 20)
        assert result == "30", "10 + 20 should equal '30'"

    def test_sum_as_string_zero(self):
        """Test addition with zero."""
        result = digits_calculator.sum_as_string(0, 0)
        assert result == "0", "0 + 0 should equal '0'"

    def test_sum_as_string_one_zero(self):
        """Test addition with one zero."""
        result = digits_calculator.sum_as_string(5, 0)
        assert result == "5", "5 + 0 should equal '5'"

    def test_sum_as_string_large_numbers(self):
        """Test addition with large numbers."""
        result = digits_calculator.sum_as_string(1_000_000, 2_000_000)
        assert result == "3000000", "Large number sum should work correctly"

    def test_sum_as_string_return_type(self):
        """Test that sum_as_string returns a string."""
        result = digits_calculator.sum_as_string(10, 20)
        assert isinstance(result, str), "Result should be a string type"

    def test_sum_as_string_multiple_calls(self):
        """Test that multiple calls produce consistent results."""
        result1 = digits_calculator.sum_as_string(100, 200)
        result2 = digits_calculator.sum_as_string(100, 200)
        assert result1 == result2 == "300", "Consistent results for same inputs"

    def test_sum_as_string_commutative(self):
        """Test that addition is commutative."""
        result1 = digits_calculator.sum_as_string(10, 20)
        result2 = digits_calculator.sum_as_string(20, 10)
        assert result1 == result2 == "30", "Addition should be commutative"


class TestModuleIntegration:
    """Test suite for module integration and attributes."""

    def test_module_has_calculate_pi(self):
        """Test that module exposes calculate_pi function."""
        assert hasattr(digits_calculator, "calculate_pi"), (
            "Module should have calculate_pi function"
        )

    def test_module_has_sum_as_string(self):
        """Test that module exposes sum_as_string function."""
        assert hasattr(digits_calculator, "sum_as_string"), (
            "Module should have sum_as_string function"
        )

    def test_functions_are_callable(self):
        """Test that exposed functions are callable."""
        assert callable(digits_calculator.calculate_pi), "calculate_pi should be callable"
        assert callable(digits_calculator.sum_as_string), "sum_as_string should be callable"
