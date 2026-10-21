import unittest

from student import calculate_average, get_result


class TestCalculateAverage(unittest.TestCase):
    def test_multiple_marks(self):
        self.assertAlmostEqual(calculate_average([75, 80, 65]), 220 / 3)

    def test_single_mark(self):
        self.assertEqual(calculate_average([50]), 50)

    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0.0)


class TestGetResult(unittest.TestCase):
    def test_above_threshold_passes(self):
        self.assertEqual(get_result(75), "Pass")

    def test_exactly_40_passes(self):
        self.assertEqual(get_result(40), "Pass")

    def test_below_threshold_fails(self):
        self.assertEqual(get_result(39.99), "Fail")

    def test_zero_fails(self):
        self.assertEqual(get_result(0), "Fail")


if __name__ == "__main__":
    unittest.main()
