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


def test_mul_by_matrix_2() -> None:
    matrix_1 = Matrix(2, 3)
    matrix_2 = Matrix(3, 5)
    matrix_1[0, 0] = 1
    matrix_1[0, 1] = 2
    matrix_1[0, 2] = 3
    matrix_1[1, 0] = 4
    matrix_1[1, 1] = 5
    matrix_1[1, 2] = 6
    matrix_2[0, 0] = 7
    matrix_2[0, 1] = 8
    matrix_2[0, 2] = 9
    matrix_2[0, 3] = 10
    matrix_2[0, 4] = 11
    matrix_2[1, 0] = 12
    matrix_2[1, 1] = 13
    matrix_2[1, 2] = 14
    matrix_2[1, 3] = 15
    matrix_2[1, 4] = 16
    matrix_2[2, 0] = 17
    matrix_2[2, 1] = 18
    matrix_2[2, 2] = 19
    matrix_2[2, 3] = 20
    matrix_2[2, 4] = 21
    print(matrix_1)
    print(matrix_2)
    matrix_3 = matrix_1 * matrix_2
    assert matrix_3[0, 0] == 82
    assert matrix_3[0, 1] == 88
    assert matrix_3[0, 2] == 94
    assert matrix_3[0, 3] == 100
    assert matrix_3[0, 4] == 106
    assert matrix_3[1, 0] == 190
    assert matrix_3[1, 1] == 205
    assert matrix_3[1, 2] == 220
    assert matrix_3[1, 3] == 235
    assert matrix_3[1, 4] == 250
    assert matrix_3.rows == 2
    assert matrix_3.columns == 5


