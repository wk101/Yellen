from typing import List
from processor.signal_processor import SignalProcess
from strategy.trading_client import TradingClient
from calculators.stop_loss import StopLoss
from calculators.take_profit import TakeProfit


class ProcessNewOrder:
    def __init__(self, trading_client: TradingClient):
        self.trading_client = trading_client
        self.signal_processor = SignalProcess()
        self.stop_loss = StopLoss()
        self.take_profit = TakeProfit()

    def execute_trades(self, adx_green: float, adx_red: float, rsi: float):
        """
        Execute trades based on the ADX green, ADX red, and RSI values.

        Args:
            adx_green (float): The ADX green line value.
            adx_red (float): The ADX red line value.
            rsi (float): The RSI value.
        """
        processed_signal = self.signal_processor.process_indicator(adx_green, adx_red, rsi)
        if processed_signal == "Long":
            sl_level = self.stop_loss.calculate_sl("long")
            tp_level = self.take_profit.calculate_tp(1, self.trading_client.get_current_price(), "long")
            self.trading_client.create_long_trade(sl_level, tp_level)
        elif processed_signal == "Short":
            sl_level = self.stop_loss.calculate_sl("short")
            tp_level = self.take_profit.calculate_tp(1, self.trading_client.get_current_price(), "short")
            self.trading_client.create_short_trade(sl_level, tp_level)
        else:
            self.trading_client.close_all_trades()

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
