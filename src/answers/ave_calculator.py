from typing import List


class AverageCalculator:

    def __init__(self, values: List[float]):

        # iterate over the list only once
        sum = 0
        for value in values:
            sum = sum + value

        self._sum = sum
        self._count = len(values)

    def add_value(self, value: float):
        self._sum = self._sum + value
        self._count = self._count + 1

    def remove_value(self, value: float):
        # handle possible errors gracefully
        if self._count == 0:
            raise Exception("Cannot remove value from empty list")

        self._sum = self._sum - value
        self._count = self._count - 1

    def compute_ave(self) -> float:
        # handle possible errors gracefully
        if self._count == 0:
            raise Exception("Cannot compute ave from empty list")

        return self._sum / self._count


if __name__ == '__main__':
    pass
