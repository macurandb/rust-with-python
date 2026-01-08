use pyo3::prelude::*;

/// Calculates an approximation of Pi using the Leibniz formula.
/// The more iterations, the more accurate the result.
#[pyfunction]
fn calculate_pi(iterations: u32) -> PyResult<f64> {
    let mut pi = 0.0;
    for k in 0..iterations {
        pi += ((-1.0f64).powf(k as f64) / (2 * k + 1) as f64) * 4.0;
    }
    Ok(pi)
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn pyo3_example(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(calculate_pi))?;
    m.add_wrapped(wrap_pyfunction!(sum_as_string))?;
    Ok(())
}


