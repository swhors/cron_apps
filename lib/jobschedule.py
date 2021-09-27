# jobschedule.py
# 2021/09/26
###################################################
#!/use/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler


class JobSchedule():

    __jobs = []

    def __init__(self):
        self.__handle = BlockingScheduler()
        self.__jobs = []


    def len(self):
        return len(self.__jobs)


    def start(self):

        """
        Start scheduler
        """

        self.__handle.start()


    def stop(self):

        """
        Stop scheduler
        """

        #for job in self.__jobs:
        #    job.remove_job()
        self.__handle.shutdown()


    def add_job(self, execute, hour:int, minute:int, typeofjob:str='interval'):

        """
        add new job to cron scheduler

        :param execute: callback function
        :param hour: hour value
        :param minute: minute value
        :param typeofjobs: execution type => interval, cron
        """

        if typeofjob == 'interval':
            job = self.__handle.add_job(execute, typeofjob,
                                  minutes=minute,
                                  seconds=0)
        elif typeofjob == 'cron':
            job = self.__handle.add_job(execute,
                                  typeofjob,
                                  hour=hour,
                                  minute=minute)

        if job is not None:
            self.__jobs.append(job)


