from AlgorithmImports import *
from QuantConnect import *
from signal_rules import SignalRules
from signal_processor import SignalProcessor
from order_size import OrderSize
from take_profit import TakeProfit
from stop_loss import StopLoss
from hourly_counter import TimeFrameChecker


class Yellen(QCAlgorithm):

    def Initialize(self):
        self.Debug(f'Yellen started!!!')
        self.long_stop_loss = 0.0
        self.long_take_profit = 0.0
        self.long_trade_count = 0
        self.long_last_trade_price = 0.00
        self.long = False
        self.pause_trading = False

        self.short_stop_loss = 0.0
        self.short_take_profit = 0.0
        self.short_trade_count = 0
        self.short_last_trade_price = 0.0
        self.short = False

        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetCash(1000000)  # Set Strategy Cash
        self.symbol = self.AddForex("GBPUSD", Resolution.Minute, Market.Oanda).Symbol
        self.SetBrokerageModel(BrokerageName.OandaBrokerage)
        self.Consolidate(self.symbol, timedelta(minutes=5), self.OnDataConsolidated)

        # Add signal component
        self.signal_rules = SignalRules()
        
        # Add signal proccessor component
        self.signal_processor = SignalProcessor()
        
        # Add signal hourly component
        self.time_frame_checker = TimeFrameChecker()
        
        # Add order size component    
        self.order_size = OrderSize(initial_size=100, _lot_size=self.Securities["GBPUSD"].SymbolProperties.LotSize)
        
        # Add take_profit component    
        self.take_profit_rules = TakeProfit()
        
        # Add stop loss component    
        self.stop_loss_rules = StopLoss()
        
        # Add RSI indicator
        self.rsi = self.RSI(self.symbol, 9, Resolution.Minute)
        self.adx = self.ADX(self.symbol, 14, Resolution.Daily)
      
        self.pause_long_trading = False
        
        # Initialize StopLoss and TakeProfit calculators
        account_drawdown = 0.0  # Initialize account drawdown
        pair_drawdown = 0.0  # Initialize pair drawdown
        
    def OnDataConsolidated(self, bar):
        # self.Debug(f'Ask close {bar.Ask.Close}')
        # Update RSI with current bar
        price = bar.Ask.Close
        self.rsi.Update(bar.EndTime, bar.Ask.Close)
        # self.Debug(f'Time: {bar.Time} RSI {self.rsi.Current.Value}')
        
        if self.Time.weekday == 0 and self.Time.hour == 0 and self.Time.minute < 11:    
            self.adx.Update(data[self.symbol].EndTime, data[self.symbol].Ask.Close)
        
        
        if self.adx.IsReady:
            # self.Debug(f'Ask close {bar.Ask.Close}')
            # self.Debug(f"Time: {bar.Time} ADX Value: {self.adx.Current.Value}")
            # self.Debug(f"Time: {bar.Time} green PDI Value: {self.adx.PositiveDirectionalIndex.Current.Value}")
            # self.Debug(f"Time: {bar.Time} red NDI Value: {self.adx.NegativeDirectionalIndex.Current.Value}")

            long_result = 0
            short_result = 0
            
            if self.pause_trading:
                self.Debug(f"Time: {bar.Time} **Pause**")
                if self.time_frame_checker.is_one_hour_over():
                    if self.LiveMode:
                        pass
                        # execute this code only if algorithm is in live trading mode
                    self.pause_trading = False
            else:    
                # Check for long trading signals
                
                
                
                long_signal = self.signal_rules.check_long_signal(
                    adx_green=self.adx.PositiveDirectionalIndex.Current.Value,
                    adx_red=self.adx.NegativeDirectionalIndex.Current.Value,
                    rsi=self.rsi.Current.Value
                )
                self.Debug(f"Time: {bar.Time}, long signal {long_signal} trade count {self.long_trade_count} RSI Value: {self.rsi.Current.Value}")
                
                if self.long_trade_count > 1 and long_signal:
                    price_movement = abs((price - self.long_last_trade_price) / price)
                    long_signal = self.signal_processor.process_signal(self.long_trade_count, price_movement)
                
                # Long Trade Execution
                if long_signal:
                    self.Debug(f"Time: {bar.Time} long {self.long_trade_count}")
                    if self.long_trade_count < 29:
                        self.long_trade_count += 1
                        order_size = self.order_size.calculate_size(trade_number=self.long_trade_count)
                        self.long_take_profit = self.take_profit_rules.calculate_tp(self.long_trade_count, price, "long")
                        if price > self.long_take_profit:
                            self.Liquidate()
                        else:
                            if self.short:
                                self.Liquidate()
                                self.short = False
                            self.long_last_trade_price = price
                            self.MarketOrder(self.symbol, order_size)
                            self.long = True
                    else:
                        self.pause_trading = True
                        self.Liquidate()
                        self.long_trade_count = 0
                    
                        
    
    def OnData(self, data):
        pass
