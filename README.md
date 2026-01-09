# rust-with-python: PyO3 Integration Template

🦀 **High-performance Rust functions** + 🐍 **Python productivity** = Perfect integration

## 🎯 Project Overview

This template demonstrates how to integrate Rust with Python using PyO3, providing a solid foundation for projects that need the performance of Rust with the convenience of Python. It includes **6 mathematical functions** showcasing different aspects of Rust-Python integration: from simple calculations to complex matrix operations with comprehensive error handling.

**Perfect for**: Performance-critical applications, numerical computing, learning Rust-Python integration, and building high-performance Python extensions.

**What's included**: 93 tests (30 Rust + 63 Python), complete development workflow, professional code organization, and comprehensive documentation.

## 📋 Project Structure

```
rust-with-python/
├── digits-calculator/          # Rust crate (PyO3 extension)
│   ├── src/
│   │   ├── lib.rs             # PyO3 wrapper functions
│   │   └── math.rs            # Pure Rust mathematical functions
│   ├── Cargo.toml             # Rust dependencies & metadata
│   └── pyproject.toml         # Python build configuration
├── tests/
│   └── test_digits_calculator.py  # 63 comprehensive Python tests
├── main.py                    # Example usage demonstration
├── Makefile                   # 15 development commands
├── pyproject.toml             # Project configuration & dependencies
├── README.md                  # This documentation
├── CONTRIBUTING.md            # Development guidelines
├── TEMPLATE_COMPLETION.md     # Template transformation report
└── uv.lock                    # Dependency lock file
```

### Architecture: Pure Rust + PyO3 Wrappers

**Two-module design for maximum testability:**

- **`src/math.rs`**: Pure Rust mathematical functions (30 unit tests, no PyO3 dependencies)
- **`src/lib.rs`**: PyO3 wrapper layer that exposes functions to Python (handles type conversion and error mapping)

This separation allows:
- Fast Rust unit testing without Python FFI overhead
- Clean separation of business logic and binding code
- Easy maintenance and debugging
- Professional code organization

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (tested with 3.13)
- **Rust 1.70+** (latest stable recommended)
- **uv** for Python dependency management ([install guide](https://docs.astral.sh/uv/getting-started/installation/))

### Installation

```bash
# Clone the repository
git clone https://github.com/macurandb/rust-with-python.git
cd rust-with-python

# Install and build everything
make install

# Verify installation
make test
```

This will:
1. Create a Python virtual environment with `uv`
2. Install all Python dependencies
3. Build the Rust extension module
4. Run all 93 tests to verify everything works

### Running the Project

```bash
# Run the demonstration
make run
```

Example output:
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
Shows all available commands with descriptions.

### Setup & Build

#### `make install`
Complete setup: creates virtual environment, installs dependencies, builds Rust module.

#### `make build` 
Builds the Rust extension module only.

#### `make check`
Quick verification without full rebuild.

### Run & Test

#### `make run`
Runs the main demonstration script.

#### `make test`
Runs all tests (30 Rust unit tests + 63 Python integration tests = 93 total tests).

#### `make test-rust`
Runs only the Rust unit tests (fast, no Python FFI).

#### `make test-python`
Runs only the Python integration tests with pytest.

### Code Quality

#### `make lint`
Checks code quality for both Rust (clippy) and Python (ruff).

Example output:
```bash
🔍 Checking Rust code with clippy...
✅ Rust code quality checks passed!
🔍 Checking Python code with ruff...
✅ Python code quality checks passed!
```

#### `make lint-rust`
Rust-only linting with clippy.

#### `make lint-python`
Python-only linting with ruff.

#### `make fmt`
Formats all code (Rust with cargo fmt, Python with ruff format).

#### `make fmt-rust`
Rust-only formatting.

#### `make fmt-python`
Python-only formatting.

### Maintenance

#### `make clean`
Removes all build artifacts and virtual environments.

#### `make all`
Complete workflow: install, build, test, lint, and run.

## 🔧 Using the Rust Module

### In Python

```python
import digits_calculator

# High-precision π calculation
pi = digits_calculator.calculate_pi(1_000_000)
print(f"π ≈ {pi}")

# Matrix multiplication
a = [[1.0, 2.0], [3.0, 4.0]]
b = [[5.0, 6.0], [7.0, 8.0]]
result = digits_calculator.matrix_multiply(a, b)
print(f"Result: {result}")  # [[19.0, 22.0], [43.0, 50.0]]

# Safe mathematical operations
sqrt_result = digits_calculator.safe_sqrt(25.0)  # 5.0
division_result = digits_calculator.divide(10.0, 3.0)  # 3.333...
factorial_result = digits_calculator.factorial(5)  # 120
```

### Rust Functions Reference

All functions are implemented in pure Rust for maximum performance:

#### `calculate_pi(iterations: u32) -> float`

Calculates π using the Leibniz formula: π/4 = 1 - 1/3 + 1/5 - 1/7 + ...

```python
# More iterations = higher precision
pi_low = digits_calculator.calculate_pi(100)      # ~3.131
pi_medium = digits_calculator.calculate_pi(10000)  # ~3.1414
pi_high = digits_calculator.calculate_pi(1000000)  # ~3.141592

import math
error = abs(pi_high - math.pi)  # Very small error
```

**Performance**: 1,000,000 iterations in ~0.004s

#### `matrix_multiply(a: List[List[float]], b: List[List[float]]) -> List[List[float]]`

High-performance matrix multiplication with comprehensive validation.

```python
# 2D transformation example
rotation = [[0.866, -0.5], [0.5, 0.866]]  # 30° rotation
point = [[1.0], [0.0]]
rotated = digits_calculator.matrix_multiply(rotation, point)
# Result: [[0.866], [0.5]]

# Supports rectangular matrices
a = [[1, 2], [3, 4], [5, 6]]  # 3x2
b = [[7, 8, 9], [10, 11, 12]]  # 2x3
result = digits_calculator.matrix_multiply(a, b)  # 3x3 result
```

**Features**: Dimension validation, empty matrix detection, floating-point precision handling.

#### `sum_as_string(a: int, b: int) -> str`

Simple integer addition returning string result (useful for very large numbers).

```python
result = digits_calculator.sum_as_string(999999999, 1)
print(result)  # "1000000000" (as string)
```

### Exception Handling Functions

All functions include proper error handling with specific Python exception types:

#### `divide(a: float, b: float) -> float`

Safe division with zero-division protection.

```python
try:
    result = digits_calculator.divide(10.0, 2.0)  # 5.0
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Division error: {e}")

# This will raise ZeroDivisionError
try:
    digits_calculator.divide(10.0, 0.0)
except ZeroDivisionError as e:
    print("Cannot divide by zero!")  # Exception caught
```

#### `safe_sqrt(x: float) -> float`

Square root calculation with negative number protection.

```python
try:
    result = digits_calculator.safe_sqrt(16.0)  # 4.0
    print(f"√16 = {result}")
except ValueError as e:
    print(f"Square root error: {e}")

# This will raise ValueError
try:
    digits_calculator.safe_sqrt(-9.0)
except ValueError as e:
    print("Cannot calculate square root of negative number!")
```

#### `factorial(n: int) -> int`

Factorial calculation with input validation and overflow detection.

```python
try:
    result = digits_calculator.factorial(5)  # 120
    print(f"5! = {result}")
except ValueError as e:
    print(f"Input error: {e}")
except OverflowError as e:
    print(f"Result too large: {e}")

# This will raise ValueError
try:
    digits_calculator.factorial(-5)
except ValueError as e:
    print("Factorial not defined for negative numbers!")
```

## 🧪 Testing

### Run All Tests

```bash
make test
```

Expected output:
```
🦀 Running Rust unit tests (pure math module)...
running 30 tests
test result: ok. 30 passed; 0 failed

🐍 Running Python integration tests...
collected 63 items
================================= 63 passed in 0.03s =================================
✅ All tests passed!
```

### Run Tests by Type

```bash
make test-rust    # Fast Rust unit tests only
make test-python  # Python integration tests only
```

### Testing Framework: pytest

The Python tests use pytest with professional patterns:

- **Parametrized tests** for comprehensive coverage
- **Fixtures** for test data management
- **Exception testing** with `pytest.raises()`
- **Type verification** and **consistency checks**
- **Performance benchmarks** included

Example test:
```python
@pytest.mark.parametrize("iterations,max_error", [
    (1_000, 0.01),
    (10_000, 0.001),
    (1_000_000, 0.001),
])
def test_calculate_pi_accuracy(self, iterations, max_error):
    result = digits_calculator.calculate_pi(iterations)
    error = abs(result - math.pi)
    assert error < max_error
```

### Test Coverage

**Total: 93 tests (100% passing)**

#### Rust Unit Tests (30 tests in src/math.rs)

Pure Rust function testing without PyO3 dependencies:

- **calculate_pi tests** (4 tests): Accuracy, edge cases, convergence
- **matrix_multiply tests** (10 tests): Basic operations, dimensions, error cases, floating-point precision
- **divide tests** (4 tests): Valid operations, error handling, negative numbers
- **safe_sqrt tests** (3 tests): Valid inputs, negative handling, edge cases  
- **factorial tests** (5 tests): Valid calculations, error cases, large numbers
- **sum_as_string tests** (4 tests): Basic operations, edge cases, large numbers

```bash
# Run with details
cd digits-calculator && cargo test -- --nocapture

test math::tests::test_calculate_pi_zero_iterations ... ok
test math::tests::test_matrix_multiply_basic_2x2 ... ok
test math::tests::test_divide_basic ... ok
test math::tests::test_safe_sqrt_basic ... ok
test math::tests::test_factorial_basic ... ok
test math::tests::test_sum_as_string_basic ... ok
# ... and 24 more tests
```

#### Python Integration Tests (63 pytest tests in tests/test_digits_calculator.py)

Comprehensive PyO3 integration testing:

- **TestCalculatePi**: 10 parametrized tests (ranges, accuracy, consistency)
- **TestMatrixMultiply**: 11 tests (valid operations, error cases, edge cases)
- **TestSumAsString**: 8 parametrized tests (operations, types, consistency)
- **TestModuleIntegration**: 10 parametrized tests (exports, callability)
- **TestDivide**: 7 tests (operations, exception handling)
- **TestSafeSqrt**: 8 tests (valid inputs, exception handling)
- **TestFactorial**: 9 tests (calculations, exception handling)

```python
# Example parametrized test
@pytest.mark.parametrize("a,b,expected", [
    (10.0, 2.0, 5.0),
    (7.0, 2.0, 3.5),
    (-10.0, 2.0, -5.0),
])
def test_divide_valid_operations(self, a, b, expected):
    result = digits_calculator.divide(a, b)
    assert abs(result - expected) < 1e-10
```

### Test Results

```
================================= test session starts =================================
collected 63 items

tests/test_digits_calculator.py::TestCalculatePi::test_calculate_pi_ranges[0-expected_range0] PASSED
tests/test_digits_calculator.py::TestMatrixMultiply::test_matrix_multiply_valid[a0-b0-expected0] PASSED
tests/test_digits_calculator.py::TestDivide::test_divide_valid_operations[10.0-2.0-5.0] PASSED
tests/test_digits_calculator.py::TestSafeSqrt::test_safe_sqrt_valid_inputs[16.0-4.0] PASSED
tests/test_digits_calculator.py::TestFactorial::test_factorial_valid_inputs[5-120] PASSED
# ... 58 more tests all PASSED

================================= 63 passed in 0.03s =================================
```

### Run Specific Tests

```bash
# Test specific function
cd digits-calculator && cargo test calculate_pi
uv run pytest tests/ -k "calculate_pi" -v

# Test specific class
uv run pytest tests/test_digits_calculator.py::TestMatrixMultiply -v

# Test with coverage
uv run pytest tests/ --tb=short
```

## 🎨 Code Quality

### Linting & Code Analysis

The project uses professional linting tools for both languages:

#### Rust Code Quality

```bash
make lint-rust
# Runs: cargo clippy -- -D warnings
```

Clippy checks for:
- Performance improvements
- Memory safety issues  
- Idiomatic Rust patterns
- Potential bugs

#### Python Code Quality

```bash
make lint-python
# Runs: ruff check .
```

Ruff checks for:
- PEP 8 style violations
- Import organization
- Code complexity
- Common Python mistakes

### Running All Code Quality Checks

```bash
make lint
# Runs both Rust and Python linting
# Zero tolerance policy: all warnings treated as errors
```

### Configuration

#### Ruff Configuration (Python)

Located in `pyproject.toml`:
```toml
[tool.ruff.lint]
line-length = 88
target-version = "py38"
extend-select = ["E", "F", "W", "I", "UP", "C4"]
```

#### Rust Configuration (Cargo)

Standard clippy with deny-warnings policy in `Makefile`.

## 📚 Creating Your Own Rust Functions

### Step 1: Implement in Rust

Add your function to `digits-calculator/src/math.rs`:

```rust
pub fn factorial(n: i32) -> Result<u64, String> {
    if n < 0 {
        return Err("Factorial is not defined for negative numbers".to_string());
    }
    
    let mut result: u64 = 1;
    for i in 2..=(n as u64) {
        result *= i;
    }
    Ok(result)
}
```

### Step 2: Add Unit Tests

Add tests in the same file:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_factorial_basic() {
        assert_eq!(factorial(5).unwrap(), 120);
        assert_eq!(factorial(0).unwrap(), 1);
    }
}
```

### Step 3: Expose to Python Module

Add PyO3 wrapper in `digits-calculator/src/lib.rs`:

```rust
#[pyfunction]
fn factorial(n: i32) -> PyResult<u64> {
    match math::factorial(n) {
        Ok(result) => Ok(result),
        Err(msg) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(msg)),
    }
}

#[pymodule]
fn digits_calculator(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(factorial))?;
    Ok(())
}
```

### Step 4: Add Integration Tests

Create Python tests in `tests/test_digits_calculator.py`:

```python
def test_factorial_basic():
    result = digits_calculator.factorial(5)
    assert result == 120
```

### Step 5: Build and Test

```bash
make clean && make install
make test
```

## 🏗️ Development Workflow

### 1. Development Setup

```bash
git clone <your-fork>
cd rust-with-python
make install
```

### 2. Make Changes

- Edit Rust code in `digits-calculator/src/`
- Add tests as you develop
- Update documentation

### 3. Code Quality Checks

```bash
make fmt    # Format all code
make lint   # Check code quality
```

Fix any issues before continuing.

### 4. Build and Test

```bash
make clean        # Clean previous builds
make install      # Rebuild everything  
make test         # Run all 93 tests
```

All tests must pass:
```
✅ Rust unit tests passed! (30/30)
✅ Python integration tests passed! (63/63)
```

### 5. Run Application

```bash
make run
```

Verify your changes work in the demo.

### Complete Development Cycle

```bash
# Complete workflow
make all

# This runs:
# 1. make clean
# 2. make install  
# 3. make test
# 4. make lint
# 5. make run
```

Expected output:
```
🧹 Cleaning up build artifacts...
📦 Installing dependencies and building...
🧪 Running all tests...
✅ All tests passed! (93/93)
🔍 Checking code quality...
✅ All quality checks passed!
🚀 Running demonstration...
✅ Application completed successfully!
```

## 🔍 Troubleshooting

### "maturin failed" error

```bash
make clean
make install
```

This rebuilds everything from scratch.

### Module import error

Ensure you're in the virtual environment:
```bash
source .venv/bin/activate
python -c "import digits_calculator; print('✅ Import successful')"
```

### Test failures

Run tests individually to isolate issues:
```bash
make test-rust     # Check Rust unit tests
make test-python   # Check Python integration tests
```

Check the specific error messages for guidance.

### Build issues on macOS

If you encounter linking errors, ensure Xcode command line tools are installed:
```bash
xcode-select --install
```

## 📖 Additional Resources

- [PyO3 Documentation](https://pyo3.rs/)
- [maturin User Guide](https://maturin.rs/)
- [Rust Book](https://doc.rust-lang.org/book/)
- [uv Documentation](https://docs.astral.sh/uv/)

## 🛠️ Technologies Used

- **Rust 1.70+**: Core mathematical functions
- **Python 3.8+**: Interface and testing
- **PyO3 0.27.0**: Rust-Python bindings  
- **maturin**: Build tool for PyO3 projects
- **pytest**: Python testing framework
- **uv**: Fast Python package manager
- **ruff**: Python linting and formatting
- **cargo clippy**: Rust linting

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick contribution checklist:**
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality  
4. Ensure all tests pass (`make test`)
5. Check code quality (`make lint`)
6. Submit a pull request

## ✨ Tips for Using as a Template

1. **Rename the module**: Change `digits-calculator` to your project name
2. **Replace functions**: Modify `src/math.rs` with your own functions
3. **Update tests**: Add comprehensive tests for your functions
4. **Documentation**: Update this README with your project details
5. **Dependencies**: Add any additional Rust or Python dependencies you need

## 🎓 Learning Path

**New to Rust-Python integration?** Follow this path:

1. **Start here**: Run `make test` and explore the existing functions
2. **Understand the architecture**: Read `src/math.rs` (pure Rust) and `src/lib.rs` (PyO3 bindings)
3. **Modify existing functions**: Try changing the `calculate_pi` implementation
4. **Add a simple function**: Start with a basic math function
5. **Advanced features**: Explore error handling and complex data types like matrices
6. **Performance**: Benchmark your Rust vs pure Python implementations

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/macurandb/rust-with-python/issues)
- **Discussions**: [GitHub Discussions](https://github.com/macurandb/rust-with-python/discussions)
- **Template Questions**: Open an issue with the `template` label

---

**🎉 Happy coding!** Enjoy the power of Rust with the convenience of Python.