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


def compare_rows(i: int, j: int):
    # fetch data in constant time
    actual = actual_data[i][j]
    expected = expected_data[i][j]

    # balance floating point subtraction
    if actual > 0.1 + expected:
        raise Exception(f"actual {actual} failed for expected {expected}")


def run_asserts():
    # iterate only once over rows and cols
    for i in range(0, len(actual_data)):
        for j in range(0, len(actual_data[i])):
            compare_rows(i, j)


if __name__ == '__main__':
    run_asserts()
