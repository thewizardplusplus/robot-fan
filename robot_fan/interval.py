class Interval:
    def __init__(self, minimum, maximum):
        if maximum < minimum:
            raise RuntimeError("the maximum is greater than the minimum")

        self.minimum = minimum
        self.maximum = maximum

    def __len__(self):
        return self.maximum - self.minimum

    def get_proportion_by_value(self, value):
        if value < self.minimum or value > self.maximum:
            raise RuntimeError("the value is out of the interval")

        return (value - self.minimum) / len(self)
