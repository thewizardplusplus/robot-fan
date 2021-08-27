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
