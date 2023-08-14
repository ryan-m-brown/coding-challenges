from typing import List


class AverageCalculator:

    def __init__(self, values: List[float]):
        self._values = values

    def add_value(self, value: float):
        self._values.append(value)

    def remove_value(self, value: float):
        self._values = self._values.remove(value)

    def compute_ave(self) -> float:
        if len(self._values) ==0:
            return 0

        sum = 0
        for value in self._values:
            sum = sum + value

        return sum / len(self._values)


if __name__ == '__main__':
    calc = AverageCalculator([1,2,3])
    print(calc.compute_ave())

    calc.add_value(10)
    print(calc.compute_ave())


