import unittest

from robot_fan.toggling_value import TogglingValue

class TestTogglingValue(unittest.TestCase):
    def test_init(self):
        toggling_value = TogglingValue(23)

        self.assertEqual(toggling_value.reference_value, 23)
        self.assertIsNone(toggling_value.previous_value)
