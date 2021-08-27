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
