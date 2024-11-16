# Creating Python Packages on GitHub: A Practical Guide

Ever wondered how to turn your Python scripts into a proper package on GitHub? As a solar physicist who recently transformed magnetic field analysis code into a package, I'll share my experience and practical tips. Let's dive in!

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


## Creating Package Structure on GitHub

Create this structure in your cloned repository:
```plaintext
stability_analysis/                # Root project directory
├── stability_analysis/           # Package directory
│   ├── __init__.py              # Package initialization
│   └── core/                    # Core functionality
│       ├── __init__.py          # Subpackage initialization
│       └── module_files.py      # Implementation modules
├── tests/                        # Test directory
├── docs/                        # Documentation
├── .github/                     # GitHub specific
│   └── workflows/               # GitHub Actions
│       └── ci.yml              # CI configuration
├── setup.py                     # Installation configuration
└── requirements.txt             # Dependencies
```

For e.g., 
   ```
   mkdir -p stability_analysis/stability_analysis/core # To create the directory structure

   # To place the files
   # Main __init__.py
   touch stability_analysis/stability_analysis/__init__.py

   # Core __init__.py
   touch stability_analysis/stability_analysis/core/__init__.py

   ```

## Setting Up GitHub-Specific Files

1. **requirements.txt**
   ```
   numpy>=1.21.0
   scipy>=1.7.0
   matplotlib>=3.4.0
   pytest>=6.2.0
   pytest-cov>=2.12.0
   black>=21.5b2
   flake8>=3.9.0
   ```

2. **__init__.py**

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

3. **.github/workflows/ci.yml**
   The `.github/workflows/ci.yml` file is part of GitHub Actions, which is GitHub's built-in continuous integration and continuous deployment (CI/CD) system. Its purpose is to automate various tasks when you push code or create pull requests. Let me explain the CI workflow from the example script below:

   ```yaml 
   name: CI/CD

   # 1. When it runs:
   
   on:
     push:
       branches: [ main ]  # Runs when code is pushed to main branch
     pull_request:
       branches: [ main ]  # Runs when a pull request is made to main branch
  
   # 2. What it does:
   
   jobs:
     test:  # First job: testing
       runs-on: ubuntu-latest
       strategy:
         matrix:
           python-version: [3.8, 3.9]  # Tests on multiple Python versions

       steps:
       - uses: actions/checkout@v2  # Gets your code
       
       - name: Set up Python
         uses: actions/setup-python@v2  # Sets up Python
       
       - name: Install dependencies  # Installs requirements
         run: |
           pip install -r requirements.txt
           pip install -e .[dev]
       
       - name: Code formatting check  # Checks code style
         run: |
           black . --check  # Checks code formatting
           isort . --check  # Checks import ordering
           flake8 .  # Checks PEP8 compliance
       
       - name: Type checking  # Checks type hints
         run: |
           mypy stability_analysis
       
       - name: Run tests  # Runs test suite
         run: |
           pytest tests/ --cov=stability_analysis

     docs:  # Second job: documentation
       needs: test  # Only runs if tests pass
       if: github.ref == 'refs/heads/main'  # Only runs on main branch
       steps:
       - name: Build documentation
         run: |
           cd docs
           make html
   ```

   Main benefits:
   1. **Automated Testing**: Automatically runs tests on each code change
   2. **Code Quality**: Enforces coding standards and style
   3. **Documentation**: Automatically builds and deploys documentation
   4. **Multiple Python Versions**: Tests compatibility across versions
   5. **Pull Request Checks**: Validates changes before merging

   Example of what it looks like in action:
   ```python
   # If you make this change:
   def analyze_data(x):
       return x + 1  # Missing type hint

   # And push to GitHub, the CI will fail with:
   # mypy error: Missing type annotation for parameter 'x'

   # After fixing:
   def analyze_data(x: float) -> float:
       return x + 1  # CI passes
   ```

   To set this up:
   1. Create `.github/workflows/ci.yml` in your repository
   2. Enable GitHub Actions in repository settings
   3. Add status badges to README:
   ```markdown
   ![Tests](https://github.com/username/repo/workflows/CI/badge.svg)
   [![codecov](https://codecov.io/gh/username/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/username/repo)
   ```
   

4. **setup.py**

   Making Your Package Installable

   The `setup.py` file is your package's ID card. Here's an example:

   ```python
   from setuptools import setup, find_packages

   with open("README.md", "r", encoding="utf-8") as fh:
       long_description = fh.read()

   with open("requirements.txt", "r", encoding="utf-8") as fh:
       requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

   setup(
       name="stability_analysis",
       version="0.1.0",
       author="Manu Gupta",
       author_email="your.email@example.com",
       description="Analysis tools for solar magnetic field stability",
       long_description=long_description,
       long_description_content_type="text/markdown",
       url="https://github.com/yourusername/stability_analysis",
       packages=find_packages(),
       classifiers=[
           "Development Status :: 3 - Alpha",
           "Intended Audience :: Science/Research",
           "Topic :: Scientific/Engineering :: Physics",
           "Programming Language :: Python :: 3",
           "License :: OSI Approved :: MIT License",
           "Operating System :: OS Independent",
       ],
       python_requires=">=3.8",
       install_requires=requirements,
       extras_require={
           "dev": [
               "pytest",
               "pytest-cov",
               "black",
               "isort",
               "flake8",
               "mypy",
               "sphinx",
           ]
       },
   )
   ```


## Installing and Using Your Package

Once your package is on GitHub, others can install it:

```bash
# For users
pip install git+https://github.com/yourusername/stability_analysis.git

# For development
git clone https://github.com/yourusername/stability_analysis.git
cd stability_analysis
pip install -e .
```

Using the package is then as simple as:

```python
from stability_analysis import PILDetector, MagneticField

# Load magnetic field data
field = MagneticField("data_path")
bz = field.load_boundary_field("20170906_0900")

# Detect PIL
detector = PILDetector(bz)
pil_map = detector.detect()
   ```
