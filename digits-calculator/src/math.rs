//! Pure Rust math functions - no PyO3 dependencies
//! These can be freely tested with `cargo test`

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

/// Multiplies two matrices.
///
/// Performs standard matrix multiplication where the result matrix dimensions
/// are (rows of A) x (cols of B). The number of columns in A must equal
/// the number of rows in B.
///
/// # Arguments
/// * `a` - First matrix as Vec<Vec<f64>>
/// * `b` - Second matrix as Vec<Vec<f64>>
///
/// # Returns
/// * `Ok(Vec<Vec<f64>>)` - The resulting matrix
/// * `Err(String)` - Error message if dimensions are incompatible
///
/// # Examples
/// ```ignore
/// let a = vec![vec![1.0, 2.0], vec![3.0, 4.0]];
/// let b = vec![vec![5.0, 6.0], vec![7.0, 8.0]];
/// let result = matrix_multiply(&a, &b).unwrap();
/// // result = [[19.0, 22.0], [43.0, 50.0]]
/// ```
pub fn matrix_multiply(
    a: &[Vec<f64>],
    b: &[Vec<f64>],
) -> Result<Vec<Vec<f64>>, String> {
    // Validate input matrices are not empty
    if a.is_empty() || b.is_empty() {
        return Err("Matrices cannot be empty".to_string());
    }

    let rows_a = a.len();
    let cols_a = a[0].len();
    let rows_b = b.len();
    let cols_b = b[0].len();

    // Validate all rows have consistent length
    for row in a.iter() {
        if row.len() != cols_a {
            return Err(
                "All rows in matrix A must have the same number of columns".to_string(),
            );
        }
    }

    for row in b.iter() {
        if row.len() != cols_b {
            return Err(
                "All rows in matrix B must have the same number of columns".to_string(),
            );
        }
    }

    // Check if matrices can be multiplied
    if cols_a != rows_b {
        return Err(format!(
            "Cannot multiply matrices: A is {}x{}, B is {}x{}. Columns of A ({}) must equal rows of B ({})",
            rows_a, cols_a, rows_b, cols_b, cols_a, rows_b
        ));
    }

    // Perform matrix multiplication
    let mut result = vec![vec![0.0; cols_b]; rows_a];

    for i in 0..rows_a {
        for j in 0..cols_b {
            let mut sum = 0.0;
            for k in 0..cols_a {
                sum += a[i][k] * b[k][j];
            }
            result[i][j] = sum;
        }
    }

    Ok(result)
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

/// Adds two integers and returns the result as a string.
/// This is a simple function for testing PyO3 integration.
pub fn sum_as_string(a: i64, b: i64) -> String {
    (a + b).to_string()
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

    // matrix_multiply tests
    #[test]
    fn test_matrix_multiply_basic_2x2() {
        let a = vec![vec![1.0, 2.0], vec![3.0, 4.0]];
        let b = vec![vec![5.0, 6.0], vec![7.0, 8.0]];
        let result = matrix_multiply(&a, &b).unwrap();

        assert_eq!(result[0][0], 19.0, "a[0][0]*b[0][0] + a[0][1]*b[1][0]");
        assert_eq!(result[0][1], 22.0, "a[0][0]*b[0][1] + a[0][1]*b[1][1]");
        assert_eq!(result[1][0], 43.0, "a[1][0]*b[0][0] + a[1][1]*b[1][0]");
        assert_eq!(result[1][1], 50.0, "a[1][0]*b[0][1] + a[1][1]*b[1][1]");
    }

    #[test]
    fn test_matrix_multiply_identity_matrix() {
        let a = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
        let b = vec![vec![5.0, 6.0], vec![7.0, 8.0]];
        let result = matrix_multiply(&a, &b).unwrap();

        // Multiplying by identity matrix should return the original matrix
        assert_eq!(result, b, "Multiplying by identity should return original matrix");
    }

    #[test]
    fn test_matrix_multiply_rectangular_3x2_times_2x3() {
        let a = vec![vec![1.0, 2.0], vec![3.0, 4.0], vec![5.0, 6.0]];
        let b = vec![vec![7.0, 8.0, 9.0], vec![10.0, 11.0, 12.0]];
        let result = matrix_multiply(&a, &b).unwrap();

        // Result should be 3x3
        assert_eq!(result.len(), 3);
        assert_eq!(result[0].len(), 3);

        // Manual calculation:
        // [0][0] = 1*7 + 2*10 = 27
        // [0][1] = 1*8 + 2*11 = 30
        // [0][2] = 1*9 + 2*12 = 33
        assert_eq!(result[0], vec![27.0, 30.0, 33.0]);
    }

    #[test]
    fn test_matrix_multiply_with_negative_numbers() {
        let a = vec![vec![-1.0, 2.0], vec![3.0, -4.0]];
        let b = vec![vec![5.0, -6.0], vec![-7.0, 8.0]];
        let result = matrix_multiply(&a, &b).unwrap();

        // [0][0] = -1*5 + 2*(-7) = -5 - 14 = -19
        assert_eq!(result[0][0], -19.0);
        // [1][1] = 3*(-6) + (-4)*8 = -18 - 32 = -50
        assert_eq!(result[1][1], -50.0);
    }

    #[test]
    fn test_matrix_multiply_single_row_times_single_col() {
        let a = vec![vec![1.0, 2.0, 3.0]];
        let b = vec![vec![4.0], vec![5.0], vec![6.0]];
        let result = matrix_multiply(&a, &b).unwrap();

        // Result is 1x1: [1*4 + 2*5 + 3*6] = [32]
        assert_eq!(result.len(), 1);
        assert_eq!(result[0].len(), 1);
        assert_eq!(result[0][0], 32.0);
    }

    #[test]
    fn test_matrix_multiply_dimension_mismatch() {
        let a = vec![vec![1.0, 2.0], vec![3.0, 4.0]]; // 2x2 matrix
        let b = vec![vec![5.0, 6.0, 7.0], vec![8.0, 9.0, 10.0], vec![11.0, 12.0, 13.0]]; // 3x3 matrix
        let result = matrix_multiply(&a, &b);

        // a is 2x2 (2 columns), b is 3x3 (3 rows) -> incompatible: 2 != 3
        assert!(result.is_err());
        assert!(result.unwrap_err().contains("Cannot multiply matrices"));
    }

    #[test]
    fn test_matrix_multiply_empty_matrix() {
        let a: Vec<Vec<f64>> = vec![];
        let b = vec![vec![1.0, 2.0], vec![3.0, 4.0]];
        let result = matrix_multiply(&a, &b);

        assert!(result.is_err());
        assert!(result.unwrap_err().contains("empty"));
    }

    #[test]
    fn test_matrix_multiply_inconsistent_row_length() {
        let a = vec![vec![1.0, 2.0], vec![3.0]];
        let b = vec![vec![5.0, 6.0], vec![7.0, 8.0]];
        let result = matrix_multiply(&a, &b);

        assert!(result.is_err());
        assert!(result
            .unwrap_err()
            .contains("All rows in matrix A must have the same"));
    }

    #[test]
    fn test_matrix_multiply_with_zeros() {
        let a = vec![vec![0.0, 0.0], vec![0.0, 0.0]];
        let b = vec![vec![5.0, 6.0], vec![7.0, 8.0]];
        let result = matrix_multiply(&a, &b).unwrap();

        // Zero matrix times any matrix should be zero matrix
        assert_eq!(result, vec![vec![0.0, 0.0], vec![0.0, 0.0]]);
    }

    #[test]
    fn test_matrix_multiply_floating_point_precision() {
        let a = vec![vec![0.1, 0.2], vec![0.3, 0.4]];
        let b = vec![vec![0.5, 0.6], vec![0.7, 0.8]];
        let result = matrix_multiply(&a, &b).unwrap();

        // [0][0] = 0.1*0.5 + 0.2*0.7 = 0.05 + 0.14 = 0.19
        assert!((result[0][0] - 0.19).abs() < 1e-10);
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

    // sum_as_string tests
    #[test]
    fn test_sum_as_string_basic() {
        let result = sum_as_string(10, 20);
        assert_eq!(result, "30", "10 + 20 should be '30'");
    }

    #[test]
    fn test_sum_as_string_zero() {
        let result = sum_as_string(0, 0);
        assert_eq!(result, "0", "0 + 0 should be '0'");
    }

    #[test]
    fn test_sum_as_string_negative() {
        let result = sum_as_string(-5, 10);
        assert_eq!(result, "5", "-5 + 10 should be '5'");
    }

    #[test]
    fn test_sum_as_string_large_numbers() {
        let result = sum_as_string(1_000_000, 2_000_000);
        assert_eq!(result, "3000000", "1000000 + 2000000 should be '3000000'");
    }
}
