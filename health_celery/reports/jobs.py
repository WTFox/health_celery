# Create your tasks here
from __future__ import absolute_import, unicode_literals

import random
import sys
import time

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def time_task(n):
    """ Chooses a random number from 0 to n and sleeps that amount in 
    seconds. Then returns that number as a result.
    """
    logger.info("Starting time task for reports")
    result = random.choice(range(n))
    time.sleep(result)
    return result


@shared_task
def space_task():
    """ Creates 512M empty string objects and stores them in a variable,
    {some_str}. After that, we store the size of the variable, delete it
    from memory, and return the size as the result.
    """
    logger.info("Starting space task for reports")
    some_str = ' ' * 512000000
    size = sys.getsizeof(some_str)
    del some_str
    return size
