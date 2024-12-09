from abc import ABC, abstractmethod
from collections import Counter
from pathlib import Path

import numpy as np


class Solution(ABC):
    @abstractmethod
    def solve(self, input_path: str) -> int:
        pass

    @staticmethod
    def _read_input(input_path: Path) -> dict[str, list[int]]:
        lefts = []
        rights = []
        with open(input_path, "rt") as f:
            for line in f.readlines():
                elems = [int(x) for x in line.split("   ")]
                lefts.append(elems[0])
                rights.append(elems[1])

        return {"lefts": lefts, "rights": rights}


class SolutionP1(Solution):
    def solve(self, input_path: str) -> int:
        input_path = Path(input_path)
        data = self._read_input(input_path)
        sorted_data = {k: self._convert_to_sorted_array(v) for k, v in data.items()}
        return self._get_total_distance(sorted_data)

    @staticmethod
    def _convert_to_sorted_array(input_data: list[int]) -> np.typing.NDArray:
        result = np.array(input_data)
        result.sort()
        return result

    @staticmethod
    def _get_total_distance(input_data: dict[str, np.typing.ArrayLike]) -> int:
        result = input_data["lefts"] - input_data["rights"]
        result = np.absolute(result)
        return result.sum()


class SolutionP2(Solution):
    def solve(self, input_path: str) -> int:
        input_path = Path(input_path).absolute()
        data = self._read_input(input_path)
        right_counted = self._get_counts(data["rights"])
        return sum([k * right_counted[k] for k in data["lefts"]])

    @staticmethod
    def _get_counts(input_data: list[int]) -> Counter:
        return Counter(input_data)


if __name__ == "__main__":
    input_path = "../../inputs/day_1.txt"
    solver_p1 = SolutionP1()
    print(solver_p1.solve(input_path))
    solver_p2 = SolutionP2()
    print(solver_p2.solve(input_path))
