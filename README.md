
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

