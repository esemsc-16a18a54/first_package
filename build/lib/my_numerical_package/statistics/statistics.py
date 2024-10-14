import numpy as np


def mean(arr):
    """
    Calculates the mean of an array.

    Args:
        arr (list): Input array.

    Returns:
        float: Mean of the array.
    """

    arr = np.array(arr)

    if arr.size == 0:
        raise ValueError("Array cannot be empty.")

    return np.mean(arr)


def median(arr):
    """
    Calculates the median of an array.

    Args:
        arr (list): Input array.

    Returns:
        float: Median of the array.

    Raises:
        ValueError: If the array is empty.
    """

    arr = np.array(arr)

    if arr.size == 0:
        raise ValueError("Array cannot be empty.")

    return np.median(arr)


def standard_deviation(arr):
    """
    Calculates the standard deviation of an array.

    Args:
        arr (list): Input array.

    Returns:
        float: Standard deviation of the array.

    Raises:
        ValueError: If the array is empty.
    """

    arr = np.array(arr)

    if arr.size == 0:
        raise ValueError("Array cannot be empty.")

    return np.std(arr)
