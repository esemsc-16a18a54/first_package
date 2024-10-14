# my_numerical_package

`my_numerical_package` is a Python package that provides various numerical operations, including matrix operations, array operations, and statistical calculations. This package leverages the power of NumPy to perform efficient and reliable computations.

## Installation

To install `my_numerical_package`, clone the repository and install the dependencies:

```bash
git clone https://github.com/esemsc-16a18a54/first_package.git
cd my_numerical_package
pip install .
```

## Usage

### Matrix Operations

The `matrix_operations` module provides functions to perform various matrix operations such as addition, subtraction, determinant calculation, and finding the inverse of a matrix.

```python
from my_numerical_package.matrix_operations import addition, subtraction, determinant, inverse

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Matrix Addition
result_add = addition(matrix1, matrix2)

# Matrix Subtraction
result_sub = subtraction(matrix1, matrix2)

# Determinant
det = determinant(matrix1)

# Inverse
inv = inverse(matrix1)
```

### Array Operations

The `array_operations` module provides functions to perform element-wise operations on arrays, such as multiplication and division.

```python
from my_numerical_package.array_operations import element_multiplication, element_division

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# Element-wise Multiplication
result_mul = element_multiplication(arr1, arr2)

# Element-wise Division
result_div = element_division(arr1, arr2)
```

### Statistical Calculations

The `statistics` module provides functions to calculate statistical measures such as mean, median, and standard deviation.

```python
from my_numerical_package.statistics import mean, median, standard_deviation

arr = [1, 2, 3, 4, 5]

# Mean
mean_value = mean(arr)

# Median
median_value = median(arr)

# Standard Deviation
std_dev = standard_deviation(arr)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.