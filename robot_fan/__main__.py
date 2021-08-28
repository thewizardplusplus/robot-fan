import mindstorms

from robot_fan.interval import Interval
from robot_fan.running import run_control_loop

ACTIVATION_COLOR = "red"
CONTROL_ANGLE_INTERVAL = Interval(275, 220)
SPEED_MODULUS_INTERVAL = Interval(10, 100)
ROTATE_DIRECTION = -1

control_color_sensor = mindstorms.ColorSensor("F")
sensory_motor = mindstorms.Motor("D")
driving_motor = mindstorms.Motor("B")
run_control_loop(
    # parameters
    activation_color=ACTIVATION_COLOR,
    control_angle_interval=CONTROL_ANGLE_INTERVAL,
    speed_modulus_interval=SPEED_MODULUS_INTERVAL,
    rotate_direction=ROTATE_DIRECTION,

    # handlers
    get_control_color=lambda: control_color_sensor.get_color(),
    get_control_angle=lambda: sensory_motor.get_position(),
    start_driving_motor=lambda speed: driving_motor.start(int(speed)),
    stop_driving_motor=lambda: driving_motor.stop(),
)
