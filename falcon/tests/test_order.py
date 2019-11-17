from decimal import Decimal

from falcon.base.order import units_to_lots, lots_to_units, UNIT_RATIO


def test_units_to_lots():
    lots = units_to_lots(UNIT_RATIO)
    assert lots == 1
    assert type(lots) is Decimal


def test_lots_to_units():
    units = lots_to_units(1)
    assert units == UNIT_RATIO
    assert type(units) is Decimal
