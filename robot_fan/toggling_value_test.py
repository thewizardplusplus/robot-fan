import unittest

from robot_fan.toggling_value import TogglingValue

class TestTogglingValue(unittest.TestCase):
    def test_init(self):
        toggling_value = TogglingValue(23)

        self.assertEqual(toggling_value.reference_value, 23)
        self.assertIsNone(toggling_value.previous_value)

    def test_update_with_not_reference_value(self):
        toggling_value = TogglingValue(23)
        was_toggled = toggling_value.update(42)

        self.assertEqual(toggling_value.previous_value, 42)
        self.assertFalse(was_toggled)

    def test_update_with_reference_value_and_toggling(self):
        toggling_value = TogglingValue(23)
        toggling_value.update(42)

        was_toggled = toggling_value.update(23)

        self.assertEqual(toggling_value.previous_value, 23)
        self.assertTrue(was_toggled)

    def test_update_with_reference_value_and_without_toggling(self):
        toggling_value = TogglingValue(23)
        toggling_value.update(23)

        was_toggled = toggling_value.update(23)

        self.assertEqual(toggling_value.previous_value, 23)
        self.assertFalse(was_toggled)
