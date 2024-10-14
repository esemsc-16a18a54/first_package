import numpy as np


def element_multiplication(arr1, arr2):
    """
    Performs element-wise multiplication of two arrays.

    Args:
        arr1 (list): First array.
        arr2 (list): Second array.

    Returns:
        numpy.ndarray: Result of element-wise multiplication.

    Raises:
        ValueError: If the arrays have different dimensions.
    """

    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    if arr1.shape != arr2.shape:
        raise ValueError("Both arrays must have the same dimensions.")

    return np.multiply(arr1, arr2)


def element_division(arr1, arr2):
    """
    Performs element-wise division of two arrays.

    Args:
        arr1 (list): First array.
        arr2 (list): Second array.

    Returns:
        numpy.ndarray: Result of element-wise division.

    Raises:
        ValueError: If the arrays have different dimensions.
    """

    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    if arr1.shape != arr2.shape:
        raise ValueError("Both arrays must have the same dimensions.")

    return np.divide(arr1, arr2)
