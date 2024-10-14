import unittest
import numpy as np
import my_numerical_package as mnp


class TestArrayOperations(unittest.TestCase):
    def test_element_multiplication(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        expected_result = np.array([4, 10, 18])
        self.assertTrue(
            np.array_equal(mnp.element_multiplication(arr1, arr2), expected_result)
        )

    def test_element_division(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        expected_result = np.array([0.25, 0.4, 0.5])
        self.assertTrue(
            np.array_equal(mnp.element_division(arr1, arr2), expected_result)
        )

    def test_mean(self):
        arr = [1, 2, 3, 4, 5]
        expected_result = 3
        self.assertEqual(mnp.mean(arr), expected_result)

    def test_median(self):
        arr = [1, 2, 2, 4, 5]
        expected_result = 2
        self.assertEqual(mnp.median(arr), expected_result)

    def test_standard_deviation(self):
        arr = [1, 2, 3, 4, 5]
        expected_result = 1.4142135623730951
        self.assertEqual(mnp.standard_deviation(arr), expected_result)


class TestMatrixOperations(unittest.TestCase):
    def test_addition(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = np.array([[6, 8], [10, 12]])
        self.assertTrue(np.array_equal(
            mnp.addition(matrix1, matrix2), expected_result
        ))

    def test_subtraction(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = np.array([[-4, -4], [-4, -4]])
        self.assertTrue(
            np.array_equal(mnp.subtraction(matrix1, matrix2), expected_result)
        )

    def test_determinant(self):
        matrix = [[1, 2], [3, 4]]
        expected_result = -2
        self.assertAlmostEqual(
            mnp.determinant(matrix), expected_result, places=7
        )

    def test_inverse(self):
        matrix = [[1, 2], [3, 4]]
        expected_result = np.array([[-2., 1.], [1.5, -0.5]])
        print(mnp.inverse(matrix), type(mnp.inverse(matrix)))
        print(expected_result, type(expected_result))
        self.assertTrue(np.array_equal(mnp.inverse(matrix), expected_result))
