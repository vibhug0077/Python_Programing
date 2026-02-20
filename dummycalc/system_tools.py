"""Helpers built on common standard library modules."""

import os
import sys
import time


def python_info():
    return {
        "version": sys.version,
        "executable": sys.executable,
        "cwd": os.getcwd(),
        "path_entries": len(sys.path),
    }


def cli_args():
    return sys.argv[1:]


def list_current_dir():
    return os.listdir(os.getcwd())


def current_time():
    return time.ctime()


def now_epoch():
    return time.time()
