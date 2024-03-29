"""External backend file meant to handle functions that would cause import errors"""


from importlib import import_module
from ast import literal_eval


module = None

def run(funcName: str, args: str):
    global module

    try:
        args = list(literal_eval(args))

        if funcName.startswith('tooltils'):
            if module is None:
                module = import_module('tooltils')
            
            if len(funcName.split('.')) == 2:
                return getattr(module, funcName.split('.')[1])(*args)
            else:
                return getattr(getattr(module, funcName.split('.')[1]), funcName.split('.')[2])(*args)
        else:
            for k, v in globals()['__builtins__'].items():
                if k == funcName:
                    return v(*args)
    except Exception:
        return None

