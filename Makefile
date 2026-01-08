.PHONY: help install build run clean all

help:
	@echo "Available targets:"
	@echo "  make install   - Install Python dependencies and build Rust extension with uv"
	@echo "  make build     - Build the Rust extension with uv"
	@echo "  make run       - Run the Python project with uv"
	@echo "  make all       - Install, build, and run (complete setup)"
	@echo "  make clean     - Clean build artifacts"
	@echo ""
	@echo "Usage: make [target]"
	@echo "Example: make all"

install:
	@echo "🔧 Installing dependencies and building Rust extension with uv..."
	@echo ""
	@echo "Step 1: Syncing Python environment with uv..."
	uv sync --all-extras
	@echo ""
	@echo "Step 2: Building Rust extension with maturin (using uv)..."
	cd digits-calculator && unset CONDA_PREFIX && uv run maturin develop --release
	@echo ""
	@echo "✅ Installation complete!"

build:
	@echo "🔨 Building Rust extension with uv..."
	cd digits-calculator && unset CONDA_PREFIX && uv run maturin develop --release
	@echo "✅ Build complete!"

run:
	@echo "🚀 Running the Python project with uv..."
	@echo ""
	uv run python main.py

test:
	@echo "🧪 Running tests..."
	@echo ""
	@echo "Running Rust tests..."
	cd digits-calculator && cargo test --release
	@echo ""
	@echo "Running Python integration tests..."
	uv run pytest tests/ -v
	@echo ""
	@echo "✅ All tests passed!"

lint:
	@echo "🔍 Running code quality checks with ruff..."
	uv run ruff check .
	@echo "✅ Linting complete!"

format:
	@echo "📝 Formatting code with ruff..."
	uv run ruff format .
	@echo "✅ Formatting complete!"

all: install run
	@echo ""
	@echo "✅ Project setup and execution complete!"

clean:
	@echo "🧹 Cleaning up build artifacts..."
	cd digits-calculator && cargo clean
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".venv" -exec rm -rf {} + 2>/dev/null || true
	rm -f digits-calculator/libdigits_calculator.so
	@echo "✅ Cleanup complete!"

.DEFAULT_GOAL := help
