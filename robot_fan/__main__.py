import mindstorms

from robot_fan.configuration import *
from robot_fan.interval import Interval
from robot_fan.running import run_control_loop

control_color_sensor = mindstorms.ColorSensor(CONTROL_COLOR_SENSOR_PORT)
sensory_motor = mindstorms.Motor(SENSORY_MOTOR_PORT)
driving_motor = mindstorms.Motor(DRIVING_MOTOR_PORT)
run_control_loop(
    # parameters
    activation_color=ACTIVATION_COLOR,
    control_angle_interval=Interval(
        MINIMAL_CONTROL_ANGLE,
        MAXIMAL_CONTROL_ANGLE,
    ),
    speed_modulus_interval=Interval(
        MINIMAL_SPEED_MODULUS,
        MAXIMAL_SPEED_MODULUS,
    ),
    rotate_direction=ROTATE_DIRECTION,

    # handlers
    get_control_color=lambda: control_color_sensor.get_color(),
    get_control_angle=lambda: sensory_motor.get_position(),
    start_driving_motor=lambda speed: driving_motor.start(int(speed)),
    stop_driving_motor=lambda: driving_motor.stop(),
)
