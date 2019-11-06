from decimal import Decimal

from falcon.base.order import OrderSide
from falcon.base.symbol import get_mt4_symbol, PIP_DICT



def pip(symbol, price=None, _abs=False):
    """
    pip('EURUSD') = 0.0001
    pip('EURUSD', -0.00352) = -35.2
    pip('EURUSD', -0.00352, True) = 35.2
    """
    symbol = get_mt4_symbol(symbol)
    if symbol not in PIP_DICT:
        raise Exception('%s not in PIP_DICT.' % symbol)

    pip_unit = PIP_DICT[symbol]
    if price:
        price = Decimal(str(price))
        if _abs:
            price = abs(price)
        return (price / pip_unit).quantize(Decimal("0.1"))

    return pip_unit


def profit_pip(symbol, open, close, side, _abs=False):
    """
    profit_pip('EURUSD', 1.00492, 1.00372, OrderSide.BUY) = -12
    """
    open = Decimal(str(open))
    close = Decimal(str(close))
    if side == OrderSide.BUY:
        profit = close - open
    else:
        profit = open - close

    return pip(symbol, profit, _abs)


def calculate_price(base_price, side, pips, instrument):
    """
    calculate_price(1.3320, OrderSide.BUY, 20, 'EURUSD') = 1.3340
    """
    instrument = get_mt4_symbol(instrument)
    pip_unit = pip(instrument)
    base_price = Decimal(str(base_price))
    pips = Decimal(str(pips))

    if side == OrderSide.BUY:
        return base_price + pips * pip_unit
    elif side == OrderSide.SELL:
        return base_price - pips * pip_unit
