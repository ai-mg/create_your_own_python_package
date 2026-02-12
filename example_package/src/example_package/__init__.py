"""
Example Package - A demonstration of modern Python packaging.

This package provides simple utilities for calculations and data processing,
demonstrating best practices for Python package structure and configuration.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Import main classes for easy access
from .calculator import Calculator
from .core.data_processor import DataProcessor

# Define public API
__all__ = [
    "Calculator",
    "DataProcessor",
]
