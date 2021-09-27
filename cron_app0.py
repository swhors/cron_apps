# cron_app0.py
# 2021/09/26
###################################################

#!/use/bin/env python
import time

from lib.jobschedule import JobSchedule
from datetime import datetime

from lib.jobschedule import JobSchedule
schedule = JobSchedule()


def fint_func():
    schedule.stop()
    time.sleep(5)

    print('Stop.....')


class JobSayHello:

    @classmethod
    def __repr__(cls) -> str:
        return f"<JobSayHello {id(cls)}>"


    @classmethod
    def __operate__(cls) -> bool:

        """
        Operate at scheduled time.
        """
        print(f'{datetime.now()} : Hello friends.')

        return True


    @classmethod
    def __init__(cls):

        """
        Initialization for job
        """
        cls._hour=0
        cls._minute=1
        cls._typeofjob='interval'



if __name__ == "__main__":

    from lib.signal_util import add_signal
    add_signal(fint_func)

    JobSayHello.__init__()
    schedule.add_job(JobSayHello.__operate__, JobSayHello._hour, JobSayHello._minute, JobSayHello._typeofjob)

    print(f'{__name__} +-----------------------------+')
    print(f'{__name__} +-                           -+')
    print(f'{__name__} +- Cron Application      ... -+')
    print(f'{__name__} +-                           -+')
    print(f'{__name__} +-----------------------------+')
     

    schedule.start()

