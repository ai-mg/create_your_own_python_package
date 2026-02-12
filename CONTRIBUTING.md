# How to Use This Repository

This repository is a comprehensive guide and template for creating Python packages using modern best practices (2026).

## What's Included

### 1. Comprehensive Guide (README.md)
The main README provides detailed explanations of:
- Modern Python packaging standards (PEP 517, 518, 621)
- Project structure (src-layout)
- Configuration files
- Testing and CI/CD
- Publishing to PyPI

### 2. Working Example (`example_package/`)
A complete, functional Python package that demonstrates all concepts:
- Proper package structure
- Type hints and documentation
- Comprehensive tests
- GitHub Actions workflow
- Pre-commit hooks

## Getting Started

### Option 1: Learn from the Example

1. **Explore the example package:**
   ```bash
   cd example_package
   ```

2. **Install and test it:**
   ```bash
   pip install -e .[dev]
   pytest
   ```

3. **Examine the files:**
   - `pyproject.toml` - Configuration and metadata
   - `src/example_package/` - Package source code
   - `tests/` - Test files
   - `.github/workflows/ci.yml` - CI/CD pipeline

### Option 2: Use as a Template

1. **Copy the example structure:**
   ```bash
   cp -r example_package your_package_name
   cd your_package_name
   ```

2. **Update the package name:**
   - Rename `src/example_package/` to `src/your_package_name/`
   - Update `pyproject.toml` with your package details
   - Update `README.md` with your package description

3. **Replace example code:**
   - Update `src/your_package_name/__init__.py`
   - Replace example modules with your code
   - Update tests to match your code

4. **Test and publish:**
   ```bash
   pip install -e .[dev]
   pytest
   python -m build
   ```

### Option 3: Start from Scratch

Follow the step-by-step guide in the main README.md to create your package from scratch.

## Key Features

### Modern Standards
- **pyproject.toml**: Single source of truth for package metadata (PEP 621)
- **src-layout**: Prevents common import issues
- **Type hints**: Full typing support with `py.typed`

### Code Quality
- **Black**: Automatic code formatting
- **Ruff**: Fast Python linter (replaces flake8)
- **mypy**: Static type checking
- **pytest**: Comprehensive testing framework

### Automation
- **GitHub Actions**: Automated testing on multiple Python versions and OS
- **Pre-commit**: Run checks before every commit
- **Trusted Publishing**: Secure PyPI publishing without tokens

## Best Practices Demonstrated

1. ✅ **Src-layout** - Industry standard package structure
2. ✅ **Type hints** - Modern Python 3.9+ type annotations
3. ✅ **Comprehensive tests** - 98% code coverage
4. ✅ **Documentation** - Google-style docstrings
5. ✅ **CI/CD** - Automated testing and building
6. ✅ **Code quality** - Formatted and linted
7. ✅ **Security** - No vulnerabilities (CodeQL checked)
8. ✅ **Modern tools** - Latest versions of all tools

## Questions or Issues?

- Check the main [README.md](README.md) for detailed explanations
- Look at the [example_package/](example_package/) for implementation details
- Review the inline code comments and docstrings
- Open an issue if you need help

## Contributing

If you find errors or have suggestions for improvements, please open an issue or pull request!

---

**Happy packaging! 🎉**
