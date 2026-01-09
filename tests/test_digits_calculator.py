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


class TestExceptionHandling:
    """Test suite for exception handling in Rust functions."""

    def test_divide_basic(self):
        """Test basic division."""
        result = digits_calculator.divide(10.0, 2.0)
        assert result == 5.0, "10 / 2 should equal 5.0"

    def test_divide_by_zero_raises_exception(self):
        """Test that division by zero raises ZeroDivisionError."""
        with self.raise_exception_check(ZeroDivisionError):
            digits_calculator.divide(10.0, 0.0)

    def test_divide_float_result(self):
        """Test division with float result."""
        result = digits_calculator.divide(7.0, 2.0)
        assert abs(result - 3.5) < 0.0001, "7 / 2 should equal 3.5"

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        result = digits_calculator.divide(-10.0, 2.0)
        assert abs(result - (-5.0)) < 0.0001, "-10 / 2 should equal -5"

    def test_divide_negative_divisor(self):
        """Test division with negative divisor."""
        result = digits_calculator.divide(10.0, -2.0)
        assert abs(result - (-5.0)) < 0.0001, "10 / -2 should equal -5"

    def test_safe_sqrt_basic(self):
        """Test basic square root."""
        result = digits_calculator.safe_sqrt(16.0)
        assert abs(result - 4.0) < 0.0001, "sqrt(16) should be 4.0"

    def test_safe_sqrt_negative_raises_exception(self):
        """Test that sqrt of negative number raises ValueError."""
        with self.raise_exception_check(ValueError):
            digits_calculator.safe_sqrt(-9.0)

    def test_safe_sqrt_zero(self):
        """Test square root of zero."""
        result = digits_calculator.safe_sqrt(0.0)
        assert result == 0.0, "sqrt(0) should be 0.0"

    def test_safe_sqrt_decimal(self):
        """Test square root of decimal number."""
        result = digits_calculator.safe_sqrt(2.0)
        expected = math.sqrt(2.0)
        assert abs(result - expected) < 0.0001, f"sqrt(2) should be approximately {expected}"

    def test_factorial_basic(self):
        """Test basic factorial."""
        result = digits_calculator.factorial(5)
        assert result == 120, "5! should be 120"

    def test_factorial_zero(self):
        """Test factorial of zero."""
        result = digits_calculator.factorial(0)
        assert result == 1, "0! should be 1"

    def test_factorial_one(self):
        """Test factorial of one."""
        result = digits_calculator.factorial(1)
        assert result == 1, "1! should be 1"

    def test_factorial_negative_raises_exception(self):
        """Test that factorial of negative number raises ValueError."""
        with self.raise_exception_check(ValueError):
            digits_calculator.factorial(-5)

    def test_factorial_large(self):
        """Test factorial of larger number."""
        result = digits_calculator.factorial(10)
        assert result == 3628800, "10! should be 3628800"

    def test_factorial_very_large(self):
        """Test factorial of very large number."""
        result = digits_calculator.factorial(20)
        assert result == 2432902008176640000, "20! should be 2432902008176640000"

    @staticmethod
    def raise_exception_check(exception_type):
        """Context manager for checking exception raising."""
        class ExceptionChecker:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                if exc_type is None:
                    raise AssertionError(f"Expected {exception_type.__name__} but no exception was raised")
                if not issubclass(exc_type, exception_type):
                    return False  # Re-raise the exception
                return True  # Suppress the expected exception

        return ExceptionChecker()
