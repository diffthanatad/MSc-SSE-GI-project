import time
import pytest
from triangle import TriangleType, classify_triangle


def check_classification(triangles, expected_result):
    for triangle in triangles:
        assert classify_triangle(*triangle) == expected_result


def test_invalid_triangles():
    triangles = [(1, 2, 9), (1, 9, 2), (2, 1, 9), (2, 9, 1), (9, 1, 2),
                 (9, 2, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]
    check_classification(triangles, TriangleType.INVALID)


def test_equalateral_triangles():
    triangles = [(1, 1, 1), (100, 100, 100), (99, 99, 99)]
    check_classification(triangles, TriangleType.EQUILATERAL)


def test_isosceles_triangles():
    triangles = [(100, 90, 90), (90, 100, 90), (90, 90, 100), (2, 2, 3)]

    check_classification(triangles, TriangleType.ISOSCELES)


def test_scalene_triangles():
    triangles = [(5, 4, 3), (5, 3, 4), (4, 5, 3), (4, 3, 5), (3, 5, 4)]
    check_classification(triangles, TriangleType.SCALENE)
