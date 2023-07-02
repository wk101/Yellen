import pytest
from strategy.calculators.order_size import OrderSize


@pytest.fixture
def order_size() -> OrderSize:
    return OrderSize(initial_size=1.0)


def test_calculate_size(order_size: OrderSize) -> None:
    assert order_size.calculate_size(1) == pytest.approx(100000.0)
    assert order_size.calculate_size(2) == pytest.approx(130000.0)
    assert order_size.calculate_size(3) == pytest.approx(169000.0)
    assert order_size.calculate_size(4) == pytest.approx(219700.0)
    assert order_size.calculate_size(5) == pytest.approx(285610.0)
    assert order_size.calculate_size(31) == pytest.approx(100000.0)
