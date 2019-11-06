import logging
import sys
import time
import traceback

from .handler import BaseHandler

logger = logging.getLogger(__name__)


class BaseRunner(object):
    loop_sleep = 1
    empty_sleep = 2

    def __init__(self, queue_name, accounts, *args, **kwargs):
        self.handlers = []
        self.running = False
        self.halt = False
        self.accounts = accounts if type(accounts) is list else [accounts]
        self.queue_name = queue_name
        self.queue = self.create_queue(queue_name)

    def stop(self):
        del self.queue
        self.running = False
        sys.exit(0)

    def create_queue(self, queue_name):
        raise NotImplementedError

    def register(self, *args):
        """register handlers"""
        for handler in args:
            if isinstance(handler, BaseHandler):
                self.handlers.append(handler)

    def launch(self):
        """before actcul run event bus"""
        logger.info('%s statup.' % self.__class__.__name__)
        logger.info('Registered handler: %s' % ', '.join([x.__class__.__name__ for x in self.handlers]))
        self.running = True
        self.halt = False

    def loop_start(self):
        pass

    def loop_end(self):
        pass

    def yield_event(self, block=False):
        raise NotImplementedError

    def put_event(self, event):
        raise NotImplementedError

    def handle_error(self, ex):
        pass

    def loop_handlers(self, event):
        """loop handlers to process event"""
        re_put = False
        for handler in self.handlers:
            if '*' in handler.subscription:
                result = self.handle_event(handler, event)
                re_put = result or re_put
                continue
            elif event.type in handler.subscription:
                result = self.handle_event(handler, event)
                re_put = result or re_put
        if re_put:
            if event.tried > 10:
                logger.error('[EVENT_RETRY] tried to many times abort, event=%s' % event)
            else:
                event.tried += 1
                self.put_event(event)

    def handle_event(self, handler, event):
        """process event by single handler"""
        try:
            return handler.process(event, self)
        except Exception as ex:
            logger.error('[EVENT_PROCESS] %s, event=%s' % (ex, event.__dict__))
            # print trace stack
            extracted_list = traceback.extract_tb(ex.__traceback__)
            for item in traceback.StackSummary.from_list(extracted_list).format()[:8]:
                logger.error(item.strip())
            self.handle_error(ex)

    def run(self):
        self.launch()

        while self.running:
            self.loop_start()

            while self.halt:
                event = self.yield_event()
                if not event:
                    time.sleep(self.empty_sleep)
                    break
                self.loop_handlers(event)

            self.loop_end()
            time.sleep(self.loop_sleep)
