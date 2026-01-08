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

/// Python module for high-performance mathematical calculations.
/// Exposes Rust functions optimized for speed and precision.
#[pymodule]
fn digits_calculator(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(calculate_pi))?;
    m.add_wrapped(wrap_pyfunction!(sum_as_string))?;
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
}



