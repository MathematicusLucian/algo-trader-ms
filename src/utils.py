import sys

def is_arg(arg_str):
    for i, arg in enumerate(sys.argv):
        if arg==arg_str: 
            return True
    return False