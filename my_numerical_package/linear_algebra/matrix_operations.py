import numpy as np


def addition(matrix1, matrix2):
    """
    Adds two matrices.

    Args:
        matrix1 (list): First matrix.
        matrix2 (list): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix addition.

    Raises:
        ValueError: If the matrices have different dimensions.
    """

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    if matrix1.shape != matrix2.shape:
        raise ValueError("Both matrices must have the same dimensions.")

    return np.add(matrix1, matrix2)


def subtraction(matrix1, matrix2):
    """
    Subtracts the second matrix from the first matrix.

    Args:
        matrix1 (list): First matrix.
        matrix2 (list): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix subtraction.

    Raises:
        ValueError: If the matrices have different dimensions.
    """

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    if matrix1.shape != matrix2.shape:
        raise ValueError("Both matrices must have the same dimensions.")

    return np.subtract(matrix1, matrix2)


def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
        matrix (list): Input matrix.

    Returns:
        float: Determinant of the matrix.

    Raises:
        ValueError: If the matrix is not square.
    """

    matrix = np.array(matrix)

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")

    return np.linalg.det(matrix)


def inverse(matrix):
    """
    Calculates the inverse of a matrix.

    Args:
        matrix (list): Input matrix.

    Returns:
        numpy.ndarray: Inverse of the matrix.

    Raises:
        ValueError: If the matrix is not square or is singular.
    """

    matrix = np.array(matrix)

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")

    if determinant(matrix) == 0:
        raise ValueError("Matrix must be non-singular.")

    return np.linalg.inv(matrix)
