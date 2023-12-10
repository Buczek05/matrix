import pytest

from matrix_class.exceptions import MatrixHaveNotInverseVersion, MatrixIsNotSquare
from matrix_class import Matrix


def test_get_transported() -> None:
    matrix = Matrix(3, 4)
    matrix[0, 0] = 1.0
    matrix[1, 1] = 2.0
    matrix[2, 2] = 3.0
    matrix[0, 1] = 4.0
    matrix_transported = matrix.get_transported()
    assert matrix_transported[0, 0] == 1.0
    assert matrix_transported[1, 1] == 2.0
    assert matrix_transported[2, 2] == 3.0
    assert matrix_transported[1, 0] == 4.0
    assert matrix_transported.rows == 4
    assert matrix_transported.columns == 3


def test_get_complement() -> None:
    matrix = Matrix(3, 3)
    matrix[0, 0] = 1.0
    matrix[0, 1] = 2.0
    matrix[0, 2] = 3.0
    matrix[1, 0] = 2.0
    matrix[1, 1] = 4.0
    matrix[1, 2] = 5.0
    matrix[2, 0] = 3.0
    matrix[2, 1] = 5.0
    matrix[2, 2] = 6.0
    matrix_complement = matrix.get_complement()
    assert matrix_complement[0, 0] == -1.0
    assert matrix_complement[0, 1] == 3.0
    assert matrix_complement[0, 2] == -2.0
    assert matrix_complement[1, 0] == 3.0
    assert matrix_complement[1, 1] == -3.0
    assert matrix_complement[1, 2] == 1.0
    assert matrix_complement[2, 0] == -2.0
    assert matrix_complement[2, 1] == 1.0
    assert matrix_complement[2, 2] == -0.0


def test_get_complement_not_square() -> None:
    matrix = Matrix(2, 4)
    with pytest.raises(MatrixIsNotSquare):
        matrix.get_complement()


def test_get_inverse_det_0() -> None:
    matrix = Matrix(3, 3)
    with pytest.raises(MatrixHaveNotInverseVersion):
        assert matrix.get_inverse()

def test_get_inverse() -> None:
    matrix = Matrix(3, 3)
    matrix[0, 0] = 1.0
    matrix[0, 1] = 2.0
    matrix[0, 2] = 3.0
    matrix[1, 0] = 2.0
    matrix[1, 1] = 4.0
    matrix[1, 2] = 5.0
    matrix[2, 0] = 3.0
    matrix[2, 1] = 5.0
    matrix[2, 2] = 6.0
    inverse_matrix = matrix.get_inverse()
    assert inverse_matrix[0, 0] == 1.0
    assert inverse_matrix[0, 1] == -3.0
    assert inverse_matrix[0, 2] == 2.0
    assert inverse_matrix[1, 0] == -3.0
    assert inverse_matrix[1, 1] == 3.0
    assert inverse_matrix[1, 2] == -1.0
    assert inverse_matrix[2, 0] == 2.0
    assert inverse_matrix[2, 1] == -1.0
    assert inverse_matrix[2, 2] == 0.0
