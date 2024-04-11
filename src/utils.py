import sys
import os
from dotenv import main
main.load_dotenv(main.find_dotenv())

def is_arg(arg_str: str) -> bool:
    for i, arg in enumerate(sys.argv):
        if arg==arg_str: 
            return True
    return False

def get_envar(envar_name: str) -> str:
    return os.environ.get(envar_name)