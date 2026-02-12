# Example Package

An example Python package demonstrating modern best practices for Python packaging in 2026.

## Features

- Modern `pyproject.toml` configuration (PEP 621)
- Src-layout structure
- Type hints with `py.typed`
- Comprehensive testing with pytest
- CI/CD with GitHub Actions
- Code quality tools (ruff, black, mypy)

## Installation

### From source (development)

```bash
git clone https://github.com/yourusername/example_package.git
cd example_package
pip install -e .[dev]
```

### From PyPI (when published)

```bash
pip install example_package
```

## Usage

```python
from example_package import Calculator, DataProcessor

# Use the calculator
calc = Calculator()
result = calc.add(5, 3)
print(f"5 + 3 = {result}")

# Process data
processor = DataProcessor()
data = [1, 2, 3, 4, 5]
processed = processor.process(data)
print(f"Processed data: {processed}")
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/example_package.git
cd example_package

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=example_package --cov-report=html

# Run specific test file
pytest tests/test_calculator.py
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/
```

### Building

```bash
# Install build tool
pip install build

# Build package
python -m build
```

## License

MIT License - see LICENSE file for details.
