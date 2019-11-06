from datetime import datetime
from decimal import Decimal

from dateparser import parse


class BaseEvent(object):
    """base event model"""
    type = None

    def __init__(self):
        self.time = datetime.utcnow()
        self.tried = 0  # some event may push back to queue for re-process

    def to_dict(self):
        data = self.__dict__.copy()
        for k in data.keys():
            if type(data[k]) in (str, float, int) or data[k] is None:
                pass
            elif type(data[k]) is Decimal:
                data[k] = float(data[k])
            elif isinstance(data[k], datetime):
                data[k] = 'datetime:%s' % data[k].strftime('%Y-%m-%d %H:%M:%S:%f')
            else:
                raise Exception('%s.%s is not serializable.' % (self.__class__.__name__, k))
        data['type'] = self.type
        return data

    @staticmethod
    def from_dict(data):
        instance = BaseEvent()
        for k in data.keys():
            if type(data[k]) is int or data[k] is None:
                pass
            elif type(data[k]) is float:
                data[k] = Decimal(str(data[k]))

            elif type(data[k]) is str:
                if data[k].startswith('datetime:'):
                    dt_str = data[k].replace('datetime:', '')
                    dt = parse(dt_str, date_formats=['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S:%f',
                                                     '%Y-%m-%dT%H:%M:%S'])
                    data[k] = dt or data[k]
            else:
                raise Exception('Event.from_dict %s=%s is not deserializable.' % (k, data[k]))
            setattr(instance, k, data[k])
        return instance
