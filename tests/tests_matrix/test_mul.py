import pytest

from matrix_class.exceptions import MatrixSizesAreWrongForMul
from matrix_class import Matrix


def test_mul_by_number() -> None:
    matrix = Matrix(2, 2)
    matrix[0, 0] = 1.0
    matrix[0, 1] = 2.0
    matrix[1, 0] = 3.0
    matrix[1, 1] = 4.0
    matrix_2 = matrix * 2
    assert matrix_2[0, 0] == 2.0
    assert matrix_2[0, 1] == 4.0
    assert matrix_2[1, 0] == 6.0
    assert matrix_2[1, 1] == 8.0


def test_mul_by_matrix_wrong_sizes() -> None:
    matrix_1 = Matrix(2, 3)
    matrix_2 = Matrix(2, 2)
    with pytest.raises(MatrixSizesAreWrongForMul):
        assert matrix_1 * matrix_2
    assert matrix_2 * matrix_1


def test_mul_by_matrix_1() -> None:
    matrix_1 = Matrix(2, 2)
    matrix_2 = Matrix(2, 2)
    matrix_1[0, 0] = 1.0
    matrix_1[0, 1] = 2.0
    matrix_1[1, 0] = 3.0
    matrix_1[1, 1] = 4.0
    matrix_2[0, 0] = 5.0
    matrix_2[0, 1] = 6.0
    matrix_2[1, 0] = 7.0
    matrix_2[1, 1] = 8.0
    matrix_3 = matrix_1 * matrix_2
    assert matrix_3[0, 0] == 19.0
    assert matrix_3[0, 1] == 22.0
    assert matrix_3[1, 0] == 43.0
    assert matrix_3[1, 1] == 50.0

