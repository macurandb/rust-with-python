use pyo3::prelude::*;

mod math;

// ============================================================================
// PyO3 WRAPPER FUNCTIONS - These expose pure functions to Python
// ============================================================================

/// Calculates an approximation of Pi using the Leibniz formula.
#[pyfunction]
fn calculate_pi(iterations: u32) -> PyResult<f64> {
    Ok(math::calculate_pi(iterations))
}

/// Multiplies two matrices.
///
/// Matrices are represented as Vec<Vec<f64>>.
/// Returns a new matrix with dimensions (rows of A) x (cols of B).
#[pyfunction]
fn matrix_multiply(a: Vec<Vec<f64>>, b: Vec<Vec<f64>>) -> PyResult<Vec<Vec<f64>>> {
    match math::matrix_multiply(&a, &b) {
        Ok(result) => Ok(result),
        Err(msg) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(msg)),
    }
}

/// Divides two numbers and handles division by zero.
#[pyfunction]
fn divide(a: f64, b: f64) -> PyResult<f64> {
    match math::divide(a, b) {
        Ok(result) => Ok(result),
        Err(_) => Err(PyErr::new::<pyo3::exceptions::PyZeroDivisionError, _>(
            "Exception: Division by Zero",
        )),
    }
}

/// Calculates the square root and handles negative numbers.
#[pyfunction]
fn safe_sqrt(x: f64) -> PyResult<f64> {
    match math::safe_sqrt(x) {
        Ok(result) => Ok(result),
        Err(_) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Cannot calculate square root of negative number",
        )),
    }
}

/// Calculates factorial and handles invalid input.
#[pyfunction]
fn factorial(n: i32) -> PyResult<u64> {
    match math::factorial(n) {
        Ok(result) => Ok(result),
        Err(msg) => {
            if msg.contains("negative") {
                Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(msg))
            } else {
                Err(PyErr::new::<pyo3::exceptions::PyOverflowError, _>(msg))
            }
        }
    }
}

/// Adds two integers and returns the result as a string.
#[pyfunction]
fn sum_as_string(a: i64, b: i64) -> PyResult<String> {
    Ok(math::sum_as_string(a, b))
}

/// Python module for high-performance mathematical calculations.
/// Exposes Rust functions optimized for speed and precision.
#[pymodule]
fn digits_calculator(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(calculate_pi))?;
    m.add_wrapped(wrap_pyfunction!(matrix_multiply))?;
    m.add_wrapped(wrap_pyfunction!(divide))?;
    m.add_wrapped(wrap_pyfunction!(safe_sqrt))?;
    m.add_wrapped(wrap_pyfunction!(factorial))?;
    m.add_wrapped(wrap_pyfunction!(sum_as_string))?;
    Ok(())
}
