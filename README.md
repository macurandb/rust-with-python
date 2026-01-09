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
Display all available commands with organized categories.

### Setup & Build

#### `make install`
Install Python dependencies and build the Rust extension.

#### `make build`
Build the Rust extension (without running the main script).

#### `make check`
Quick code check without full build:
- `cargo check` for Rust
- `ruff check` for Python

### Run & Test

#### `make run`
Execute the main demonstration script.

#### `make test`
Run all tests (Rust unit tests + Python integration tests).

#### `make test-rust`
Run Rust unit tests only with `cargo test --lib`.

#### `make test-python`
Run Python integration tests only with `pytest`.

### Code Quality

#### `make lint`
Run all linters:
- `cargo clippy` for Rust code analysis
- `ruff check` for Python code quality

#### `make lint-rust`
Run `cargo clippy` with warnings as errors on Rust code.

#### `make lint-python`
Run `ruff check` for Python linting.

#### `make fmt`
Format all code (Rust + Python).

#### `make fmt-rust`
Format Rust code with `cargo fmt`.

#### `make fmt-python`
Format Python code with `ruff format`.

### Maintenance

#### `make clean`
Remove all build artifacts and cache files.

#### `make all`
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

### Exception Handling Functions

The module includes functions demonstrating proper error handling from Rust to Python:

#### `divide(a: float, b: float) -> float`

Divides two numbers with proper error handling.

- **Parameters**: `a` (dividend), `b` (divisor)
- **Returns**: Result of a / b as float
- **Raises**: `ZeroDivisionError` if b is zero

**Example**:
```python
import digits_calculator

# Normal operation
result = digits_calculator.divide(10.0, 2.0)  # Returns 5.0

# Error handling
try:
    result = digits_calculator.divide(10.0, 0.0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

#### `safe_sqrt(x: float) -> float`

Calculates square root with validation.

- **Parameters**: `x` - Number to get square root of
- **Returns**: Square root of x
- **Raises**: `ValueError` if x is negative

**Example**:
```python
result = digits_calculator.safe_sqrt(16.0)  # Returns 4.0

try:
    result = digits_calculator.safe_sqrt(-9.0)
except ValueError as e:
    print(f"Error: {e}")
```

#### `factorial(n: int) -> int`

Calculates factorial with boundary checking.

- **Parameters**: `n` - Number to calculate factorial for
- **Returns**: Factorial of n
- **Raises**: `ValueError` if n is negative

**Example**:
```python
result = digits_calculator.factorial(5)  # Returns 120

try:
    result = digits_calculator.factorial(-5)
except ValueError as e:
    print(f"Error: {e}")
```

### Run All Tests

```bash
make test
```

This runs:
- Rust unit tests
- Python integration tests with **pytest**

### Run Tests by Type

```bash
make test-rust       # Rust unit tests only
make test-python     # Python integration tests only (pytest)
```

### Testing Framework: pytest

The project uses **pytest**, the industry-standard Python testing framework, with professional best practices:

- **Parametrized Tests**: `@pytest.mark.parametrize` for efficient test variations
- **Fixtures**: Reusable test components with `@pytest.fixture`
- **Exception Testing**: `pytest.raises()` for clean exception validation
- **Test Organization**: Logical test classes with clear naming conventions
- **Detailed Reports**: Rich output with test descriptions and error messages

Example pytest command:
```bash
# Run all tests with verbose output
uv run pytest tests/ -v

# Run specific test class
uv run pytest tests/test_digits_calculator.py::TestCalculatePi -v

# Run specific test
uv run pytest tests/test_digits_calculator.py::TestCalculatePi::test_calculate_pi_zero_iterations -v

# Run with detailed output and short traceback
uv run pytest tests/ -v --tb=short
```

### Test Coverage

The project includes comprehensive tests for all functions:

#### Rust Unit Tests (7 tests in lib.rs)

**calculate_pi tests**:
- `test_calculate_pi_zero_iterations`: Zero input boundary
- `test_calculate_pi_one_iteration`: Single iteration
- `test_calculate_pi_accuracy_increases_with_iterations`: Accuracy improvement
- `test_calculate_pi_large_iterations`: Performance with 1M iterations

**sum_as_string tests**:
- `test_sum_as_string_basic`: Basic functionality
- `test_sum_as_string_zero`: Zero handling
- `test_sum_as_string_large_numbers`: Large number handling

#### Python Integration Tests with pytest (52 tests in tests/test_digits_calculator.py)

**TestCalculatePi** (10 parametrized + individual tests):
- Range validation with multiple iteration counts
- Accuracy testing with various tolerances
- Type checking
- Consistency verification
- Accuracy improvement with iterations

**TestSumAsString** (8 parametrized + individual tests):
- Parametrized testing with 5 input combinations
- Type verification
- Consistency checks
- Commutativity property

**TestModuleIntegration** (10 parametrized tests):
- Function export verification
- Module attribute checking
- Callable verification for all 5 functions

**TestDivide** (7 parametrized + error tests):
- Valid operations with 5 parameter combinations
- ZeroDivisionError testing
- Error message validation

**TestSafeSqrt** (8 parametrized + error tests):
- Valid square roots with 6 test cases
- ValueError on negative inputs
- Error message validation

**TestFactorial** (9 parametrized + error tests):
- Factorial calculations for 0-20
- ValueError on negative inputs
- Error message validation

### Test Results

All tests pass with pytest:
```
✅ Rust unit tests:          7/7 passing
✅ Python integration tests: 52/52 passing (parametrized)
✅ Total coverage:           59+ test cases
```

### Run Specific Tests

```bash
# Run a specific test class
uv run pytest tests/test_digits_calculator.py::TestCalculatePi -v

# Run a specific test
uv run pytest tests/test_digits_calculator.py::TestCalculatePi::test_calculate_pi_ranges -v

# Run with verbose output
uv run pytest tests/ -v --tb=short

# Run with coverage report
uv run pytest tests/ --cov=digits_calculator
```

## 🎨 Code Quality

### Linting & Code Analysis

The project uses industry-standard tools for code quality:

#### Rust Code Quality

- **cargo clippy**: Rust's official linter that catches common mistakes
- **cargo fmt**: Automatic Rust code formatter
- **cargo check**: Quick syntax and type checking without building

```bash
make lint-rust    # Run cargo clippy with deny-warnings
make fmt-rust     # Format Rust code
make check-rust   # Quick check
```

#### Python Code Quality

- **ruff check**: Fast Python linter (includes E, F, W, I, UP, C4 rules)
- **ruff format**: Python code formatter following project standards
- **pytest**: Comprehensive testing framework

```bash
make lint-python   # Run ruff check
make fmt-python    # Format Python code
make test-python   # Run integration tests
```

### Running All Code Quality Checks

```bash
make lint       # Run all linters (Rust + Python)
make fmt        # Format all code (Rust + Python)
make check      # Quick checks without full build
```

### Configuration

#### Ruff Configuration (Python)

Defined in `pyproject.toml`:

```toml
[tool.ruff.lint]
line-length = 100
target-version = "py313"
extend-select = ["E", "F", "W", "I", "UP", "C4"]
```

**Rules**:
- `E`: PEP 8 errors
- `F`: Pyflakes (undefined names, unused imports)
- `W`: PEP 8 warnings
- `I`: isort (import sorting)
- `UP`: PyUpgrade (modernize code)
- `C4`: flake8-comprehensions

#### Rust Configuration (Cargo)

Defined in `digits-calculator/Cargo.toml` with clippy lint levels set to deny.

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

### 3. Code Quality Checks

Before committing, ensure code passes all quality checks:

```bash
make lint       # Run linters (cargo clippy + ruff check)
make fmt        # Format code (cargo fmt + ruff format)
make check      # Quick check without full build
```

### 4. Build and Test

```bash
make build      # Build the extension
make test       # Run all tests (Rust + Python)
```

Or run tests separately:

```bash
make test-rust     # Rust unit tests only
make test-python   # Python integration tests only
```

### 5. Run Application

```bash
make run        # Run main.py
```

### Complete Development Cycle

A typical development session:

```bash
# Setup
make install

# Make your changes
# ... edit files ...

# Quality checks
make fmt        # Format code
make lint       # Check code quality

# Build and test
make build      # Compile Rust extension
make test       # Run all tests

# Deploy/run
make run        # Execute application
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

**Recent additions**: Exception handling functions, comprehensive linting and formatting tools, enhanced testing infrastructure
