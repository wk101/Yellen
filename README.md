
<p align="left">
<a href="https://circleci.com/gh/badges/shields/tree/master">
        <img src="https://img.shields.io/circleci/project/github/badges/shields/master" alt="build status"></a>
    <a href="https://coveralls.io/github/badges/shields">
        <img src="https://img.shields.io/coveralls/github/badges/shields"
            alt="coverage"></a>
</p>

# Quant Connect Yellen Trading Strategy


The Yellen Trading Strategy is a trend-following forex trading strategy that aims to identify potential long trading opportunities in the GBP/USD currency pair. The strategy utilizes a combination of technical indicators, including the Relative Strength Index (RSI) and the Average Directional Index (ADX), to generate trading signals.

**Strategy Overview:**

1. **Indicators:**
   - Relative Strength Index (RSI): The RSI is a momentum oscillator that measures the speed and change of price movements. It oscillates between 0 and 100, where values above 70 indicate overbought conditions, and values below 30 indicate oversold conditions.
   - Average Directional Index (ADX): The ADX is a trend strength indicator that ranges from 0 to 100. High ADX values indicate a strong trend, while low values suggest a weak or ranging market.

2. **Signal Generation:**
   - The strategy uses the `SignalRules` class to evaluate the values of RSI and ADX and other conditions to determine potential long trading signals.
   - A long trading signal is generated when specific criteria are met, indicating a potential upward price movement and the presence of a strong trend.

3. **Signal Confirmation:**
   - To avoid overtrading and manage risk, the `SignalProcessor` class is employed to process the long trading signals.
   - The `SignalProcessor` considers the current trade count and recent price movement to decide whether to confirm or filter out the long signal.
   - This component helps enhance the strategy by focusing on higher-probability trading opportunities and reducing unnecessary trades.

4. **Order Sizing:**
   - The `OrderSize` class calculates the appropriate position size for each long trade based on the current trade count and the lot size of the GBP/USD forex pair.
   - Proper position sizing is essential for effective risk management, and this class ensures that trade sizes are adjusted according to the strategy's progress.

5. **Take Profit and Stop Loss:**
   - The `TakeProfit` class determines the take profit price for each long trade.
   - The strategy aims to capture profits when certain conditions are met, closing winning trades at favorable price levels.
   - The `StopLoss` class, while not included in the provided code, would determine the stop loss price for each long trade to limit potential losses if the market moves against the position.

6. **Trading Frequency Control:**
   - The `TimeFrameChecker` class helps control the frequency of trades by imposing a one-hour pause after each long trade execution.
   - This mechanism prevents consecutive trades within a short time frame, providing a cooldown period before considering new opportunities.

## Backtest Yellen Trading Strategy

This provides a comprehensive guide on backtesting the Yellen Trading Strategy using the QuantConnect platform. The Yellen Trading Strategy aims to identify potential long trading opportunities in the GBP/USD forex pair based on a combination of the RSI (Relative Strength Index) and ADX (Average Directional Index) indicators. Please remember that this strategy is purely for educational purposes and does not constitute financial advice. Always exercise caution and conduct thorough research before deploying any trading strategy in real markets.

![image](https://github.com/wk101/yellen/assets/106099024/42b278be-477e-4e81-b49b-f4a4b343173c)

### QuantConnect Strategy Overview

The Yellen Trading Strategy is implemented as a custom algorithm using the QuantConnect platform. The strategy utilizes various components to process signals, determine order sizes, set take profit levels, and manage stop-loss rules. Below is an overview of the key components used in the strategy:

1. **SignalRules**: This component evaluates trading signals based on the RSI, ADX, and other conditions to determine if a long trade should be initiated.

2. **SignalProcessor**: The SignalProcessor component further processes long trading signals based on the current trade count and price movement, helping to manage risk and avoid overtrading.

3. **OrderSize**: The OrderSize component calculates the appropriate position size for each trade based on the current trade count and the lot size of the forex pair.

4. **TakeProfit**: This component determines the take profit price for each long trade, aiming to capture profits when certain conditions are met.

5. **StopLoss**: While not present in the provided code, you can add a StopLoss component to manage the risk of each trade, ensuring losses are limited if the market moves against the position.

6. **TimeFrameChecker**: The TimeFrameChecker component ensures that trading is paused for one hour after each long trade execution, helping to manage frequency and avoid consecutive trades.

### Backtesting Steps on QuantConnect

1. **Create a QuantConnect Account**: If you don't have one, sign up for a free QuantConnect account at https://www.quantconnect.com/.

2. **Access the IDE**: Log in to your QuantConnect account and access the QuantConnect Integrated Development Environment (IDE).

3. **Create a New Algorithm**: In the IDE, click on the "New Algorithm" button to create a new algorithm.

4. **Implement the Strategy**: In the code editor, paste the provided code from the Yellen Trading Strategy implementation.

5. **Set Strategy Parameters**: Review and set the desired start and end dates for the backtest using `SetStartDate` and `SetEndDate` methods. Define the initial cash balance with `SetCash`.

6. **Add Missing Components**: If the StopLoss component or any other necessary parts are not included in the provided code, implement them based on your risk management preferences.

7. **Run the Backtest**: Click on the "Backtest" button to start the backtesting process. The QuantConnect platform will use historical data to execute the strategy and generate performance metrics.

8. **Analyze Results**: Once the backtest is complete, carefully analyze the backtesting results, including performance metrics, charts, and insights. Pay attention to drawdowns, win rates, and other risk-related metrics.

9. **Optimization (Optional)**: Depending on the results, you can perform parameter optimization, adjust strategy components, or try different variations to enhance performance. Remember to avoid overfitting and validate results across various market conditions.

### Risk and Caution

It's crucial to recognize that backtesting results may not accurately reflect future performance. Real-world trading involves numerous unpredictable factors and risks. Always consider risk management practices, such as stop-loss and position sizing, and thoroughly test the strategy under various market conditions before deploying it in live markets.

### Long Entry Rules:
ADX Indicator: The green line (also known as the Positive Directional Movement Indicator or +DMI) must be above the red line (Negative Directional Movement Indicator or -DMI) on the daily chart. This suggests that there is a strong upward trend.

RSI Indicator: The RSI (9) falls below 30 (indicating oversold conditions) and then rises back above 30. This suggests that the price might be reversing from a downward trend to an upward trend.

### Short Entry Rules:
ADX Indicator: The red line (-DMI) must be above the green line (+DMI) on the daily chart. This indicates that there is a strong downward trend.

RSI Indicator: The RSI (9) goes above 70 (indicating overbought conditions) and then falls back below 70. This suggests that the price might be reversing from an upward trend to a downward trend.

## Classes

The Yellen trading strategy is a comprehensive trading system that combines multiple components to identify trade entries and manage position sizes. This repository contains classes for implementing the different components of the Yellen strategy.


### 1. TakeProfit

A class to calculate the take profit level based on the number of trades, the latest price, and the trade type. The take profit level is adjusted based on predefined rules for each trade.

**Attributes:**

- `tp_values` (List[float]): List containing percentage values for take profit adjustments according to the number of trades.
- `first_trade_price` (Optional[float]): The price of the first trade. None if no trades have been executed.

**Methods:**

- `calculate_tp(trade_count: int, price: float, trade_type: str) -> float`: Calculates and returns the take profit level based on the number of trades, the latest price, and the trade type.

### 2. OrderSize

A class to calculate the lot size for each trade based on the trade number. The lot size is increased by a fixed multiplier for each subsequent trade.

**Attributes:**

- `initial_lot_size` (int): The initial lot size for the first trade.
- `lot_multiplier` (float): The multiplier to increase the lot size for each subsequent trade.

**Methods:**

- `calculate_lot_size(trade_num: int) -> int`: Calculates and returns the lot size for the given trade number.

- `reset_size() -> None`: Resets the lot size to the initial value and pauses trading for a specified time. Sends an email notification after the pause.

### 3. TargetPrice

A class to calculate the target price for a trade based on the entry price and a specified price movement percentage.

**Methods:**

- `calculate_target_price(entry_price: float, price_movement: float) -> float`: Calculates and returns the target price for the trade based on the entry price and the specified price movement percentage.

### 4. RSI (Relative Strength Index) Class

The RSI (Relative Strength Index) is a momentum oscillator widely used in technical analysis to measure the speed and change of price movements. It was developed by J. Welles Wilder Jr. and is a popular tool for identifying overbought and oversold conditions in the market.

#### RSI Introduction

The RSI is classified as a momentum oscillator because it measures the rate of change of price movements. As J. Welles Wilder Jr. noted, the slope of a momentum oscillator is directly proportional to the velocity of the move, and the distance traveled up or down by the oscillator is proportional to the magnitude of the move. Oscillators, including the RSI, provide valuable insights into the rate of change of price movements.

However, Wilder also pointed out three main issues with momentum oscillators that can be challenging for those unfamiliar with their calculations:

1. Erratic Movements: Momentum oscillators, including the RSI, can exhibit erratic movements due to short-term price fluctuations and market noise. Traders and analysts need to consider this factor when interpreting the oscillator readings.

2. Scale of Y-Axis: The scale of the Y-axis on the oscillator chart does not provide a direct measure to compare current and previous pricing. It's important to understand that the Y-axis represents the oscillator value rather than the actual price.

3. Historical Data Requirement: To generate new calculations, momentum oscillators like the RSI require retaining measures for all past periods. This means that historical data needs to be considered, and calculations may be influenced by the length of the historical period.

#### Usage

The RSI class provides a simple implementation to calculate the Relative Strength Index for a given array of price values. It follows the standard RSI formula and includes the calculation of average gains and average losses over a specified period.

To use the RSI class, follow these steps:

1. Instantiate an RSI object with the desired period length.
2. Call the `calculate` method and provide an array of price values.
3. The method will return an array of RSI values corresponding to the input prices.

Example usage:

```python
import numpy as np
from rsi import RSI

# Create an instance of the RSI class
rsi_calculator = RSI(period=14)

# Define an array of price values
prices = np.array([50, 55, 60, 57, 58, 56, 53, 54, 52, 50, 51, 49, 48, 50])

# Calculate the RSI values
rsi_values = rsi_calculator.calculate(prices)

print(rsi_values)

```

### 5. ADX

A class to calculate the Average Directional Index (ADX) for a given price data series.

**Methods:**

- `calculate_adx(price_data: List[float], period: int) -> float`: Calculates and returns the ADX value for the given price data series and the specified period.

## Usage

Here's an example of how to use the Yellen trading strategy classes in your trading system:

```python
from calculators.take_profit import TakeProfit
from calculators.order_size import OrderSize
from strategy.calculators.target_price import TargetPrice
from strategy.indicators.rsi import RSI
from strategy.indicators.adx import ADX
from strategy.order import Order

# Create instances of the classes
tp = TakeProfit()
order_size = OrderSize()
target_price = TargetPrice()
rsi = RSI()
adx = ADX()
order = Order("long", 1.2345, 100000)

# Calculate take profit level
tp_level = tp.calculate_tp(2, 1.235, "long")

# Calculate lot size
lot_size = order_size.calculate_lot_size(3)

# Calculate target price
target = target_price.calculate_target_price(1.2345, 0.5)

# Calculate RSI value
rsi_value = rsi.calculate_rsi([1.234, 1.235, 1.236, 1.237, 1.238], 5)

# Calculate ADX value
adx_value = adx.calculate_adx([1.234, 1.235, 1.236, 1.237, 1.238], 14)


```

This example demonstrates how to utilize the different components of the Yellen trading strategy. You can customize and integrate these classes into your trading system based on your specific requirements.

---

