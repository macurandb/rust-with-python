# Contributing Guide

Thank you for your interest in contributing to this template project!

## Development Setup

### Prerequisites

- Python 3.13+
- Rust 1.70+
- `uv` (UV Python package manager)
- `git`

### Initial Setup

```bash
git clone <repository-url>
cd rust-with-python
make install
```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Edit Rust code in `digits-calculator/src/lib.rs`
- Edit Python code in `.py` files or `tests/`
- Update documentation as needed

### 3. Build and Test

```bash
make build      # Build the Rust extension
make test       # Run all tests
make lint       # Check code quality
make format     # Format code
```

### 4. Verify All Tests Pass

```bash
make clean
make install
make test
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "Add descriptive commit message"
```

### 6. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Style

### Python

- Use `ruff` for formatting (run `make format`)
- Follow PEP 8 conventions
- Add type hints where appropriate
- Add docstrings to functions and classes

### Rust

- Run `cargo fmt` for formatting
- Run `cargo clippy` for linting
- Add documentation comments (`///`)
- Include unit tests in `#[cfg(test)]` modules

### Examples

#### Python Function

```python
def calculate_something(value: int) -> str:
    """
    Calculate something interesting.

    Args:
        value: Input value to process

    Returns:
        Formatted result string
    """
    return str(value * 2)
```

#### Rust Function

```rust
/// Calculates something interesting.
///
/// # Arguments
/// * `value` - Input value to process
///
/// # Returns
/// * `PyResult<String>` - Formatted result
#[pyfunction]
fn calculate_something(value: i32) -> PyResult<String> {
    Ok((value * 2).to_string())
}
```

## Testing Guidelines

### Adding Tests

1. **Rust Unit Tests**: Add to the `#[cfg(test)]` module in `digits-calculator/src/lib.rs`
2. **Python Integration Tests**: Add to `tests/test_digits_calculator.py`

### Test Structure

Tests should follow this pattern:

```python
def test_feature_description():
    """Test that [feature] behaves correctly when [condition]."""
    result = module.function(input_value)
    assert result == expected_value
```

### Running Specific Tests

```bash
# Rust tests
cd digits-calculator
cargo test test_name --release

# Python tests
uv run pytest tests/test_filename.py::test_name -v
```

## Documentation

### Updating README

If your changes affect:

- Available commands → Update the "Available Commands" section
- Installation process → Update "Quick Start"
- API → Update "Rust Functions Reference"
- Setup → Update "Development Setup"

### Adding Docstrings

Always include docstrings for:

- Public functions
- Classes
- Modules

Use clear, descriptive language and include examples when helpful.

## Common Tasks

### Adding a New Rust Function

1. Add function to `digits-calculator/src/lib.rs`:

```rust
/// Describe what your function does.
#[pyfunction]
fn my_function(param: Type) -> PyResult<ReturnType> {
    // Implementation
    Ok(result)
}
```

2. Expose in the module:

```rust
#[pymodule]
fn digits_calculator(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // ... existing wraps ...
    m.add_wrapped(wrap_pyfunction!(my_function))?;
    Ok(())
}
```

3. Add unit tests:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_my_function() {
        let result = my_function(input).unwrap();
        assert_eq!(result, expected);
    }
}
```

4. Add integration tests in `tests/test_digits_calculator.py`

5. Run `make test` to verify

### Updating Dependencies

#### Python Dependencies

Edit `pyproject.toml` in the `[project]` dependencies section, then run:

```bash
uv sync --all-extras
```

#### Rust Dependencies

Edit `digits-calculator/Cargo.toml`, then run:

```bash
cd digits-calculator
cargo update
```

## Troubleshooting

### Build Failures

```bash
make clean
make install
```

### Test Failures

Run with verbose output:

```bash
make test  # This runs with -v flag
```

### Formatting Issues

Auto-fix most issues:

```bash
make format
```

## Pull Request Process

1. Ensure all tests pass: `make test`
2. Ensure code is formatted: `make format`
3. Ensure code is linted: `make lint`
4. Update README if needed
5. Provide a clear description of changes
6. Link any related issues

## Questions or Need Help?

- Check the main README.md
- Review existing code and tests for examples
- Check the PyO3 documentation: https://pyo3.rs/
- Open an issue with your question

Thank you for contributing! 🚀
