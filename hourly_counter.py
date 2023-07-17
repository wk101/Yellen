
class TimeFrameChecker:
    def __init__(self):
        self.counter = 0

    def increment_five_minute_bars(self):
        # Simulate the passage of time with a 5-minute delay
        self.counter += 1

    def is_one_hour_over(self) -> bool:
        while self.counter < 12:  # 12 * 5 minutes = 1 hour
            self.increment_five_minute_bars()
            return False
        return self.counter >= 12  # Return True if 1 hour is over, otherwise False
