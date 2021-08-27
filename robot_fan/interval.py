class Interval:
    def __init__(self, minimum, maximum):
        if maximum < minimum:
            raise RuntimeError("the maximum is greater than the minimum")

        self.minimum = minimum
        self.maximum = maximum

    def __len__(self):
        return self.maximum - self.minimum
