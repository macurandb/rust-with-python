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

/// Formats the sum of two numbers as a string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok(math::sum(a, b).to_string())
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
