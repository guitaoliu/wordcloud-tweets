import time

import schedule

from .config import GENERATE_CYCLE, DAYS
from .wordcloud import run
from .logger import logger
from .push2web import push2web

def run_schedule():
    schedule.every(GENERATE_CYCLE).days.do(run).run()
    schedule.every(GENERATE_CYCLE).days.do(push2web).run()
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logger.info("You have canceled all jobs")
            return