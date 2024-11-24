"""
This script initializes and starts a worker from the `tasks` module.
It is designed to be used for debugging purposes with breakpoints.

Example usage:
    To run this script, ensure that the `tasks` module is available in your Python environment.
    You can set breakpoints in your IDE or use a debugger to step through the code.

    ```bash
    python debug_worker.py
    ```

    This will start the worker and allow you to debug its initialization and execution.
"""
import os
import sys
import logging
from logging.config import dictConfig
from src.celery import app

sys.path.append(os.getcwd())

log_level = logging.DEBUG
log_path = 'app.log'

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': log_level,
            'class': 'logging.FileHandler',
            'filename': log_path,
            'formatter': 'standard',
        },
        'console': {
            'level': log_level,
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': log_level,
            'propagate': True,
        },
    },
}

dictConfig(logging_config)

if __name__ == "__main__":
    # Initialize the worker from the app
    worker = app.Worker()   # If it doesn't work, set a breakpoint here!

    # Start the worker
    worker.start()  # and here :)
