/// Pure Rust math functions - no PyO3 dependencies
/// These can be freely tested with `cargo test`

/// Calculates an approximation of Pi using the Leibniz formula.
///
/// The Leibniz formula states that π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
pub fn calculate_pi(iterations: u32) -> f64 {
    let mut pi = 0.0;
    for k in 0..iterations {
        pi += ((-1.0f64).powf(k as f64) / (2 * k + 1) as f64) * 4.0;
    }
    pi
}

/// Computes the sum of two numbers.
pub fn sum(a: usize, b: usize) -> usize {
    a + b
}

/// Divides two numbers with proper error handling.
pub fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

/// Calculates the square root of a number.
pub fn safe_sqrt(x: f64) -> Result<f64, String> {
    if x < 0.0 {
        Err("Cannot calculate square root of negative number".to_string())
    } else {
        Ok(x.sqrt())
    }
}

/// Calculates factorial.
pub fn factorial(n: i32) -> Result<u64, String> {
    if n < 0 {
        return Err("Factorial is not defined for negative numbers".to_string());
    }

    let n = n as u64;
    let mut result: u64 = 1;

    for i in 2..=n {
        result = result.saturating_mul(i);
        if result == 0 {
            return Err("Factorial result is too large".to_string());
        }
    }

    Ok(result)
}

#[cfg(test)]
mod tests {
    use super::*;

    // calculate_pi tests
    #[test]
    fn test_calculate_pi_zero_iterations() {
        let result = calculate_pi(0);
        assert_eq!(result, 0.0, "Zero iterations should return 0");
    }

    #[test]
    fn test_calculate_pi_one_iteration() {
        let result = calculate_pi(1);
        assert!((result - 4.0).abs() < 0.001, "One iteration should approximate to 4.0");
    }

    #[test]
    fn test_calculate_pi_accuracy_increases_with_iterations() {
        let result_100 = calculate_pi(100);
        let result_1000 = calculate_pi(1000);
        let result_10000 = calculate_pi(10000);
        let pi_actual = std::f64::consts::PI;

        let error_100 = (result_100 - pi_actual).abs();
        let error_1000 = (result_1000 - pi_actual).abs();
        let error_10000 = (result_10000 - pi_actual).abs();

        assert!(error_100 > error_1000, "Error should decrease with more iterations");
        assert!(error_1000 > error_10000, "Error should continue to decrease");
    }

    #[test]
    fn test_calculate_pi_large_iterations() {
        let result = calculate_pi(1_000_000);
        let pi_actual = std::f64::consts::PI;
        let error = (result - pi_actual).abs();
        assert!(error < 0.001, "1M iterations should be accurate within 0.001");
    }

    // sum tests
    #[test]
    fn test_sum_basic() {
        let result = sum(10, 20);
        assert_eq!(result, 30, "10 + 20 should equal 30");
    }

    #[test]
    fn test_sum_zero() {
        let result = sum(0, 0);
        assert_eq!(result, 0, "0 + 0 should equal 0");
    }

    #[test]
    fn test_sum_large_numbers() {
        let result = sum(1_000_000, 2_000_000);
        assert_eq!(result, 3_000_000, "Large number sum should work correctly");
    }

    // divide tests
    #[test]
    fn test_divide_basic() {
        let result = divide(10.0, 2.0);
        assert!(result.is_ok());
        assert!((result.unwrap() - 5.0).abs() < 0.0001, "10 / 2 should equal 5");
    }

    #[test]
    fn test_divide_by_zero() {
        let result = divide(10.0, 0.0);
        assert!(result.is_err(), "Division by zero should return an error");
    }

    #[test]
    fn test_divide_float_result() {
        let result = divide(7.0, 2.0);
        assert!(result.is_ok());
        assert!((result.unwrap() - 3.5).abs() < 0.0001, "7 / 2 should equal 3.5");
    }

    #[test]
    fn test_divide_negative_numbers() {
        let result = divide(-10.0, 2.0);
        assert!(result.is_ok());
        assert!((result.unwrap() - (-5.0)).abs() < 0.0001, "-10 / 2 should equal -5");
    }

    // safe_sqrt tests
    #[test]
    fn test_safe_sqrt_basic() {
        let result = safe_sqrt(16.0);
        assert!(result.is_ok());
        assert!((result.unwrap() - 4.0).abs() < 0.0001, "sqrt(16) should be 4");
    }

    #[test]
    fn test_safe_sqrt_negative() {
        let result = safe_sqrt(-9.0);
        assert!(result.is_err(), "sqrt of negative should return an error");
    }

    #[test]
    fn test_safe_sqrt_zero() {
        let result = safe_sqrt(0.0);
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), 0.0, "sqrt(0) should be 0");
    }

    // factorial tests
    #[test]
    fn test_factorial_basic() {
        let result = factorial(5);
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), 120, "5! should be 120");
    }

    #[test]
    fn test_factorial_zero() {
        let result = factorial(0);
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), 1, "0! should be 1");
    }

    #[test]
    fn test_factorial_one() {
        let result = factorial(1);
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), 1, "1! should be 1");
    }

    #[test]
    fn test_factorial_negative() {
        let result = factorial(-5);
        assert!(result.is_err(), "Factorial of negative should return an error");
    }

    #[test]
    fn test_factorial_large() {
        let result = factorial(20);
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), 2432902008176640000, "20! should be 2432902008176640000");
    }
}
