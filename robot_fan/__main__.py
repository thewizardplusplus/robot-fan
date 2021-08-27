import mindstorms

from robot_fan.interval import Interval
from robot_fan.toggling_value import TogglingValue

ACTIVATION_COLOR = "red"
CONTROL_ANGLE_INTERVAL = Interval(275, 220)
SPEED_MODULUS_INTERVAL = Interval(10, 100)
ROTATE_DIRECTION = -1

control_color_sensor = mindstorms.ColorSensor("F")
sensory_motor = mindstorms.Motor("D")
driving_motor = mindstorms.Motor("B")

is_active = False
control_color = TogglingValue(ACTIVATION_COLOR)
while True:
  was_control_color_toggled = \
    control_color.update(control_color_sensor.get_color())
  if was_control_color_toggled:
    is_active = not is_active

  if not is_active:
    driving_motor.stop()
    continue

  control_angle = sensory_motor.get_position()
  control_factor = CONTROL_ANGLE_INTERVAL.get_proportion_by_value(control_angle)
  speed_modulus = SPEED_MODULUS_INTERVAL.get_value_by_proportion(control_factor)
  driving_motor.start(int(ROTATE_DIRECTION * speed_modulus))
