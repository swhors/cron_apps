# cron_app.py
# 2021/09/26
###################################################
#!/use/bin/env python
import time

from lib.jobschedule import JobSchedule
import jobs as jobs

schedule = JobSchedule()

classes = jobs.get_all_class(jobs.__path__[0])


def fint_func():
    schedule.stop()
    time.sleep(5)
    jobs.fint_all_class()
    print('Stop....')


if __name__ == "__main__":

    from lib.signal_util import add_signal
    add_signal(fint_func)

    for cls in classes:
        schedule.add_job(cls.execute, cls.hour, cls.minute, cls.typeofjob)

    print(f'{__name__} +-----------------------------+')
    print(f'{__name__} +-                           -+')
    print(f'{__name__} +- Cron Application      ... -+')
    print(f'{__name__} +-                           -+')
    print(f'{__name__} +-----------------------------+')
     

    schedule.start()

