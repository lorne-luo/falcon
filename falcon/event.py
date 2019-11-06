from decimal import Decimal

from falcon.base.event import BaseEvent
from falcon.base.order import OrderType
from falcon.base.symbol import get_mt4_symbol


class EventType(object):
    DEBUG = 'DEBUG'
    STARTUP = 'STARTUP'  # system start up
    SHUTDOWN = 'SHUTDOWN'  # system shutdown
    HEARTBEAT = 'HEARTBEAT'
    TICK_PRICE = 'TICK_PRICE'  # tick price
    TIMEFRAME = 'TIMEFRAME'  # time frame changes
    SIGNAL = 'SIGNAL'
    ORDER_CLOSE = 'ORDER_CLOSE'
    ORDER_HOLDING = 'ORDER_HOLDING'
    TRADE_OPEN = 'TRADE_OPEN'
    TRADE_CLOSE = 'TRADE_CLOSE'
    ORDER = 'ORDER'
    MARKET = 'MARKET'


class StartUpEvent(BaseEvent):
    type = EventType.STARTUP


class ShutdownEvent(BaseEvent):
    type = EventType.SHUTDOWN


class HeartBeatEvent(BaseEvent):
    type = EventType.HEARTBEAT

    def __init__(self, hearbeat_count):
        super(HeartBeatEvent, self).__init__()
        self.counter = hearbeat_count


class DebugEvent(BaseEvent):
    type = EventType.DEBUG

    def __init__(self, action):
        super(DebugEvent, self).__init__()
        self.action = action


class TimeFrameEvent(BaseEvent):
    type = EventType.TIMEFRAME

    def __init__(self, timeframe, current_time, previous, timezone, time):
        super(TimeFrameEvent, self).__init__()
        self.timeframe = timeframe
        self.current_time = current_time
        self.previous = previous
        self.timezone = timezone
        self.time = time


class MarketEvent(BaseEvent):
    type = EventType.MARKET

    def __init__(self, action):
        super(MarketEvent, self).__init__()
        self.action = action


class TickPriceEvent(BaseEvent):
    type = EventType.TICK_PRICE

    def __init__(self, broker, instrument, time, bid, ask):
        super(TickPriceEvent, self).__init__()
        self.broker = broker
        self.instrument = instrument
        self.time = time
        self.bid = bid
        self.ask = ask

    def __str__(self):
        return "Type: %s, Instrument: %s, Time: %s, Bid: %s, Ask: %s" % (
            str(self.type), str(self.instrument),
            str(self.time), str(self.bid), str(self.ask)
        )


class SignalEvent(BaseEvent):
    type = EventType.SIGNAL

    def __init__(self, action, strategy_name, version, magic_number, instrument, side, price=None,
                 stop_loss=None, take_profit=None, trailing_stop=None, percent=None, trade_id=None,
                 order_type=OrderType.MARKET):
        self.action = action
        self.strategy = strategy_name
        self.version = version
        self.magic_number = magic_number
        self.instrument = instrument
        self.order_type = order_type
        self.side = side
        self.price = price
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.trailing_stop = trailing_stop
        self.percent = percent
        self.trade_id = trade_id
        super(SignalEvent, self).__init__()

    def __str__(self):
        return "Type: %s, Instrument: %s, Order Type: %s, Side: %s" % (
            str(self.type), str(self.instrument),
            str(self.order_type), str(self.side)
        )


class OrderUpdateEvent(BaseEvent):
    """order update signal"""
    type = EventType.ORDER_CLOSE

    def __init__(self, strategy_name, version, magic_number, instrument, stop_loss=None, take_profit=None,
                 trailing_stop=None, percent=None):
        self.strategy = strategy_name
        self.version = version
        self.magic_number = magic_number
        self.instrument = instrument
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.trailing_stop = trailing_stop
        self.percent = percent
        super(OrderUpdateEvent, self).__init__()


class OrderHoldingEvent(BaseEvent):
    """order holding, to notify strategy to calculate close signal"""
    type = EventType.ORDER_HOLDING

    def __init__(self, magic_number, orders):
        self.orders = orders
        self.magic_number = magic_number
        super(OrderHoldingEvent, self).__init__()


class TradeCloseEvent(BaseEvent):
    type = EventType.ORDER_CLOSE

    def __init__(self, broker, account_id, trade_id, instrument, side, lots, profit, close_time, close_price, pips=None,
                 open_time=None):
        self.broker = broker
        self.account_id = account_id
        self.trade_id = trade_id
        self.instrument = get_mt4_symbol(instrument)
        self.side = side
        self.lots = lots
        self.profit = Decimal(str(profit))
        self.close_price = Decimal(str(close_price))
        self.close_time = close_time
        self.open_time = open_time
        self.pips = Decimal(str(pips)) if pips else None
        super(TradeCloseEvent, self).__init__()

    def to_text(self):
        last = ''
        if self.open_time:
            last = self.open_time - self.close_time
        text = '%s#%s\n%s = %s\nprofit = %s' % (
            self.instrument, self.trade_id, self.side, self.lots, self.profit)
        if self.pips:
            text += '\npips = %s' % self.pips
        if last:
            text += '\nlast = %s' % str(last)
        return text


class TradeOpenEvent(BaseEvent):
    type = EventType.TRADE_OPEN

    def __init__(self, broker, account_id, trade_id, instrument, side, lots, open_time, open_price, stop_loss=None,
                 take_profit=None, magic_number=None):
        self.broker = broker
        self.account_id = account_id
        self.trade_id = trade_id
        self.instrument = get_mt4_symbol(instrument)
        self.side = side
        self.lots = lots
        self.open_time = open_time
        self.open_price = Decimal(str(open_price))
        self.stop_loss = Decimal(str(stop_loss)) if stop_loss else None
        self.take_profit = Decimal(str(take_profit)) if take_profit else None
        self.magic_number = magic_number
        super(TradeOpenEvent, self).__init__()

    def to_text(self):
        text = 'ST#%s\n%s#%s\n%s = %s\nprice = %s\nSL = %s\nTP = %s' % (
            self.magic_number, self.instrument, self.trade_id, self.side, self.lots, self.open_price, self.stop_loss,
            self.take_profit)
        return text


class OrderEvent(BaseEvent):
    type = EventType.ORDER

    def __init__(self, instrument, units, order_type, side, expiry=None, price=None, lowerBound=None, upperBound=None,
                 stopLoss=None, takeProfit=None, trailingStop=None):
        self.instrument = instrument
        self.units = units
        self.order_type = order_type
        self.side = side
        self.expiry = expiry
        self.price = price
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.stopLoss = stopLoss
        self.takeProfit = takeProfit
        self.trailingStop = trailingStop
        super(OrderEvent, self).__init__()

    def __str__(self):
        return "Type: %s, Instrument: %s, Units: %s, Order Type: %s, Side: %s" % (
            str(self.type), str(self.instrument), str(self.units),
            str(self.order_type), str(self.side)
        )


class ConnectEvent(BaseEvent):
    def __init__(self, action):
        self.action = action.upper()
        super(ConnectEvent, self).__init__()
