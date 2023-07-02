from typing import List
from strategy.indicators.rsi import RSI
from strategy.indicators.adx import ADX
from strategy.signal_calculator import SignalCalculator
from strategy.position_processor import PositionProcessor
from strategy.stop_loss import StopLoss
from metatrader_client import MetaTraderClient


class YellenStrategy:
    def __init__(self) -> None:
        self.rsi_red: RSI = RSI(period=7)
        self.rsi_green: RSI = RSI(period=14)
        self.adx: ADX = ADX()
        self.signal_calculator: SignalCalculator = SignalCalculator()
        self.position_processor: PositionProcessor = PositionProcessor()
        self.stop_loss: StopLoss = StopLoss()

    def calculate_indicators(self) -> None:
        """
        Calculate the necessary indicators for the strategy.
        """
        # Retrieve OHLC data from MetaTrader client
        ohlc: List[float] = MetaTraderClient.get_ohlc()

        # Calculate ADX
        self.adx.calculate(ohlc)

        # Calculate RSI
        self.rsi_red.calculate(ohlc)
        self.rsi_green.calculate(ohlc)

    def calculate_signals(self) -> None:
        """
        Calculate trading signals based on the indicators.
        """
        self.signal_calculator.calculate_signals(
            self.adx.green_line, self.adx.red_line,
            self.rsi_green.value, self.rsi_red.value
        )

    def process_positions(self) -> None:
        """
        Process and adjust the positions based on the signals.
        """
        self.position_processor.process_positions(self.signal_calculator.signals)

    def process_order(self) -> None:
        """
        Process the order for trade execution.
        """
        self.position_processor.process_order(self.signal_calculator.signals, self.stop_loss)

    def on_new_bar(self) -> None:
        """
        Perform necessary actions when a new bar is formed.
        """
        self.calculate_indicators()
        self.calculate_signals()
        self.process_positions()
        self.process_order()

    def run_strategy(self) -> None:
        """
        Run the Yellen strategy.
        """
        # Perform initial setup
        self.calculate_indicators()
        self.calculate_signals()
        self.process_positions()
        self.process_order()

        # Start monitoring for new bars
        while True:
            # Wait for a new bar formation
            MetaTraderClient.wait_for_new_bar()

            # Perform actions on new bar
            self.on_new_bar()
