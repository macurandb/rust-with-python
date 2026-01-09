# macOS Troubleshooting Guide for PyO3 Projects

This guide documents common issues and solutions when working with PyO3 on macOS, based on real-world experience building the rust-with-python template.

## 🍎 Common macOS Issues and Solutions

### 1. **Conda Environment Conflicts**

**Problem**: `maturin` fails to build when Conda is active, showing linking errors.

**Symptoms**:
```bash
error: linking with `cc` failed: exit status: 1
ld: library not found for -lpython3.x
```

**Solution**: Always unset `CONDA_PREFIX` before building:
```bash
unset CONDA_PREFIX
maturin develop --release
```

**Our Implementation**: The Makefile automatically handles this:
```makefile
build:
	cd digits-calculator && unset CONDA_PREFIX && uv run maturin develop --release
```

### 2. **Xcode Command Line Tools Missing**

**Problem**: Build fails with missing compiler or linker errors.

**Symptoms**:
```bash
xcrun: error: invalid active developer path
error: failed to run custom build command for `pyo3-ffi`
```

**Solution**: Install Xcode command line tools:
```bash
xcode-select --install
```

**Verification**:
```bash
xcode-select -p
# Should output: /Applications/Xcode.app/Contents/Developer
# or: /Library/Developer/CommandLineTools
```

### 3. **Architecture Mismatches (Apple Silicon)**

**Problem**: Building for wrong architecture on M1/M2 Macs.

**Symptoms**:
```bash
ld: warning: ignoring file, building for macOS-x86_64 but attempting to link with file built for macOS-arm64
```

**Solution**: Force the correct architecture:
```bash
export ARCHFLAGS="-arch arm64"
maturin develop --release
```

**For universal builds**:
```bash
maturin build --release --universal2
```

### 4. **Python Version Conflicts**

**Problem**: Multiple Python installations causing confusion.

**Symptoms**:
```bash
Python.h: No such file or directory
error: Microsoft Visual C++ 14.0 is required (on macOS - wrong error message)
```

**Solution**: Use `uv` for consistent Python management:
```bash
# Our recommended approach
uv venv
source .venv/bin/activate
uv sync
```

**Debug Python version**:
```bash
python -c "import sysconfig; print(sysconfig.get_config_var('LDVERSION'))"
which python
python --version
```

### 5. **Dynamic Library Loading Issues**

**Problem**: Built extension can't be imported due to library path issues.

**Symptoms**:
```bash
ImportError: dlopen failed: Library not loaded
ImportError: No module named 'your_module'
```

**Solution**: Check library paths and rebuild:
```bash
# Check what libraries your extension needs
otool -L target/wheels/*.whl

# Clean rebuild
make clean
make install
```

### 6. **Homebrew Python Conflicts**

**Problem**: Homebrew Python interfering with system Python.

**Symptoms**:
```bash
Fatal Python error: initfsencoding: unable to load the file system codec
```

**Solution**: Use isolated environments:
```bash
# Avoid system Python conflicts
brew unlink python@3.x  # if needed
uv venv --python 3.11    # specify exact version
```

### 7. **Rust Toolchain Issues**

**Problem**: Wrong Rust version or missing components.

**Symptoms**:
```bash
error: failed to run `rustc` to learn about target-specific information
```

**Solution**: Update Rust toolchain:
```bash
rustup update stable
rustup default stable
rustc --version  # Should show recent version
```

### 8. **Permission Issues**

**Problem**: Permission denied when building or installing.

**Symptoms**:
```bash
PermissionError: [Errno 13] Permission denied
```

**Solution**: Never use sudo with Python packages:
```bash
# WRONG: sudo pip install maturin
# RIGHT: Use virtual environment
uv venv
source .venv/bin/activate
uv add maturin
```

## 🔧 Debugging Workflow

### Step-by-Step Troubleshooting:

1. **Clean everything**:
```bash
make clean
rm -rf .venv
rm -rf target/
```

2. **Check environment**:
```bash
echo $CONDA_PREFIX    # Should be empty
which python
python --version
rustc --version
```

3. **Fresh setup**:
```bash
uv venv
source .venv/bin/activate
uv sync
```

4. **Test build**:
```bash
cd digits-calculator
cargo check
cargo test
```

5. **Build extension**:
```bash
unset CONDA_PREFIX
uv run maturin develop --release -v
```

### Diagnostic Commands:

```bash
# Check Python configuration
python -c "import sysconfig; print(sysconfig.get_config_vars())"

# Check library paths
echo $DYLD_LIBRARY_PATH
echo $DYLD_FALLBACK_LIBRARY_PATH

# Check Rust targets
rustup show

# Check maturin version
maturin --version
```

## 🚀 Recommended macOS Setup

### 1. **Install Dependencies**:
```bash
# Install Xcode command line tools
xcode-select --install

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. **Project Setup**:
```bash
# Clone project
git clone https://github.com/macurandb/rust-with-python.git
cd rust-with-python

# Automated setup (handles everything)
make install
```

### 3. **Verify Installation**:
```bash
make test
# Should show: 93/93 tests passing
```

## 📋 Environment Checklist

Before reporting issues, verify:

- [ ] Xcode command line tools installed (`xcode-select -p`)
- [ ] Rust up to date (`rustc --version`)
- [ ] No active Conda environment (`echo $CONDA_PREFIX`)
- [ ] Using virtual environment (`which python`)
- [ ] Clean build directory (`make clean`)
- [ ] Latest uv version (`uv --version`)

## 🆘 Still Having Issues?

1. **Enable verbose output**:
```bash
cd digits-calculator
RUST_LOG=debug uv run maturin develop --release -v
```

2. **Check our working configuration**:
   - macOS Sonoma 14.x
   - Apple Silicon (M1/M2/M3)
   - Python 3.13.x
   - Rust 1.75+
   - PyO3 0.27.x

3. **Report issues**: [GitHub Issues](https://github.com/macurandb/rust-with-python/issues)
   - Include: macOS version, Python version, Rust version
   - Attach: Full error output with `-v` flag
   - Mention: Hardware (Intel vs Apple Silicon)

## 💡 Pro Tips

- Always use virtual environments (`uv venv`)
- Never mix Conda and pip in the same project
- Keep Rust toolchain updated
- Use `make clean` before rebuilding after errors
- Check `target/` directory size - clean if >1GB

---

**Last Updated**: January 2025  
**Tested On**: macOS Sonoma 14.x, Apple Silicon  
**Status**: Production Ready ✅