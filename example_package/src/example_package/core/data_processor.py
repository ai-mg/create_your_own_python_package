"""Data processing module with numpy integration."""

from typing import Any

import numpy as np
import numpy.typing as npt


class DataProcessor:
    """Process numerical data with various transformations.

    This class demonstrates how to integrate numpy with type hints
    and provides common data processing operations.

    Attributes:
        normalize: Whether to normalize data by default

    Example:
        >>> processor = DataProcessor(normalize=True)
        >>> data = [1, 2, 3, 4, 5]
        >>> result = processor.process(data)
        >>> print(result)
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    def __init__(self, normalize: bool = False) -> None:
        """Initialize the data processor.

        Args:
            normalize: Whether to normalize data by default
        """
        self.normalize = normalize

    def process(
        self,
        data: list[float],
        operation: str = "identity",
        **kwargs: Any,
    ) -> list[float]:
        """Process data with specified operation.

        Args:
            data: Input data to process
            operation: Operation to apply ('identity', 'square', 'sqrt', 'normalize')
            **kwargs: Additional arguments for specific operations

        Returns:
            Processed data as a list

        Raises:
            ValueError: If data is empty or operation is invalid

        Example:
            >>> processor = DataProcessor()
            >>> processor.process([1, 2, 3], operation='square')
            [1.0, 4.0, 9.0]
        """
        if not data:
            raise ValueError("Data cannot be empty")

        arr = np.array(data, dtype=float)

        if operation == "identity":
            result = arr
        elif operation == "square":
            result = arr**2
        elif operation == "sqrt":
            result = np.sqrt(np.abs(arr))
        elif operation == "normalize":
            result = self._normalize(arr)
        else:
            raise ValueError(f"Invalid operation: {operation}")

        if self.normalize and operation != "normalize":
            result = self._normalize(result)

        return result.tolist()

    def _normalize(
        self, arr: npt.NDArray[np.floating[Any]]
    ) -> npt.NDArray[np.floating[Any]]:
        """Normalize array to [0, 1] range.

        Args:
            arr: Input array

        Returns:
            Normalized array
        """
        min_val = np.min(arr)
        max_val = np.max(arr)

        if max_val == min_val:
            return np.zeros_like(arr)

        return (arr - min_val) / (max_val - min_val)

    def statistics(self, data: list[float]) -> dict[str, float]:
        """Calculate basic statistics for data.

        Args:
            data: Input data

        Returns:
            Dictionary with mean, std, min, max values

        Raises:
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Data cannot be empty")

        arr = np.array(data)

        return {
            "mean": float(np.mean(arr)),
            "std": float(np.std(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
        }

    def filter_outliers(
        self,
        data: list[float],
        threshold: float = 2.0,
    ) -> list[float]:
        """Filter outliers using z-score method.

        Args:
            data: Input data
            threshold: Z-score threshold (default: 2.0)

        Returns:
            Data with outliers removed. If there are fewer than three values
            or the data has zero variance, the original data is returned
            unchanged.

        Raises:
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Data cannot be empty")

        if len(data) < 3:
            return data

        arr = np.array(data)
        mean = np.mean(arr)
        std = np.std(arr)

        if std == 0:
            return data

        z_scores = np.abs((arr - mean) / std)
        filtered = arr[z_scores < threshold]

        return filtered.tolist()
