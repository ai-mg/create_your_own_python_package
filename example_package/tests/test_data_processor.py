"""Tests for the data processor module."""

import pytest

from example_package import DataProcessor


def test_data_processor_identity() -> None:
    """Test identity operation."""
    processor = DataProcessor()
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = processor.process(data, operation="identity")
    assert result == data


def test_data_processor_square() -> None:
    """Test square operation."""
    processor = DataProcessor()
    data = [1.0, 2.0, 3.0]
    result = processor.process(data, operation="square")
    assert result == pytest.approx([1.0, 4.0, 9.0])


def test_data_processor_sqrt() -> None:
    """Test square root operation."""
    processor = DataProcessor()
    data = [1.0, 4.0, 9.0, 16.0]
    result = processor.process(data, operation="sqrt")
    assert result == pytest.approx([1.0, 2.0, 3.0, 4.0])


def test_data_processor_normalize() -> None:
    """Test normalization operation."""
    processor = DataProcessor()
    data = [0.0, 5.0, 10.0]
    result = processor.process(data, operation="normalize")
    assert result == pytest.approx([0.0, 0.5, 1.0])


def test_data_processor_auto_normalize() -> None:
    """Test automatic normalization."""
    processor = DataProcessor(normalize=True)
    data = [10.0, 20.0, 30.0]
    result = processor.process(data, operation="square")
    # After squaring: [100, 400, 900], normalized to [0, 0.375, 1.0]
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)


def test_data_processor_empty_data() -> None:
    """Test that empty data raises ValueError."""
    processor = DataProcessor()
    with pytest.raises(ValueError, match="Data cannot be empty"):
        processor.process([])


def test_data_processor_invalid_operation() -> None:
    """Test that invalid operation raises ValueError."""
    processor = DataProcessor()
    with pytest.raises(ValueError, match="Invalid operation"):
        processor.process([1, 2, 3], operation="invalid")


def test_statistics() -> None:
    """Test statistics calculation."""
    processor = DataProcessor()
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    stats = processor.statistics(data)

    assert stats["mean"] == pytest.approx(3.0)
    assert stats["min"] == pytest.approx(1.0)
    assert stats["max"] == pytest.approx(5.0)
    assert "std" in stats


def test_statistics_empty_data() -> None:
    """Test statistics with empty data raises ValueError."""
    processor = DataProcessor()
    with pytest.raises(ValueError, match="Data cannot be empty"):
        processor.statistics([])


def test_filter_outliers() -> None:
    """Test outlier filtering."""
    processor = DataProcessor()
    # Data with one clear outlier
    data = [1.0, 2.0, 3.0, 4.0, 5.0, 100.0]
    result = processor.filter_outliers(data, threshold=2.0)

    # The outlier (100) should be removed
    assert len(result) < len(data)
    assert 100.0 not in result


def test_filter_outliers_small_dataset() -> None:
    """Test outlier filtering with small dataset."""
    processor = DataProcessor()
    data = [1.0, 2.0]
    result = processor.filter_outliers(data)
    # Should return original data for small datasets
    assert result == data


def test_filter_outliers_empty() -> None:
    """Test outlier filtering with empty data."""
    processor = DataProcessor()
    with pytest.raises(ValueError, match="Data cannot be empty"):
        processor.filter_outliers([])


@pytest.fixture
def processor() -> DataProcessor:
    """Provide a data processor instance for tests."""
    return DataProcessor()


def test_with_fixture(processor: DataProcessor) -> None:
    """Test using pytest fixture."""
    data = [1.0, 2.0, 3.0]
    result = processor.process(data, operation="square")
    assert len(result) == len(data)
