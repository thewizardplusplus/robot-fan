import unittest

from robot_fan.interval import Interval
from robot_fan.running import run_control_loop

class TestRunControlLoop(unittest.TestCase):
    def test_without_activations(self):
        def _start_driving_motor(speed):
            raise RuntimeError("should not be called")

        stop_count = 0
        def _stop_driving_motor():
            nonlocal stop_count
            stop_count += 1

        iteration_count = 0
        def _should_continue():
            nonlocal iteration_count
            iteration_count += 1
            return iteration_count < 6

        run_control_loop(
            # parameters
            activation_color="color_1",
            control_angle_interval=Interval(5, 12),
            speed_modulus_interval=Interval(23, 42),
            rotate_direction=-1,

            # handlers
            get_control_color=lambda: "color_2",
            get_control_angle=lambda: 5,
            start_driving_motor=_start_driving_motor,
            stop_driving_motor=_stop_driving_motor,
            should_continue=_should_continue,
        )

        self.assertEqual(stop_count, 5)

    def test_with_activations(self):
        color = None
        def _get_control_color():
            nonlocal color
            color = "color_2" if color == "color_1" else "color_1"
            return color

        speeds = []
        def _start_driving_motor(speed):
            speeds.append(speed)

        stop_count = 0
        def _stop_driving_motor():
            nonlocal stop_count
            stop_count += 1

        iteration_count = 0
        def _should_continue():
            nonlocal iteration_count
            iteration_count += 1
            return iteration_count < 6

        run_control_loop(
            # parameters
            activation_color="color_1",
            control_angle_interval=Interval(5, 12),
            speed_modulus_interval=Interval(23, 42),
            rotate_direction=-1,

            # handlers
            get_control_color=_get_control_color,
            get_control_angle=lambda: 5,
            start_driving_motor=_start_driving_motor,
            stop_driving_motor=_stop_driving_motor,
            should_continue=_should_continue,
        )

        self.assertEqual(speeds, [-23, -23, -23])
        self.assertEqual(stop_count, 2)

    def test_with_speed_controlling(self):
        control_angle = 0
        def _get_control_angle():
            nonlocal control_angle
            control_angle += 10
            return control_angle

        speeds = []
        def _start_driving_motor(speed):
            speeds.append(speed)

        def _stop_driving_motor():
            raise RuntimeError("should not be called")

        iteration_count = 0
        def _should_continue():
            nonlocal iteration_count
            iteration_count += 1
            return iteration_count < 6

        run_control_loop(
            # parameters
            activation_color="color_1",
            control_angle_interval=Interval(0, 50),
            speed_modulus_interval=Interval(0, 500),
            rotate_direction=-1,

            # handlers
            get_control_color=lambda: "color_1",
            get_control_angle=_get_control_angle,
            start_driving_motor=_start_driving_motor,
            stop_driving_motor=_stop_driving_motor,
            should_continue=_should_continue,
        )

        self.assertEqual(speeds, [-100, -200, -300, -400, -500])
