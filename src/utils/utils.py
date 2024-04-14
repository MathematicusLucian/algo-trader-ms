import sys
import os
from datetime import datetime
import pytz
from dotenv import main
main.load_dotenv(main.find_dotenv())

def is_arg(arg_str: str) -> bool:
    for i, arg in enumerate(sys.argv):
        if arg==arg_str: 
            return True
    return False

def get_envar(envar_name: str) -> str:
    return os.environ.get(envar_name)

def get_root_dir():
    return os.path.abspath(os.curdir)

def get_datetime_now(format=None):
    if format == "timestamp":
        return datetime.now().timestamp()
    elif format == "iso":
        today = datetime.now()
        iso_date = today.isoformat()
        iso_date_with_hash = datetime.now().isoformat('#')
        iso_date_with_space = today.isoformat()
        today_datestring = datetime.today()
        aware_us_central = datetime.now(pytz.timezone('US/Central'))
        iso_date = aware_us_central.isoformat()
    else:
        return datetime.now()