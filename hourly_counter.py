#region imports
from AlgorithmImports import *
#endregion


class TimeFrameChecker:
    def __init__(self):
        self.counter = 0

    def increment_five_minute_bars(self):
        # Simulate the passage of time with a 5-minute delay
        self.counter += 1

    def is_one_hour_over(self, bar:str='5min') -> bool:
        
        _counter = 0
        if bar =='5Min':
            _counter = 12    
        elif bar == '10Min':
            _counter = 6
        elif bar == '15Min':
            _counter = 4
        
        while self.counter < _counter:  # 12 * 5 minutes = 1 hour
            self.increment_five_minute_bars()
            return False
        return self.counter >= _counter  # Return True if 1 hour is over, otherwise False
