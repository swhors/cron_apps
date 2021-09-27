#  __init__.py
#
#  2021/09/26
############################################

import os, glob
from lib.class_util import class_from_file

classes = []

def get_all_class(path:str):
    """
    Initialize all classes

    :param path: current path for jobs
    """

    global classes

    for file in glob.glob(path+"/job_*.py"):
        print(file)
        cls = class_from_file(file)
        cls.init()
        print(f'loaded jobs = {cls.__name__}')
        classes.append(cls)

    return classes


def fint_all_class():
    """
    Finalize all classes
    """
    for cls in classes:
        cls.fint()

