

def run():
    # Create an instance of the FXStrategy class

    strategy = Yellen()

    # Generate OHLC data for 30 bars
    ohlcv_data = generate_ohlcv_data()

    # Process each bar using the strategy
    for bar in ohlcv_data:
        strategy.on_bar(bar)

if __name__ == '__main__':
    run()

