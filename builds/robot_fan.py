ACTIVATION_COLOR = "red"
MINIMAL_CONTROL_ANGLE = 275
MAXIMAL_CONTROL_ANGLE = 220
MINIMAL_SPEED_MODULUS = 10
MAXIMAL_SPEED_MODULUS = 100
ROTATE_DIRECTION = -1
CONTROL_COLOR_SENSOR_PORT = "F"
SENSORY_MOTOR_PORT = "D"
DRIVING_MOTOR_PORT = "B"
class Interval:
	def __init__(self, minimum, maximum):
		self.minimum = minimum
		self.maximum = maximum
	def __len__(self):
		return abs(self.maximum - self.minimum)
	def get_proportion_by_value(self, value):
		minimum = min(self.minimum, self.maximum)
		maximum = max(self.minimum, self.maximum)
		if value < minimum or value > maximum:
			raise RuntimeError("the value is out of the interval")
		return abs(value - self.minimum) / len(self)
	def get_value_by_proportion(self, proportion):
		if proportion < 0 or proportion > 1:
			raise RuntimeError("the proportion is incorrect")
		return proportion * len(self) + self.minimum
class TogglingValue:
	def __init__(self, reference_value):
		self.reference_value = reference_value
		self.previous_value = None
	def update(self, value):
		was_toggled = \
			value == self.reference_value and value != self.previous_value
		self.previous_value = value
		return was_toggled
def run_control_loop(
	activation_color,
	control_angle_interval,
	speed_modulus_interval,
	rotate_direction,
	get_control_color,
	get_control_angle,
	start_driving_motor,
	stop_driving_motor,
	should_continue=lambda: True,
):
	is_active = False
	control_color = TogglingValue(activation_color)
	while should_continue():
		was_control_color_toggled = control_color.update(get_control_color())
		if was_control_color_toggled:
			is_active = not is_active
		if not is_active:
			stop_driving_motor()
			continue
		control_factor = \
			control_angle_interval.get_proportion_by_value(get_control_angle())
		speed_modulus = \
			speed_modulus_interval.get_value_by_proportion(control_factor)
		start_driving_motor(rotate_direction * speed_modulus)
import mindstorms
control_color_sensor = mindstorms.ColorSensor(CONTROL_COLOR_SENSOR_PORT)
sensory_motor = mindstorms.Motor(SENSORY_MOTOR_PORT)
driving_motor = mindstorms.Motor(DRIVING_MOTOR_PORT)
run_control_loop(
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
	get_control_color=lambda: control_color_sensor.get_color(),
	get_control_angle=lambda: sensory_motor.get_position(),
	start_driving_motor=lambda speed: driving_motor.start(int(speed)),
	stop_driving_motor=lambda: driving_motor.stop(),
)
