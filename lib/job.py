# job.py
#
# 2021/09/26
###########################################
#!/usr/bin/env python

class JobMeta(type):
    def hour(cls):
        return cls._hour 
    
        
    @property
    def minute(cls):
        return cls._minute
    

    @property
    def typeofjob(cls):
        return cls._typeofjob


class Job(metaclass=JobMeta):

    _hour = 0
    _minute = -1
    _typeofjob = 'interval'

    @classmethod
    def __reps__(cls) -> str:
        return f"<Job {id(cls)}"


    @classmethod
    def execute(cls) -> bool:
        return cls.__operate__()


    @classmethod
    def init(cls) -> bool:
        return cls.__init__()

    
    @classmethod
    def fint(cls):
        cls.__fint__()


    @classmethod
    def __operate__(cls) -> bool:
        return True


    @classmethod
    def __init__(cls) -> bool:
        return True


    @classmethod
    def __fint__(cls):
        pass
