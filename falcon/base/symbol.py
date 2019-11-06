from decimal import Decimal

PIP_DICT = {
    # Currency
    'USDDKK': Decimal('0.0001'),
    'EURAUD': Decimal('0.0001'),
    'CHFJPY': Decimal('0.01'),
    'EURSGD': Decimal('0.0001'),
    'USDJPY': Decimal('0.01'),
    'EURTRY': Decimal('0.0001'),
    'USDCZK': Decimal('0.0001'),
    'GBPAUD': Decimal('0.0001'),
    'USDPLN': Decimal('0.0001'),
    'USDSGD': Decimal('0.0001'),
    'EURSEK': Decimal('0.0001'),
    'USDHKD': Decimal('0.0001'),
    'EURNZD': Decimal('0.0001'),
    'SGDJPY': Decimal('0.01'),
    'AUDCAD': Decimal('0.0001'),
    'GBPCHF': Decimal('0.0001'),
    'USDTHB': Decimal('0.01'),
    'TRYJPY': Decimal('0.01'),
    'CHFHKD': Decimal('0.0001'),
    'AUDUSD': Decimal('0.0001'),
    'EURDKK': Decimal('0.0001'),
    'EURUSD': Decimal('0.0001'),
    'AUDNZD': Decimal('0.0001'),
    'SGDHKD': Decimal('0.0001'),
    'EURHUF': Decimal('0.01'),
    'USDCNH': Decimal('0.0001'),
    'EURHKD': Decimal('0.0001'),
    'EURJPY': Decimal('0.01'),
    'NZDUSD': Decimal('0.0001'),
    'GBPPLN': Decimal('0.0001'),
    'GBPJPY': Decimal('0.01'),
    'USDTRY': Decimal('0.0001'),
    'EURCAD': Decimal('0.0001'),
    'USDSEK': Decimal('0.0001'),
    'GBPSGD': Decimal('0.0001'),
    'EURGBP': Decimal('0.0001'),
    'GBPHKD': Decimal('0.0001'),
    'USDZAR': Decimal('0.0001'),
    'AUDCHF': Decimal('0.0001'),
    'USDCHF': Decimal('0.0001'),
    'USDMXN': Decimal('0.0001'),
    'GBPUSD': Decimal('0.0001'),
    'EURCHF': Decimal('0.0001'),
    'EURNOK': Decimal('0.0001'),
    'AUDSGD': Decimal('0.0001'),
    'CADCHF': Decimal('0.0001'),
    'SGDCHF': Decimal('0.0001'),
    'CADHKD': Decimal('0.0001'),
    'USDINR': Decimal('0.01'),
    'NZDCAD': Decimal('0.0001'),
    'GBPZAR': Decimal('0.0001'),
    'NZDSGD': Decimal('0.0001'),
    'ZARJPY': Decimal('0.01'),
    'CADJPY': Decimal('0.01'),
    'GBPCAD': Decimal('0.0001'),
    'USDSAR': Decimal('0.0001'),
    'NZDCHF': Decimal('0.0001'),
    'NZDHKD': Decimal('0.0001'),
    'GBPNZD': Decimal('0.0001'),
    'AUDHKD': Decimal('0.0001'),
    'EURCZK': Decimal('0.0001'),
    'CHFZAR': Decimal('0.0001'),
    'USDHUF': Decimal('0.01'),
    'NZDJPY': Decimal('0.01'),
    'HKDJPY': Decimal('0.0001'),
    'CADSGD': Decimal('0.0001'),
    'USDNOK': Decimal('0.0001'),
    'USDCAD': Decimal('0.0001'),
    'AUDJPY': Decimal('0.01'),
    'EURPLN': Decimal('0.0001'),
    'EURZAR': Decimal('0.0001'),
    # METAL
    'XAUGBP': Decimal('0.01'),
    'XAGUSD': Decimal('0.0001'),
    'XAUNZD': Decimal('0.01'),
    'XAUXAG': Decimal('0.01'),
    'XAGJPY': Decimal('1'),
    'XAGHKD': Decimal('0.0001'),
    'XAGAUD': Decimal('0.0001'),
    'XAUCAD': Decimal('0.01'),
    'XAUAUD': Decimal('0.01'),
    'XAUJPY': Decimal('10'),
    'XAUHKD': Decimal('0.01'),
    'XPDUSD': Decimal('0.01'),
    'XAUUSD': Decimal('0.01'),
    'XAGCAD': Decimal('0.0001'),
    'XAUSGD': Decimal('0.01'),
    'XAGSGD': Decimal('0.0001'),
    'XAGEUR': Decimal('0.0001'),
    'XAGCHF': Decimal('0.0001'),
    'XPTUSD': Decimal('0.01'),
    'XAUCHF': Decimal('0.01'),
    'XAGNZD': Decimal('0.0001'),
    'XAGGBP': Decimal('0.0001'),
    'XAUEUR': Decimal('0.01'),
    # CFD
    'UK10YBGBP': Decimal('0.01'),
    'DE10YBEUR': Decimal('0.01'),
    'WTICOUSD': Decimal('0.01'),
    'BTCUSD': Decimal('1'),
    'NL25EUR': Decimal('0.01'),
    'CORNUSD': Decimal('0.01'),
    'SPX500USD': Decimal('1'),
    'JP225USD': Decimal('1'),
    'MBTCUSD': Decimal('0.01'),
    'USB02YUSD': Decimal('0.01'),
    'IN50USD': Decimal('1'),
    'TWIXUSD': Decimal('1'),
    'WHEATUSD': Decimal('0.01'),
    'HK33HKD': Decimal('1'),
    'US2000USD': Decimal('0.01'),
    'SUGARUSD': Decimal('0.0001'),
    'US30USD': Decimal('1'),
    'USB05YUSD': Decimal('0.01'),
    'NATGASUSD': Decimal('0.01'),
    'USB30YUSD': Decimal('0.01'),
    'SG30SGD': Decimal('0.1'),
    'AU200AUD': Decimal('1'),
    'CN50USD': Decimal('1'),
    'SOYBNUSD': Decimal('0.01'),
    'USB10YUSD': Decimal('0.01'),
    'EU50EUR': Decimal('1'),
    'FR40EUR': Decimal('1'),
    'BCOUSD': Decimal('0.01'),
    'NAS100USD': Decimal('1'),
    'DE30EUR': Decimal('1'),
    'XCUUSD': Decimal('0.0001'),
    'UK100GBP': Decimal('1'),
}

MT4_SYMBOLS = list(PIP_DICT.keys())


def get_mt4_symbol(symbol):
    symbol = str(symbol)
    return symbol.replace(' ', '').replace('_', '').replace('-', '').replace('/', '')