import pytest

from matrix_class.exceptions import RowOutOfBoundsException, ColumnOutOfBoundsException, MatrixSizesAreDifferent
from matrix_class import Matrix


@pytest.fixture
def matrix() -> Matrix:
    matrix = Matrix(3, 4)
    matrix.set_item(0, 0, 1.0)
    matrix.set_item(1, 1, 2.5)
    matrix.set_item(2, 2, 13.0)
    return matrix


def test_columns(matrix: Matrix):
    assert matrix.columns == 4


def test_rows(matrix: Matrix):
    assert matrix.rows == 3


def test_get_item(matrix: Matrix):
    assert matrix[0, 0] == 1.0


def test_get_item_out_of_bounds(matrix: Matrix):
    with pytest.raises(RowOutOfBoundsException):
        assert matrix[3, 0]
    with pytest.raises(ColumnOutOfBoundsException):
        assert matrix[0, 4]


def test_set_item(matrix: Matrix):
    matrix[0, 0] = 2.0
    assert matrix[0, 0] == 2.0


def test_set_item_out_of_bounds(matrix: Matrix):
    with pytest.raises(RowOutOfBoundsException):
        matrix[3, 0] = 2.0
    with pytest.raises(ColumnOutOfBoundsException):
        matrix[0, 4] = 2.0


def test_print_matrix(matrix: Matrix):
    assert str(matrix) == "    1    0    0    0\n" \
                          "    0  2.5    0    0\n" \
                          "    0    0   13    0\n"


def test_add_matrix() -> None:
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
    matrix_3 = matrix_1 + matrix_2
    assert matrix_3[0, 0] == 6.0
    assert matrix_3[0, 1] == 8.0
    assert matrix_3[1, 0] == 10.0
    assert matrix_3[1, 1] == 12.0


def test_add_matrix_different_sizes() -> None:
    matrix_1 = Matrix(2, 2)
    matrix_2 = Matrix(3, 3)
    with pytest.raises(MatrixSizesAreDifferent):
        assert matrix_1 + matrix_2


def test_sub_matrix() -> None:
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
    matrix_3 = matrix_1 - matrix_2
    assert matrix_3[0, 0] == -4.0
    assert matrix_3[0, 1] == -4.0
    assert matrix_3[1, 0] == -4.0
    assert matrix_3[1, 1] == -4.0


def test_sub_matrix_different_sizes() -> None:
    matrix_1 = Matrix(2, 2)
    matrix_2 = Matrix(3, 3)
    with pytest.raises(MatrixSizesAreDifferent):
        assert matrix_1 - matrix_2


def test_equal() -> None:
    matrix_1 = Matrix(2, 2)
    matrix_2 = Matrix(2, 2)
    matrix_1[0, 0] = 1.0
    matrix_1[0, 1] = 2.0
    matrix_1[1, 0] = 3.0
    matrix_1[1, 1] = 4.0
    matrix_2[0, 0] = 1.0
    matrix_2[0, 1] = 2.0
    matrix_2[1, 0] = 3.0
    matrix_2[1, 1] = 4.0
    assert matrix_1 == matrix_2

    matrix_1 = Matrix(2, 2)
    matrix_2 = Matrix(2, 3)
    assert matrix_1 != matrix_2

    matrix_1 = Matrix(2, 2)
    matrix_2 = Matrix(2, 2)
    matrix_1[0, 0] = 1.0
    matrix_1[0, 1] = 2.0
    matrix_1[1, 0] = 3.0
    assert matrix_1 != matrix_2
