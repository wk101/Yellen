import pytest
from your_module import OrderSize

@pytest.fixture
def order_size_instance():
    # Create an instance of OrderSize for testing
    initial_size = 100000  # Change this value as needed
    lot_size = 100000      # Change this value as needed
    return OrderSize(initial_size, lot_size)

def test_calculate_size(order_size_instance):
    # Test the calculate_size method for different trade numbers

    # Test initial trade
    assert order_size_instance.calculate_size(1) == 100000

    # Test a few trades to see if the scaling factor is applied correctly
    assert order_size_instance.calculate_size(2) == 130000
    assert order_size_instance.calculate_size(3) == 169000
    assert order_size_instance.calculate_size(4) == 219700

    # Test a trade after 30 trades (should reset back to the initial size)
    assert order_size_instance.calculate_size(31) == 100000

    # Add more test cases as needed
