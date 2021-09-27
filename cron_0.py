from apscheduler.schedulers.blocking import BlockingScheduler

def execute():
    print('hello')

if __name__=="__main__":
    __handle = BlockingScheduler()
    __handle.add_job(execute, 'interval',
                     minutes=1,
                     seconds=0)


    __handle.start()

