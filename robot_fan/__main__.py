import mindstorms

from robot_fan.interval import Interval

ACTIVATION_COLOR = "red"
CONTROL_ANGLE_INTERVAL = Interval(275, 220)
SPEED_MODULUS_INTERVAL = Interval(10, 100)
ROTATE_DIRECTION = -1

control_color_sensor = mindstorms.ColorSensor("F")
sensory_motor = mindstorms.Motor("D")
driving_motor = mindstorms.Motor("B")

is_active = False
previous_color = None
while True:
  current_color = control_color_sensor.get_color()
  if current_color == ACTIVATION_COLOR and current_color != previous_color:
    is_active = not is_active
  previous_color = current_color

  if not is_active:
    driving_motor.stop()
    continue

  control_angle = sensory_motor.get_position()
  control_factor = CONTROL_ANGLE_INTERVAL.get_proportion_by_value(control_angle)
  speed_modulus = SPEED_MODULUS_INTERVAL.get_value_by_proportion(control_factor)
  driving_motor.start(int(ROTATE_DIRECTION * speed_modulus))
