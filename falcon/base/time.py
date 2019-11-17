import re
import time
import datetime

from dateparser import parse


def parse_timestamp(timestamp, utc=False):
    if utc:
        return datetime.datetime.utcfromtimestamp(timestamp)
    else:
        return datetime.datetime.fromtimestamp(timestamp)


def datetime_to_timestamp(dt):
    return time.mktime(dt.timetuple())


def datetime_to_str(dt, format='%Y-%m-%d %H:%M:%S:%f'):
    if dt:
        return dt.strftime(format)
    return None


def str_to_datetime(string, format='%Y-%m-%d %H:%M:%S:%f'):
    if string:
        try:
            dt = datetime.datetime.strptime(string, format)
        except:
            dt = parse(string)

        return dt
    return None


def timestamp_to_str(timestamp, datetime_fmt="%Y/%m/%d %H:%M:%S:%f"):
    return datetime.datetime.fromtimestamp(timestamp).strftime(datetime_fmt)


def parse_date(value):
    date_re = re.compile(
        r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})$'
    )
    match = date_re.match(value)
    if match:
        kw = {k: int(v) for k, v in match.groupdict().items()}
        return datetime.date(**kw)
