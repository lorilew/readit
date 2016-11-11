import time
from django_rq.decorators import job
import django_rq
import rq

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@job
def printsomething(the_thing):
    time.sleep(2)
    print("Look at me I'm printing something!...{}".format(the_thing))
    1 / 0


# def my_handler(job, exc_type, exc_value, traceback):
#     job.meta.setdefault('failures', 0)
#     job.meta['failures'] += 1
#
#     if job.meta['failures'] >= 3:
#         logger.warn('job:{} has failed {} times - moving to failed queue'.format(job.id, job.meta['failures']))
#         job.save()
#         return True
#
#     logger.warn('job:{} has failed {} times - retrying'.format(job.id, job.meta['failures']))
#
#     django_rq.enqueue(job, timeout=job.timeout)
#     return False
#
#
# with rq.Connection():
#     q = rq.Queue
#     worker = rq.Worker
#     worker.push_exc_handler(my_handler)
#     worker.work()