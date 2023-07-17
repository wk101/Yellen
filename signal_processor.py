#region imports
from AlgorithmImports import *
#endregion

class SignalProcessor:
    def __init__(self):
        pass
    
    def process_signal(self, trade_number: int, price_movement: float) -> bool:
        # Define the trading strategy as a dictionary
        dict_price_movement = {
            2: 0.005,
            3: 0.004,
            4: 0.0035,
            5: 0.003,
            6: 0.003,
            7: 0.0025,
            8: 0.0025,
            9: 0.002,
            10: 0.002,
            11: 0.0018,
            12: 0.0018,
            13: 0.0015,
            14: 0.0015,
            15: 0.0012,
            16: 0.0012,
            17: 0.001,
            18: 0.001,
            19: 0.0008,
            20: 0.0008,
            21: 0.0005,
            22: 0.0005,
            23: 0.0003,
            24: 0.0003,
            25: 0.0003,
            26: 0.0003,
            27: 0.0003,
            28: 0.0003,
            29: 0.0003,
            30: 0.0003
        }

        
        if price_movement > dict_price_movement[trade_number]:
            return True
        else:
            return False
