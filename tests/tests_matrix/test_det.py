import pytest

from matrix_class.exceptions import MatrixIsNotSquare
from matrix_class import Matrix


def test_det_not_square():
    matrix = Matrix(3, 4)
    matrix[0, 0] = 1.0
    matrix[1, 1] = 2.0
    matrix[2, 2] = 3.0
    matrix[0, 1] = 4.0
    with pytest.raises(MatrixIsNotSquare):
        assert matrix.det


def test_det_1_1():
    matrix = Matrix(1, 1)
    matrix[0, 0] = 55.0
    assert matrix.det == 55.0


def test_det_2_1():
    matrix = Matrix(2, 2)
    matrix[0, 0] = 1.0
    matrix[1, 1] = 1.0
    matrix[0, 1] = 1.0
    matrix[1, 0] = 1.0
    assert matrix.det == 0.0


def test_det_2_2():
    matrix = Matrix(2, 2)
    matrix[0, 0] = 1.0
    matrix[1, 1] = 1.0
    assert matrix.det == 1.0


def test_det_2_3():
    matrix = Matrix(2, 2)
    matrix[0, 0] = 1.0
    matrix[1, 1] = 2.0
    matrix[0, 1] = 3.0
    matrix[1, 0] = 4.0
    assert matrix.det == -10.0


def test_det_3_1():
    matrix = Matrix(3, 3)
    matrix[0, 0] = 1.0
    matrix[1, 1] = 1.0
    matrix[2, 2] = 1.0
    matrix[0, 1] = 1.0
    matrix[1, 2] = 1.0
    matrix[2, 0] = 1.0
    matrix[0, 2] = 1.0
    matrix[1, 0] = 1.0
    matrix[2, 1] = 1.0
    assert matrix.det == 0.0


def test_det_3_2():
    matrix = Matrix(3, 3)
    matrix[0, 0] = 1.0
    matrix[0, 1] = 2.0
    matrix[0, 2] = 3.0
    matrix[1, 0] = 4.0
    matrix[1, 1] = 5.0
    matrix[1, 2] = 6.0
    matrix[2, 0] = 7.0
    matrix[2, 1] = 8.0
    matrix[2, 2] = 9.0
    assert matrix.det == 0.0


def test_det_3_3():
    matrix = Matrix(3, 3)
    matrix[0, 0] = 1.0
    matrix[0, 1] = 2.0
    matrix[0, 2] = 3.0
    matrix[1, 0] = 4.0
    matrix[1, 1] = 55.0
    matrix[1, 2] = 6.0
    matrix[2, 0] = 7.0
    matrix[2, 1] = 8.0
    matrix[2, 2] = 9.0
    assert matrix.det == -600.0


def test_det_4_1():
    matrix = Matrix(4, 4)
    for i in range(4):
        matrix[i, i] = 1.0
    assert matrix.det == 1.0


def test_det_4_2():
    matrix = Matrix(4, 4)
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for i in range(4):
        for j in range(4):
            matrix[i, j] = values[4 * i + j]
    assert matrix.det == 0.0


def test_det_4_3():
    matrix = Matrix(4, 4)
    for i in range(4):
        for j in range(4):
            matrix[i, j] = (i + 1) * (j + 1)
    assert matrix.det == 0.0


def test_det_5_1():
    matrix = Matrix(5, 5)
    for i in range(5):
        matrix[i, i] = 1.0
    assert matrix.det == 1.0


def test_det_5_2():
    matrix = Matrix(5, 5)
    for i in range(5):
        for j in range(5):
            matrix[i, j] = (i + 1) * (j + 1)
    assert matrix.det == 0.0


def test_det_5_3():
    matrix = Matrix(5, 5)
    for i in range(5):
        for j in range(5):
            matrix[i, j] = 5 * i + j + 1
    assert matrix.det == 0.0


def test_det_6_1():
    matrix = Matrix(6, 6)
    for i in range(6):
        matrix[i, i] = 1.0
    assert matrix.det == 1.0


def test_det_6_2():
    matrix = Matrix(6, 6)
    for i in range(6):
        for j in range(6):
            matrix[i, j] = (i + 1) * (j + 2)
    assert matrix.det == 0.0


def test_det_6_3():
    matrix = Matrix(6, 6)
    for i in range(6):
        for j in range(6):
            matrix[i, j] = (i + j) * (i + j + 1)
    assert matrix.det == 0.0


def test_det_7_1():
    matrix = Matrix(7, 7)
    for i in range(7):
        matrix[i, i] = 1.0
    assert matrix.det == 1.0


def test_det_7_2():
    matrix = Matrix(7, 7)
    for i in range(7):
        for j in range(7):
            matrix[i, j] = (i + 1) * (j + 3)
    assert matrix.det == 0.0


def test_det_7_3():
    matrix = Matrix(7, 7)
    for i in range(7):
        for j in range(7):
            matrix[i, j] = (i + 2) * (j + 2)
    assert matrix.det == 0.0
