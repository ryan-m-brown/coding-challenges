from typing import List

actual_data = [
    [1.5, 2.71, 3.11, 4.2, 5.1, 6.8, 7.3, 8.92, 0.0, 10.5],
    [1.5, 2.75, 3.14, 4.2, 1.01, 6.81, 7.3, 8.99, 9.1, 1.5],
    [11.57, 2.7, 3.15, 4.2, 5.0, 6.8, 7.33, 8.9, 9.11, 0.5]
]

expected_data = [
    [1.5, 2.7, 3.14, 4.2, 5.0, 6.8, 7.3, 8.9, 0.1, 10.5],
    [1.5, 2.7, 3.14, 4.2, 1.02, 6.8, 7.3, 8.9, 9.1, 1.52],
    [11.5, 2.7, 3.14, 4.2, 5.0, 6.8, 7.3, 8.9, 9.1, 0.52]
]


def compare_rows(actual_row: List[float], expected_row: List[float]):
    for actual in actual_row:
        for expected in expected_row:
            # assume expected and actual are positive
            # assume rules are actual-expected
            if actual - expected > 0.1:
                raise Exception(f"actual {actual} failed for expected {expected}")


def run_asserts():
    # assume actual and expected have the same dims
    for actual_row in actual_data:
        for expected_row in expected_data:
            compare_rows(actual_row, expected_row)


if __name__ == '__main__':
    pass
