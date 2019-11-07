from datetime import datetime
from decimal import Decimal

from falcon.base.event import BaseEvent
from falcon.base.market import is_market_open
from falcon.base.order import OrderSide
from falcon.base.order import SignalAction
from falcon.base.price import pip, profit_pip, calculate_price
from falcon.base.symbol import get_mt4_symbol
from falcon.base.time import parse_date
from falcon.base.timeframe import PERIOD_M5, get_candle_time
from falcon.event import SignalEvent, TradeCloseEvent


def test_events_dict():
    event = SignalEvent(action=SignalAction.OPEN,
                        strategy_name='strategy_name',
                        version='1.0',
                        magic_number='123121',
                        instrument='EURUSD',
                        side=OrderSide.BUY,
                        )
    data = event.to_dict()
    e = SignalEvent.from_dict(data)

    now = datetime.now()
    event = TradeCloseEvent(broker='FXCM', account_id='12313123', trade_id='asdfsadfs', instrument='EURUSD',
                            side=OrderSide.BUY, lots=0.1, profit=20, close_time=now, close_price=1.223)
    data = event.to_dict()
    e = BaseEvent.from_dict(data)
    assert event.close_time == e.close_time


def test_market():
    is_open = is_market_open()
    assert isinstance(is_open, bool)


def test_price():
    pips = pip('EURUSD', -0.00352)
    assert pips == Decimal('-35.2')
    pips = pip('EURUSD', -0.00352, True)
    assert pips == Decimal('35.2')

    profit_pips = profit_pip('EURUSD', 1.00351, 1.00372, OrderSide.BUY, True)
    assert profit_pips == Decimal('2.1')

    profit_pips = profit_pip('EURUSD', 1.00351, 1.00372, OrderSide.SELL)
    assert profit_pips == Decimal('-2.1')

    price = calculate_price(1.3320, OrderSide.BUY, 20, 'EURUSD')
    assert price == Decimal('1.3340')


def test_symbol():
    symbol = get_mt4_symbol('EUR/USD')
    assert symbol == 'EURUSD'

    symbol = get_mt4_symbol('EUR_USD')
    assert symbol == 'EURUSD'

    symbol = get_mt4_symbol('EURUSD')
    assert symbol == 'EURUSD'


def test_time():
    candle_time = get_candle_time(datetime.now(), PERIOD_M5)
    assert candle_time.minute % 5 == 0
    assert candle_time.second == 0

    date = parse_date('2019-11-07')
    assert date.day == 7
