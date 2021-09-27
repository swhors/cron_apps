# job_sayhello.py
#
# 2021/09/26
###########################################
#!/usr/bin/env python

import json
from datetime import datetime, timedelta
from lib.job import Job

classname='JobSayHello'


class JobSayHello(Job):

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
    def __fint__(cls):
        pass


    @classmethod
    def __init__(cls) -> bool:

        """
        Initialization for job
        """
        cls._hour=0
        cls._minute=1

        return True

