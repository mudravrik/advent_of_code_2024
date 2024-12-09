from pathlib import Path

import numpy as np
import pytest

from advent_of_code.day_1.solution import SolutionP1, SolutionP2


@pytest.fixture
def solver_p1() -> SolutionP1:
    return SolutionP1()


@pytest.fixture
def solver_p2() -> SolutionP2:
    return SolutionP2()


def test__read_input(solver_p1):
    test_file = Path("test_input.txt")
    read = solver_p1._read_input(test_file)
    assert read == {
        "lefts": [1, 6, 3, 5, 2, 4],
        "rights": [2, 1, 1, 3, 1, 6]}


def test__convert_to_sorted_array(solver_p1):
    read_data = [1, 6, 3]
    sorted_arrays = solver_p1._convert_to_sorted_array(read_data)
    assert (sorted_arrays == np.array([1, 3, 6])).all()


def test__get_total_distance_p1(solver_p1):
    data = {"lefts": np.array([1, 3, 6]), "rights": np.array([2, 4, 5])}
    result = solver_p1._get_total_distance(data)
    assert result == 3


def test_solve_p1(solver_p1):
    assert solver_p1.solve("test_input.txt") == 7


def test_solve_p2(solver_p2):
    assert solver_p2.solve("test_input.txt") == 14
