import math

import mindstorms

ACTIVATION_COLOR = "red"

MINIMAL_ANGLE = 275
MAXIMAL_ANGLE = 220

MINIMAL_SPEED = 10
MAXIMAL_SPEED = 100
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

  angle = sensory_motor.get_position()
  factor = math.fabs((angle - MINIMAL_ANGLE) / (MAXIMAL_ANGLE - MINIMAL_ANGLE))
  speed = (MAXIMAL_SPEED - MINIMAL_SPEED) * factor + MINIMAL_SPEED
  driving_motor.start(int(ROTATE_DIRECTION * speed))
