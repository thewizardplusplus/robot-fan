import unittest

from robot_fan.interval import Interval

class TestInterval(unittest.TestCase):
    def test_init_success_with_different_values(self):
        interval = Interval(23, 42)

        self.assertEqual(interval.minimum, 23)
        self.assertEqual(interval.maximum, 42)

    def test_init_success_with_same_values(self):
        interval = Interval(23, 23)

        self.assertEqual(interval.minimum, 23)
        self.assertEqual(interval.maximum, 23)

    def test_init_error(self):
        error_message = "the maximum is greater than the minimum"
        with self.assertRaisesRegex(RuntimeError, error_message):
            Interval(42, 23)

    def test_len_with_different_values(self):
        interval = Interval(23, 42)
        interval_length = len(interval)

        self.assertEqual(interval_length, 19)

    def test_len_with_same_values(self):
        interval = Interval(23, 23)
        interval_length = len(interval)

        self.assertEqual(interval_length, 0)

    def test_get_proportion_by_value_success(self):
        interval = Interval(23, 42)
        proportion = interval.get_proportion_by_value(37.25)

        self.assertAlmostEqual(proportion, 0.75)

    def test_get_proportion_by_value_error_with_too_small_value(self):
        error_message = "the value is out of the interval"
        with self.assertRaisesRegex(RuntimeError, error_message):
            interval = Interval(23, 42)
            interval.get_proportion_by_value(-100)

    def test_get_proportion_by_value_error_with_too_great_value(self):
        error_message = "the value is out of the interval"
        with self.assertRaisesRegex(RuntimeError, error_message):
            interval = Interval(23, 42)
            interval.get_proportion_by_value(100)

    def test_get_value_by_proportion_success(self):
        interval = Interval(23, 42)
        value = interval.get_value_by_proportion(0.75)

        self.assertAlmostEqual(value, 37.25)

    def test_get_value_by_proportion_error_with_too_small_proportion(self):
        error_message = "the proportion is incorrect"
        with self.assertRaisesRegex(RuntimeError, error_message):
            interval = Interval(23, 42)
            interval.get_value_by_proportion(-2)

    def test_get_value_by_proportion_error_with_too_great_proportion(self):
        error_message = "the proportion is incorrect"
        with self.assertRaisesRegex(RuntimeError, error_message):
            interval = Interval(23, 42)
            interval.get_value_by_proportion(2)
