from median import median_calc


def test_median_calc():
    median_calc([1, 2, 3, 4, 5]) == 3
    median_calc([3, 1, 2, 5, 3]) == 3
    median_calc([1, 300, 2, 200, 1]) == 2
    median_calc([3, 6, 20, 99, 10, 15]) == 12.5
