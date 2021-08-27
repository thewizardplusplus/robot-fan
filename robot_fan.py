import mindstorms

MINIMAL_ANGLE = 275
MAXIMAL_ANGLE = 220

MINIMAL_SPEED = -10
MAXIMAL_SPEED = -100

sensory_motor = mindstorms.Motor("D")
driving_motor = mindstorms.Motor("B")

while True:
  angle = sensory_motor.get_position()
  factor = (angle - MINIMAL_ANGLE) / (MAXIMAL_ANGLE - MINIMAL_ANGLE)
  speed = (MAXIMAL_SPEED - MINIMAL_SPEED) * factor + MINIMAL_SPEED
  driving_motor.start(int(speed))
