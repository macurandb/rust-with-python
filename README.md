# rust-with-python: PyO3 Integration Template

A professional template project demonstrating seamless integration between **Python** and **Rust** using **PyO3**. This project showcases how to write high-performance Rust code and expose it to Python with proper testing, documentation, and development practices.

## 🎯 Project Overview

This template demonstrates:

- ✅ **Python + Rust Integration**: Using PyO3 to expose Rust functions to Python
- ✅ **Performance**: Running computationally intensive tasks in Rust
- ✅ **Testing**: Comprehensive unit tests in Rust and integration tests in Python
- ✅ **Code Quality**: Using ruff for Python code formatting and linting
- ✅ **Development Workflow**: Makefile commands for building, testing, and running
- ✅ **Dependency Management**: Using `uv` for Python dependency management

## 📋 Project Structure

```
rust-with-python/
├── digits-calculator/          # Rust extension module
│   ├── Cargo.toml             # Rust dependencies
│   ├── src/
│   │   └── lib.rs             # Rust implementation with unit tests
│   └── pyproject.toml         # Maturin configuration
├── tests/
│   └── test_digits_calculator.py  # Python integration tests
├── main.py                     # Example usage
├── Makefile                    # Development commands
├── pyproject.toml             # Python project configuration with ruff
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Rust 1.70+
- `uv` (UV Python package manager)
- macOS, Linux, or Windows

### Installation

Clone the repository and set up the project:

```bash
git clone <repository-url>
cd rust-with-python
make install
```

This will:
1. Install Python dependencies using `uv`
2. Build the Rust extension using maturin
3. Install the extension in the Python environment

### Running the Project

```bash
make run
```

Output:
```
======================================================================
Welcome to rust-with-python!
Demonstrating Python and Rust Integration with PyO3
======================================================================

📊 Testing calculate_pi function (Rust Implementation):
----------------------------------------------------------------------
π approximation (1,000,000 iterations using Leibniz formula):
  Result:   3.1415916535897743
  Expected: 3.141592653589793
  Error:    0.0000010000

🔢 Testing sum_as_string function (Rust Implementation):
----------------------------------------------------------------------
Sum of 10 + 20 = 30

======================================================================
✅ All demonstrations completed successfully!
======================================================================
```

## 📦 Available Commands

### `make help`
Display all available commands.

### `make install`
Install Python dependencies and build the Rust extension.

### `make build`
Build the Rust extension (without running the main script).

### `make run`
Execute the main demonstration script.

### `make test`
Run both Rust unit tests and Python integration tests.

### `make lint`
Check code quality with ruff.

### `make format`
Format Python code with ruff.

### `make clean`
Remove all build artifacts and cache files.

### `make all`
Complete workflow: install, build, and run.

## 🔧 Using the Rust Module

### In Python

```python
import digits_calculator

# Calculate Pi using 1 million iterations
pi_approx = digits_calculator.calculate_pi(1_000_000)
print(f"π ≈ {pi_approx}")

# Sum two numbers and return as string
result = digits_calculator.sum_as_string(10, 20)
print(result)  # Output: "30"
```

### Rust Functions Reference

#### `calculate_pi(iterations: u32) -> float`

Calculates an approximation of π using the Leibniz formula:

π/4 = 1 - 1/3 + 1/5 - 1/7 + ...

- **Parameters**: `iterations` - Number of terms to compute
- **Returns**: Approximation of π as a float
- **Accuracy**: Increases with more iterations

**Example**:
```python
pi_1k = digits_calculator.calculate_pi(1_000)       # ~0.01 error
pi_1m = digits_calculator.calculate_pi(1_000_000)   # ~0.001 error
```

#### `sum_as_string(a: int, b: int) -> str`

Adds two numbers and returns the result as a string.

- **Parameters**: `a`, `b` - Numbers to sum (unsigned 64-bit integers)
- **Returns**: Sum formatted as a string
- **Use case**: Example of type conversion between Python and Rust

**Example**:
```python
result = digits_calculator.sum_as_string(100, 200)  # Returns "300"
```

## 🧪 Testing

### Run All Tests

```bash
make test
```

### Run Rust Tests Only

```bash
cd digits-calculator
cargo test --release
```

### Run Python Integration Tests Only

```bash
uv run pytest tests/ -v
```

### Test Coverage

- **Rust Unit Tests** (`digits-calculator/src/lib.rs`):
  - `test_calculate_pi_zero_iterations`: Boundary condition test
  - `test_calculate_pi_one_iteration`: Convergence test
  - `test_calculate_pi_accuracy_increases_with_iterations`: Accuracy improvement
  - `test_calculate_pi_large_iterations`: Performance with large numbers
  - `test_sum_as_string_basic`: Basic functionality
  - `test_sum_as_string_large_numbers`: Boundary values

- **Python Integration Tests** (`tests/test_digits_calculator.py`):
  - Type checking (float, string returns)
  - Mathematical accuracy
  - Consistency across multiple calls
  - Module exposure and callable verification

## 🎨 Code Quality

### Format Code

```bash
make format
```

Uses `ruff` to format Python code according to project standards.

### Lint Code

```bash
make lint
```

Checks Python code quality and style.

### Configuration

Ruff is configured in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 100
target-version = "py313"
extend-select = ["E", "F", "W", "I", "UP", "C4"]
```

## 📚 Creating Your Own Rust Functions

### Step 1: Implement in Rust

Edit `digits-calculator/src/lib.rs`:

```rust
/// Calculate factorial of a number
#[pyfunction]
fn factorial(n: u32) -> PyResult<u64> {
    if n > 20 {
        return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Input too large"
        ));
    }
    let result = (1..=n as u64).product();
    Ok(result)
}
```

### Step 2: Add Unit Tests

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_factorial_basic() {
        let result = factorial(5).unwrap();
        assert_eq!(result, 120);
    }
}
```

### Step 3: Expose to Python Module

Update the `#[pymodule]` function:

```rust
#[pymodule]
fn digits_calculator(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(calculate_pi))?;
    m.add_wrapped(wrap_pyfunction!(sum_as_string))?;
    m.add_wrapped(wrap_pyfunction!(factorial))?;  // Add this line
    Ok(())
}
```

### Step 4: Add Integration Tests

Create tests in `tests/test_digits_calculator.py`:

```python
def test_factorial_basic():
    result = digits_calculator.factorial(5)
    assert result == 120
```

### Step 5: Build and Test

```bash
make build
make test
```

## 🏗️ Development Workflow

### 1. Development Setup

```bash
make install
```

### 2. Make Changes

- Edit Rust code in `digits-calculator/src/lib.rs`
- Edit Python code in `.py` files

### 3. Build and Test

```bash
make build     # Build the extension
make test      # Run all tests
make lint      # Check code quality
```

### 4. Format Code

```bash
make format    # Auto-format Python code
```

### 5. Run Application

```bash
make run       # Run main.py
```

## 🔍 Troubleshooting

### "maturin failed" error

Ensure `CONDA_PREFIX` is not set when building:

```bash
unset CONDA_PREFIX
make build
```

### Module import error

Verify the build completed successfully:

```bash
make clean
make install
```

### Test failures

Check that all tests pass individually:

```bash
cd digits-calculator
cargo test --release --verbose

uv run pytest tests/ -v --tb=short
```

## 📖 Additional Resources

- [PyO3 Documentation](https://pyo3.rs/)
- [Rust Book](https://doc.rust-lang.org/book/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Maturin Documentation](https://www.maturin.rs/)

## 🛠️ Technologies Used

- **Python**: 3.13+
- **Rust**: Latest stable
- **PyO3**: 0.27.0 - Python bindings for Rust
- **Maturin**: Build tool for Python packages with Rust extensions
- **uv**: Fast Python package manager
- **Ruff**: Python linter and formatter
- **pytest**: Python testing framework

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ✨ Tips for Using as a Template

1. **Rename the project**: Update `pyproject.toml` and `Cargo.toml`
2. **Update the module name**: Change `digits_calculator` to your module name
3. **Replace functions**: Add your own Rust functions
4. **Add tests**: Write tests for your specific use cases
5. **Update README**: Document your specific functions and usage
6. **Version control**: Initialize with `git init` and commit your changes

## 🎓 Learning Path

If you're new to Python-Rust integration:

1. Start by understanding `main.py` - see how Python calls Rust
2. Read `digits-calculator/src/lib.rs` - understand the Rust implementation
3. Review `tests/test_digits_calculator.py` - see how testing works
4. Modify an existing function and rebuild
5. Add a new simple function
6. Run tests to verify everything works

## 📞 Support

For issues and questions:

1. Check the [PyO3 documentation](https://pyo3.rs/)
2. Review existing tests for examples
3. Check the Troubleshooting section above

---

**Happy Coding! 🚀**

Last updated: January 2026
