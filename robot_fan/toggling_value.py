class TogglingValue:
    def __init__(self, reference_value):
        self.reference_value = reference_value
        self.previous_value = None

    def update(self, value):
        was_toggled = \
            value == self.reference_value and value != self.previous_value
        self.previous_value = value

        return was_toggled
