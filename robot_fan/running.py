from robot_fan.toggling_value import TogglingValue

def run_control_loop(
    # parameters
    activation_color,
    control_angle_interval,
    speed_modulus_interval,
    rotate_direction,

    # handlers
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
