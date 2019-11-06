import logging

logger = logging.getLogger(__name__)


class BaseHandler(object):
    subscription = ()

    def process(self, event, context):
        raise NotImplementedError
