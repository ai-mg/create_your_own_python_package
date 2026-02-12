"""Test package initialization."""

from example_package import Calculator, DataProcessor, __version__


def test_version() -> None:
    """Test version is defined."""
    assert __version__ == "0.1.0"


def test_imports() -> None:
    """Test that main classes are importable."""
    assert Calculator is not None
    assert DataProcessor is not None


def test_calculator_import() -> None:
    """Test Calculator can be instantiated."""
    calc = Calculator()
    assert calc is not None


def test_data_processor_import() -> None:
    """Test DataProcessor can be instantiated."""
    processor = DataProcessor()
    assert processor is not None
