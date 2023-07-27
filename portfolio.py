from AlgorithmImports import *
from QuantConnect import *
from signal_rules import SignalRules
from signal_processor import SignalProcessor
from order_size import OrderSize
from take_profit import TakeProfit
from stop_loss import StopLoss
from hourly_counter import TimeFrameChecker
from main import *


class YellenPortfolio(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2022, 12, 1)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash

        # Define the configurations for the two instances of the Yellen strategy
        config1 = StrategyConfiguration(initial_size=100, lot_size=10000)
        config2 = StrategyConfiguration(initial_size=50, lot_size=5000)

        # Create the two instances of the Yellen strategy with their respective configurations
        self.yellen1 = self.AddAlgorithm(Yellen, "Yellen1", config1)
        self.yellen2 = self.AddAlgorithm(Yellen, "Yellen2", config2)
        
        # Define the allocation percentages for each strategy
        self.allocation_yellen1 = 0.5  # 50% allocation to Yellen1
        self.allocation_yellen2 = 0.5  # 50% allocation to Yellen2

        # Todo Fix this
        # Schedule the portfolio rebalancing event (e.g., every month)
        self.Schedule.On(self.DateRules.MonthStart("AAPL"), self.TimeRules.AfterMarketOpen("AAPL"), self.RebalancePortfolio)

    def RebalancePortfolio(self):
        # Calculate the target allocations based on the strategy allocation percentages
        total_allocation = self.allocation_yellen1 + self.allocation_yellen2

        target_allocation_yellen1 = self.allocation_yellen1 / total_allocation
        target_allocation_yellen2 = self.allocation_yellen2 / total_allocation

        # Set the target allocations for each strategy
        self.SetHoldings(self.yellen1.Symbol, target_allocation_yellen1)
        self.SetHoldings(self.yellen2.Symbol, target_allocation_yellen2)
