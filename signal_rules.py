#region Imports
from AlgorithmImports import *
#endregion

class SignalRules:
    def __init__(self):
        self.adx_green_over_red = False
        self.adx_red_over_green = False
        self.rsi_below_30 = False
        self.rsi_above_30 = False
        self.rsi_above_70 = False
        self.rsi_below_70 = False

    def check_long_signal(self, adx_green: float, adx_red: float, rsi: float) -> bool:
        """
        Check if the provided values satisfy the long signal rules.

        Args:
            adx_green (float): The ADX green line value.
            adx_red (float): The ADX red line value.
            rsi (float): The RSI value.

        Returns:
            bool: True if the signal rules are satisfied for a long position, False otherwise.
        """
        is_result_long = False
        self.adx_green_over_red = adx_green > adx_red
        if self.rsi_below_30: 
            self.rsi_above_30 = rsi > 30
            is_result_long = self.adx_green_over_red and self.rsi_below_30 and self.rsi_above_30 
        
        self.rsi_below_30 = rsi < 30
        
        if is_result_long:
            self.reset()
        
        return is_result_long

    def check_short_signal(self, adx_green: float, adx_red: float, rsi: float) -> bool:
        """
        Check if the provided values satisfy the short signal rules.

        Args:
            adx_green (float): The ADX green line value.
            adx_red (float): The ADX red line value.
            rsi (float): The RSI value.

        Returns:
            bool: True if the signal rules are satisfied for a short position, False otherwise.
        """
        is_result_short = False
        self.adx_red_over_green = adx_red > adx_green
        self.rsi_above_70 = rsi > 70
        self.rsi_below_70 = rsi < 70
        
        if self.adx_red_over_green and self.rsi_above_70 and self.rsi_below_70:
            is_result_short = True
            self.reset()
        
        return is_result_short

    def reset(self):
        """
        Reset the state of the signal rules.
        """
        self.adx_green_over_red = False
        self.adx_red_over_green = False
        self.rsi_below_30 = False
        self.rsi_above_30 = False
        self.rsi_above_70 = False
        self.rsi_below_70 = False
