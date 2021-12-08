class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    max_limit = 100

    def add(self, val):
        super().add(val)
        if self.value > self.max_limit:
            self.value = self.max_limit


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
