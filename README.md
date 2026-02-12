# Creating Python Packages on GitHub: A Practical Guide (2026 Edition)

Ever wondered how to turn your Python scripts into a proper package on GitHub? This guide covers the latest best practices for creating Python packages using modern standards (PEP 517, PEP 518, PEP 621) and tools. Let's dive in!

> **Note**: This guide has been updated to reflect the current best practices as of 2026, including the use of `pyproject.toml` as the primary configuration file and the src-layout pattern.

## Getting Started with GitHub

1. **Create a New Repository**
   - Go to GitHub and click "New repository"
   - Name it "your_package_name" which is "stability_analysis" in my case
   - Add README.md, .gitignore (Python), and LICENSE
   - Initialize repository

2. **Clone Repository Locally**
   ```bash
   git clone https://github.com/yourusername/stability_analysis.git
   cd stability_analysis
   ```

3. **Set Up Virtual Environment** 
   Use venv or conda or whatever you prefer
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```


## Modern Package Structure (Recommended: src-layout)

The **src-layout** is the modern best practice for Python packages. It prevents common issues and ensures proper testing:

```plaintext
your_package/                      # Root project directory
├── src/                          # Source directory (recommended)
│   └── your_package/            # Package directory
│       ├── __init__.py          # Package initialization
│       ├── py.typed             # Marker for type hints
│       └── core/                # Core functionality
│           ├── __init__.py      # Subpackage initialization
│           └── module_files.py  # Implementation modules
├── tests/                        # Test directory
│   ├── __init__.py
│   └── test_module.py
├── docs/                         # Documentation
│   ├── conf.py
│   └── index.rst
├── .github/                      # GitHub specific
│   └── workflows/               # GitHub Actions
│       └── ci.yml              # CI configuration
├── pyproject.toml               # Modern project configuration (PEP 621)
├── setup.py                     # Optional backward compatibility
├── requirements.txt             # Dependencies (or use pyproject.toml)
├── requirements-dev.txt         # Development dependencies
├── .gitignore                   # Git ignore patterns
├── LICENSE                      # License file
├── README.md                    # Project documentation
└── MANIFEST.in                  # Include/exclude package data
```

### Why src-layout?

1. **Import Protection**: Prevents accidentally importing from the source directory during development
2. **Testing Integrity**: Ensures tests run against the installed package, not source files
3. **Cleaner Namespace**: Separates package code from project files
4. **Industry Standard**: Widely adopted by the Python community

### Alternative: Flat Layout

For simple packages, you can use a flat layout (package directly in root), but src-layout is recommended for most projects:

```plaintext
your_package/                      # Root project directory
├── your_package/                 # Package directory (no src/)
│   ├── __init__.py
│   └── module.py
├── tests/
├── pyproject.toml
└── README.md
```

### Creating the Directory Structure

```bash
# Using src-layout (recommended)
mkdir -p your_package/src/your_package/core
mkdir -p your_package/tests
mkdir -p your_package/docs
mkdir -p your_package/.github/workflows

# Create essential files
touch your_package/src/your_package/__init__.py
touch your_package/src/your_package/py.typed
touch your_package/src/your_package/core/__init__.py
touch your_package/tests/__init__.py
touch your_package/pyproject.toml
touch your_package/README.md
touch your_package/.gitignore
```

## Modern Configuration: pyproject.toml (PEP 621)

The `pyproject.toml` file is now the **standard** way to configure Python projects (replacing setup.py). It follows PEP 517, PEP 518, and PEP 621 standards.

### Basic pyproject.toml Example

```toml
[build-system]
# PEP 517/518 - Specify the build backend
requires = ["setuptools>=65.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
# PEP 621 - Project metadata
name = "your_package"
version = "0.1.0"
description = "A short description of your package"
readme = "README.md"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
requires-python = ">=3.9"
dependencies = [
    "numpy>=1.24.0",
    "scipy>=1.10.0",
    "matplotlib>=3.7.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]
docs = [
    "sphinx>=7.0.0",
    "sphinx-rtd-theme>=1.3.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/your_package"
Documentation = "https://your_package.readthedocs.io"
Repository = "https://github.com/yourusername/your_package.git"
Issues = "https://github.com/yourusername/your_package/issues"

# Tool-specific configurations
[tool.setuptools.packages.find]
where = ["src"]

[tool.black]
line-length = 88
target-version = ['py39', 'py310', 'py311', 'py312']

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]
ignore = []

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
addopts = "--cov=your_package --cov-report=html --cov-report=term"
```

### Alternative Build Backends

Modern Python packaging supports multiple build backends. Choose based on your needs:

#### 1. Setuptools (Most Common)
```toml
[build-system]
requires = ["setuptools>=65.0", "wheel"]
build-backend = "setuptools.build_meta"
```

#### 2. Hatchling (Modern, Fast)
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/your_package"]
```

#### 3. Flit (Minimal, Simple)
```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"
```

#### 4. Poetry (Dependency Management)
```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "your_package"
version = "0.1.0"
# ... other metadata

[tool.poetry.dependencies]
python = "^3.9"
numpy = "^1.24.0"
```

## The __init__.py File

The `__init__.py` file is crucial - it's not just a package marker! Here's an example `__init__.py` file below followed by the description showing its different roles:

   ```python
   """
   Stability Analysis Package for Solar Magnetic Fields.
   Provides tools for analyzing magnetic stability including PIL detection
   and decay index calculation.
   """

   # 1. Package Metadata
   __version__ = '0.1.0'
   __author__ = 'Your Name'
   __email__ = 'your.email@example.com'

   # 2. Import Control
   from .core.pil_detection import PILDetector
   from .core.magnetic_field import MagneticField
   from .core.decay_index import DecayIndexCalculator

   # 3. Namespace Organization
   __all__ = [
       'PILDetector',
       'MagneticField',
       'DecayIndexCalculator',
   ]

   # 4. Default Configuration   # Global variables for my code
   default_config = {
       'grid_spacing': 0.72,
       'critical_index': 1.5
   }

   # 5. Lazy Loading Example
   def get_analyzer(data_path: str):
       """Load analyzer only when needed to save memory."""
       from .core.analysis import MagneticFieldAnalyzer
       return MagneticFieldAnalyzer(data_path)

   # 6. Package-level Exception Classes
   class StabilityAnalysisError(Exception):
       """Base exception for the package."""
       pass
   ```

   The `__init__.py` file serves several important roles in Python packages:

   1. **Package Marker**:
   ```plaintext
   my_package/
       __init__.py      # Marks this directory as a Python package
       module1.py
       module2.py
   ```
   Without `__init__.py`, Python would treat the directory as just a folder, not a package.

   2. **Import Control**:
   Clean imports (instead of long paths)
   ```python
   # __init__.py
   # Define what should be available when someone does "from package import *"
   __all__ = ['PILDetector', 'MagneticField']

   # Make classes available at package level
   from .pil_detection import PILDetector
   from .magnetic_field import MagneticField
   ```

   This enables:
   ```python
   # Without __init__.py:
   from my_package.pil_detection import PILDetector

   # With __init__.py:
   from my_package import PILDetector  # Cleaner import
   ```


   Or, 

   ```python
   #Controlled import with __all__
   from stability_analysis import *  # Only imports what's in __all__
   ```

   3. **Package Initialization**:
   ```python
   # __init__.py
   # Run code when package is imported
   print("Initializing package...")

   # Define package-level variables
   __version__ = '0.1.0'
   __author__ = 'Manu Gupta'

   # Initialize package-level settings
   default_config = {
       'grid_spacing': 0.72,
       'critical_index': 1.5
   }
   ```

   4. **Namespace Organization**:
   ```python
   # Without __init__.py:
   stability_analysis/
       core/
           pil_detection.py
           magnetic_field.py

   # Need to import like this:
   from stability_analysis.core.pil_detection import PILDetector
   from stability_analysis.core.magnetic_field import MagneticField

   # With __init__.py:
   # stability_analysis/__init__.py
   from .core.pil_detection import PILDetector
   from .core.magnetic_field import MagneticField

   # Can now import like this:
   from stability_analysis import PILDetector, MagneticField
   ```

   5. **Subpackage Organization**:
   ```python
   stability_analysis/
       __init__.py
       core/
           __init__.py
           pil_detection.py
           magnetic_field.py
       utils/
           __init__.py
           helpers.py
   ```

   Each `__init__.py` controls its own namespace:

   ```python
   # stability_analysis/core/__init__.py
   from .pil_detection import PILDetector
   from .magnetic_field import MagneticField

   __all__ = ['PILDetector', 'MagneticField']

   # stability_analysis/__init__.py
   from .core import PILDetector, MagneticField
   from .utils import helpers

   __all__ = ['PILDetector', 'MagneticField', 'helpers']
   ```

   6. **Relative Imports**:
   ```python
   # stability_analysis/core/pil_detection.py
   from .magnetic_field import MagneticField  # Same directory
   from ..utils import helpers  # Parent directory
   ```

   7. **Package Version Control**:
   Version checking
   ```python
   # stability_analysis/__init__.py
   __version__ = '0.1.0'

   # In code:
   import stability_analysis
   print(stability_analysis.__version__)
   ```

   8. **Lazy Loading**:
   Lazy loading when needed
   analyzer = stability_analysis.get_analyzer("data/")

   ```python
   # __init__.py
   def get_detector():
       # Only import when needed
       from .core.pil_detection import PILDetector
       return PILDetector()
   ```

## Modern GitHub Actions CI/CD

The `.github/workflows/ci.yml` file automates testing, code quality checks, and deployment. Here's a modern example:

```yaml
name: CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  release:
    types: [ published ]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.9", "3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]
    
    - name: Lint with ruff
      run: |
        ruff check .
    
    - name: Format check with black
      run: |
        black --check .
    
    - name: Type check with mypy
      run: |
        mypy src/
    
    - name: Test with pytest
      run: |
        pytest tests/ --cov=your_package --cov-report=xml --cov-report=term
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v4
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
        fail_ci_if_error: false

  build:
    needs: test
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.12"
    
    - name: Install build dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    
    - name: Build package
      run: python -m build
    
    - name: Check package
      run: twine check dist/*
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v4
      with:
        name: dist
        path: dist/

  publish:
    needs: build
    runs-on: ubuntu-latest
    if: github.event_name == 'release' && github.event.action == 'published'
    environment:
      name: pypi
      url: https://pypi.org/p/your_package
    permissions:
      id-token: write  # Required for trusted publishing
    
    steps:
    - name: Download artifacts
      uses: actions/download-artifact@v4
      with:
        name: dist
        path: dist/
    
    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
```

### Key Features of Modern CI/CD:

1. **Multiple OS Testing**: Tests on Ubuntu, Windows, and macOS
2. **Python Version Matrix**: Tests across multiple Python versions
3. **Dependency Caching**: Speeds up workflow with pip cache
4. **Modern Linting**: Uses `ruff` (faster than flake8) and `black`
5. **Type Checking**: Validates type hints with `mypy`
6. **Code Coverage**: Uploads coverage to Codecov
7. **Package Building**: Uses modern `build` tool (PEP 517)
8. **Trusted Publishing**: Uses OpenID Connect for secure PyPI publishing (no tokens needed!)

### Status Badges for README

Add these badges to show build status:

```markdown
[![CI/CD](https://github.com/username/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/username/repo/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/username/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/username/repo)
[![PyPI version](https://badge.fury.io/py/your-package.svg)](https://badge.fury.io/py/your-package)
[![Python versions](https://img.shields.io/pypi/pyversions/your-package.svg)](https://pypi.org/project/your-package/)
[![License](https://img.shields.io/github/license/username/repo.svg)](https://github.com/username/repo/blob/main/LICENSE)
```

## Additional Important Files

### 1. .gitignore

Essential for excluding build artifacts and temporary files:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Type checking
.mypy_cache/
.pytype/

# OS
.DS_Store
Thumbs.db
```

### 2. LICENSE

Choose an appropriate license. Popular choices:
- **MIT**: Permissive, simple
- **Apache 2.0**: Permissive with patent protection
- **GPL-3.0**: Copyleft license
- **BSD-3-Clause**: Permissive with attribution

### 3. MANIFEST.in (Optional)

If you need to include non-Python files in your package:

```
include README.md
include LICENSE
include requirements.txt
recursive-include src/your_package/data *
recursive-include docs *.rst
global-exclude __pycache__
global-exclude *.py[co]
```

### 4. py.typed

A marker file to indicate your package supports type hints:

```bash
touch src/your_package/py.typed
```

This allows type checkers like mypy to use your package's type hints.

### 5. setup.py (Optional - for backward compatibility)

While `pyproject.toml` is now standard, you may want a minimal `setup.py` for backward compatibility:

```python
"""Setup script for backward compatibility."""
from setuptools import setup

# All configuration is in pyproject.toml
setup()
```

Or a more detailed version if not using pyproject.toml:

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="your_package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_package",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/your_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "ruff", "mypy"],
    },
)
```


## Building and Publishing Your Package

### Building the Package

Modern Python uses the `build` tool (PEP 517):

```bash
# Install build tool
pip install build

# Build both wheel and source distribution
python -m build

# Output:
# dist/
#   your_package-0.1.0-py3-none-any.whl
#   your_package-0.1.0.tar.gz
```

### Publishing to PyPI

#### Method 1: Trusted Publishing (Recommended - No tokens!)

GitHub Actions can publish directly to PyPI using OpenID Connect:

1. **Configure PyPI**:
   - Go to PyPI → Account Settings → Publishing
   - Add a new "trusted publisher"
   - Enter: GitHub username, repository name, workflow name, environment name

2. **Use in GitHub Actions** (already shown in CI/CD section above)

#### Method 2: Using API Token

```bash
# Install twine
pip install twine

# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ your_package

# Upload to PyPI
twine upload dist/*
```

### Installing Your Package

Once published on GitHub or PyPI:

```bash
# From PyPI
pip install your_package

# From GitHub (latest)
pip install git+https://github.com/yourusername/your_package.git

# From GitHub (specific branch/tag)
pip install git+https://github.com/yourusername/your_package.git@v0.1.0

# For development (editable install)
git clone https://github.com/yourusername/your_package.git
cd your_package
pip install -e .[dev]
```

### Using Your Package

```python
from your_package import YourClass

# Use your package
obj = YourClass()
result = obj.process()
```

## Modern Best Practices Summary

### Development Tools (2026)

1. **Ruff**: Fast Python linter and formatter (replaces flake8, isort, and more)
2. **Black**: Code formatter (or use ruff format)
3. **mypy**: Static type checker
4. **pytest**: Testing framework
5. **pre-commit**: Git hooks for code quality

### Pre-commit Configuration

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

Install pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

### Type Hints

Modern Python packages should include type hints:

```python
from typing import List, Optional, Dict, Any

def process_data(
    data: List[float],
    threshold: float = 0.5,
    options: Optional[Dict[str, Any]] = None
) -> List[float]:
    """Process data with optional filtering.
    
    Args:
        data: Input data points
        threshold: Filtering threshold
        options: Optional processing options
        
    Returns:
        Processed data
        
    Raises:
        ValueError: If data is empty
    """
    if not data:
        raise ValueError("Data cannot be empty")
    
    options = options or {}
    return [x for x in data if x > threshold]
```

### Testing Best Practices

```python
# tests/test_module.py
import pytest
from your_package import YourClass

def test_basic_functionality():
    """Test basic functionality."""
    obj = YourClass()
    result = obj.process()
    assert result is not None

def test_error_handling():
    """Test error handling."""
    obj = YourClass()
    with pytest.raises(ValueError):
        obj.process(invalid_input=True)

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    """Test using fixture."""
    obj = YourClass()
    result = obj.process(sample_data)
    assert len(result) == len(sample_data)
```

## Version Management

### Semantic Versioning

Follow [SemVer](https://semver.org/): `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Dynamic Versioning

Keep version in one place using `__version__`:

```python
# src/your_package/__init__.py
__version__ = "0.1.0"
```

```toml
# pyproject.toml
[project]
dynamic = ["version"]

[tool.setuptools.dynamic]
version = {attr = "your_package.__version__"}
```

## Documentation

### Docstring Format (Google Style)

```python
def complex_function(param1: int, param2: str) -> bool:
    """Brief description of function.
    
    Longer description explaining what the function does,
    its purpose, and any important details.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param1 is negative
        TypeError: When param2 is not a string
    
    Example:
        >>> result = complex_function(5, "test")
        >>> print(result)
        True
    """
    if param1 < 0:
        raise ValueError("param1 must be non-negative")
    return len(param2) > param1
```

### Sphinx Documentation

Basic `docs/conf.py`:

```python
project = 'Your Package'
copyright = '2026, Your Name'
author = 'Your Name'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Google/NumPy style docstrings
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

html_theme = 'sphinx_rtd_theme'
```

## Quick Start Checklist

- [ ] Create repository with README, LICENSE, .gitignore
- [ ] Set up src-layout structure
- [ ] Create `pyproject.toml` with metadata and dependencies
- [ ] Write package code with type hints
- [ ] Add `__init__.py` files
- [ ] Create `py.typed` marker
- [ ] Write tests in `tests/` directory
- [ ] Set up `.github/workflows/ci.yml`
- [ ] Install pre-commit hooks
- [ ] Add documentation
- [ ] Build package: `python -m build`
- [ ] Test locally: `pip install -e .[dev]`
- [ ] Run tests: `pytest`
- [ ] Publish to PyPI

## Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [PEP 517 - Build System](https://www.python.org/dev/peps/pep-0517/)
- [PEP 518 - Build System Dependencies](https://www.python.org/dev/peps/pep-0518/)
- [PEP 621 - Project Metadata](https://www.python.org/dev/peps/pep-0621/)
- [setuptools documentation](https://setuptools.pypa.io/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)

---

**See the `example_package/` directory for a complete working example!**
