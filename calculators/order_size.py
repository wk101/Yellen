from typing import List
from processor.signal_processor import SignalProcess
from calculators.stop_loss import StopLoss
from calculators.take_profit import TakeProfit
from QuantConnect import QCAlgorithm, OrderDirection
from calculators.order_size import OrderSize


class ProcessOrder(QCAlgorithm):
    def __init__(self):
        self.signal_processor = SignalProcess()
        self.stop_loss = StopLoss()
        self.take_profit = TakeProfit()
        self.order_size = OrderSize(initial_size=1.0)

    def execute_trades(self, adx_green: float, adx_red: float, rsi: float):
        """
        Execute trades based on the ADX green, ADX red, and RSI values.

        Args:
            adx_green (float): The ADX green line value.
            adx_red (float): The ADX red line value.
            rsi (float): The RSI value.
        """
        processed_signal = self.signal_processor.process_indicator(adx_green, adx_red, rsi)
        order_size = self.order_size.calculate_size()
        if processed_signal == "Long":
            sl_level = self.stop_loss.calculate_sl("long")
            tp_level = self.take_profit.calculate_tp(order_size, self.Securities[self.Symbol].Price, "long")
            self.MarketOrder(self.Symbol, order_size, stopLoss=sl_level, takeProfit=tp_level)
        elif processed_signal == "Short":
            sl_level = self.stop_loss.calculate_sl("short")
            tp_level = self.take_profit.calculate_tp(order_size, self.Securities[self.Symbol].Price, "short")
            self.MarketOrder(self.Symbol, -order_size, stopLoss=sl_level, takeProfit=tp_level)
        else:
            self.Liquidate()

    def execute_trades_batch(self, adx_green_list: List[float], adx_red_list: List[float], rsi_list: List[float]):
        """
        Execute trades in batch based on lists of ADX green, ADX red, and RSI values.

        Args:
            adx_green_list (List[float]): The list of ADX green line values.
            adx_red_list (List[float]): The list of ADX red line values.
            rsi_list (List[float]): The list of RSI values.
        """
        for adx_green, adx_red, rsi in zip(adx_green_list, adx_red_list, rsi_list):
            self.execute_trades(adx_green, adx_red, rsi)
