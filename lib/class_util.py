#  class_util.py
#
#  2021/09/26
############################################

#import os, glob
from importlib.util import spec_from_file_location, module_from_spec


def class_from_file(file_path)->[]:

    """
    load python class from file

    :param file_path: str
    """
    
    spec = spec_from_file_location('classname', file_path)
    print(spec, type(spec))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    cls = getattr(module, module.classname)
    return cls


