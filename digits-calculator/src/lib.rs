use pyo3::prelude::*;

/// Calculates an approximation of Pi using the Leibniz formula.
///
/// The Leibniz formula states that π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
/// This function computes the sum up to the specified number of iterations.
///
/// # Arguments
/// * `iterations` - Number of iterations for the approximation
///
/// # Returns
/// * `PyResult<f64>` - The approximated value of π
///
/// # Examples
/// ```python
/// import digits_calculator
/// pi_approx = digits_calculator.calculate_pi(1_000_000)
/// # Result: approximately 3.1415926...
/// ```
#[pyfunction]
fn calculate_pi(iterations: u32) -> PyResult<f64> {
    let mut pi = 0.0;
    for k in 0..iterations {
        pi += ((-1.0f64).powf(k as f64) / (2 * k + 1) as f64) * 4.0;
    }
    Ok(pi)
}

/// Formats the sum of two numbers as a string.
///
/// This is a simple example function demonstrating how to expose
/// Rust functions to Python that work with basic types.
///
/// # Arguments
/// * `a` - First number
/// * `b` - Second number
///
/// # Returns
/// * `PyResult<String>` - The sum formatted as a string
///
/// # Examples
/// ```python
/// import digits_calculator
/// result = digits_calculator.sum_as_string(10, 20)
/// # Result: "30"
/// ```
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// Divides two numbers and handles division by zero.
///
/// Demonstrates proper exception handling in Rust that translates to Python exceptions.
/// Raises ZeroDivisionError if the divisor is zero.
///
/// # Arguments
/// * `a` - Dividend (numerator)
/// * `b` - Divisor (denominator)
///
/// # Returns
/// * `PyResult<f64>` - The result of division a / b
///
/// # Raises
/// * `ZeroDivisionError` - If b is zero
///
/// # Examples
/// ```python
/// import digits_calculator
/// result = digits_calculator.divide(10.0, 2.0)
/// # Result: 5.0
///
/// # This raises ZeroDivisionError:
/// try:
///     result = digits_calculator.divide(10.0, 0.0)
/// except ZeroDivisionError as e:
///     print(f"Error: {e}")
/// ```
#[pyfunction]
fn divide(a: f64, b: f64) -> PyResult<f64> {
    if b == 0.0 {
        return Err(PyErr::new::<pyo3::exceptions::PyZeroDivisionError, _>(
            "Exception: Division by Zero",
        ));
    }
    Ok(a / b)
}

/// Calculates the square root and handles negative numbers.
///
/// Demonstrates custom error handling for invalid inputs.
/// Raises ValueError if the number is negative.
///
/// # Arguments
/// * `x` - The number to get the square root of
///
/// # Returns
/// * `PyResult<f64>` - The square root of x
///
/// # Raises
/// * `ValueError` - If x is negative
///
/// # Examples
/// ```python
/// import digits_calculator
/// result = digits_calculator.safe_sqrt(16.0)
/// # Result: 4.0
///
/// # This raises ValueError:
/// try:
///     result = digits_calculator.safe_sqrt(-9.0)
/// except ValueError as e:
///     print(f"Error: {e}")
/// ```
#[pyfunction]
fn safe_sqrt(x: f64) -> PyResult<f64> {
    if x < 0.0 {
        return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Cannot calculate square root of negative number",
        ));
    }
    Ok(x.sqrt())
}

/// Calculates factorial and handles invalid input.
///
/// Demonstrates error handling for out-of-range values.
/// Raises ValueError if n is negative.
///
/// # Arguments
/// * `n` - The number to calculate factorial for
///
/// # Returns
/// * `PyResult<u64>` - The factorial of n
///
/// # Raises
/// * `ValueError` - If n is negative
///
/// # Examples
/// ```python
/// import digits_calculator
/// result = digits_calculator.factorial(5)
/// # Result: 120
///
/// # This raises ValueError:
/// try:
///     result = digits_calculator.factorial(-5)
/// except ValueError as e:
///     print(f"Error: {e}")
/// ```
#[pyfunction]
fn factorial(n: i32) -> PyResult<u64> {
    if n < 0 {
        return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Factorial is not defined for negative numbers",
        ));
    }

    let n = n as u64;
    let mut result: u64 = 1;

    for i in 2..=n {
        result = result.saturating_mul(i);
        if result == 0 {
            return Err(PyErr::new::<pyo3::exceptions::PyOverflowError, _>(
                "Factorial result is too large",
            ));
        }
    }

    Ok(result)
}

/// Python module for high-performance mathematical calculations.
/// Exposes Rust functions optimized for speed and precision.
#[pymodule]
fn digits_calculator(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(calculate_pi))?;
    m.add_wrapped(wrap_pyfunction!(sum_as_string))?;
    m.add_wrapped(wrap_pyfunction!(divide))?;
    m.add_wrapped(wrap_pyfunction!(safe_sqrt))?;
    m.add_wrapped(wrap_pyfunction!(factorial))?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_pi_zero_iterations() {
        let result = calculate_pi(0).unwrap();
        assert_eq!(result, 0.0, "Zero iterations should return 0");
    }

    #[test]
    fn test_calculate_pi_one_iteration() {
        let result = calculate_pi(1).unwrap();
        assert!((result - 4.0).abs() < 0.001, "One iteration should approximate to 4.0");
    }

    #[test]
    fn test_calculate_pi_accuracy_increases_with_iterations() {
        let result_100 = calculate_pi(100).unwrap();
        let result_1000 = calculate_pi(1000).unwrap();
        let result_10000 = calculate_pi(10000).unwrap();
        let pi_actual = std::f64::consts::PI;

        let error_100 = (result_100 - pi_actual).abs();
        let error_1000 = (result_1000 - pi_actual).abs();
        let error_10000 = (result_10000 - pi_actual).abs();

        assert!(
            error_100 > error_1000,
            "Error should decrease with more iterations"
        );
        assert!(
            error_1000 > error_10000,
            "Error should continue to decrease with more iterations"
        );
    }

    #[test]
    fn test_calculate_pi_large_iterations() {
        let result = calculate_pi(1_000_000).unwrap();
        let pi_actual = std::f64::consts::PI;
        let error = (result - pi_actual).abs();

        assert!(error < 0.001, "1M iterations should be accurate within 0.001");
    }

    #[test]
    fn test_sum_as_string_basic() {
        let result = sum_as_string(10, 20).unwrap();
        assert_eq!(result, "30", "10 + 20 should equal 30");
    }

    #[test]
    fn test_sum_as_string_zero() {
        let result = sum_as_string(0, 0).unwrap();
        assert_eq!(result, "0", "0 + 0 should equal 0");
    }

    #[test]
    fn test_sum_as_string_large_numbers() {
        let result = sum_as_string(1_000_000, 2_000_000).unwrap();
        assert_eq!(result, "3000000", "Large number sum should work correctly");
    }

    #[test]
    fn test_divide_basic() {
        let result = divide(10.0, 2.0).unwrap();
        assert!((result - 5.0).abs() < 0.0001, "10 / 2 should equal 5");
    }

    #[test]
    fn test_divide_by_zero() {
        let result = divide(10.0, 0.0);
        assert!(result.is_err(), "Division by zero should return an error");
    }

    #[test]
    fn test_divide_float_result() {
        let result = divide(7.0, 2.0).unwrap();
        assert!((result - 3.5).abs() < 0.0001, "7 / 2 should equal 3.5");
    }

    #[test]
    fn test_divide_negative_numbers() {
        let result = divide(-10.0, 2.0).unwrap();
        assert!((result - (-5.0)).abs() < 0.0001, "-10 / 2 should equal -5");
    }

    #[test]
    fn test_safe_sqrt_basic() {
        let result = safe_sqrt(16.0).unwrap();
        assert!((result - 4.0).abs() < 0.0001, "sqrt(16) should be 4");
    }

    #[test]
    fn test_safe_sqrt_negative() {
        let result = safe_sqrt(-9.0);
        assert!(result.is_err(), "sqrt of negative should return an error");
    }

    #[test]
    fn test_safe_sqrt_zero() {
        let result = safe_sqrt(0.0).unwrap();
        assert_eq!(result, 0.0, "sqrt(0) should be 0");
    }

    #[test]
    fn test_factorial_basic() {
        let result = factorial(5).unwrap();
        assert_eq!(result, 120, "5! should be 120");
    }

    #[test]
    fn test_factorial_zero() {
        let result = factorial(0).unwrap();
        assert_eq!(result, 1, "0! should be 1");
    }

    #[test]
    fn test_factorial_one() {
        let result = factorial(1).unwrap();
        assert_eq!(result, 1, "1! should be 1");
    }

    #[test]
    fn test_factorial_negative() {
        let result = factorial(-5);
        assert!(result.is_err(), "Factorial of negative should return an error");
    }

    #[test]
    fn test_factorial_large() {
        let result = factorial(20).unwrap();
        assert_eq!(result, 2432902008176640000, "20! should be 2432902008176640000");
    }
}



