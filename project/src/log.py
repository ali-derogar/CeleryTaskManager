import logging

app_logger = logging.getLogger('celery.worker')

"""
Initialize and configure the application logger for the Celery worker.

This code sets up the logger for the Celery worker, configures the log level, and
attaches a file handler to log messages to a file named 'app.log'.

Usage:
    Ensure this code is called to configure the logger for the Celery worker.
"""

# Set the log level (INFO, DEBUG, etc.)
app_logger.setLevel(logging.INFO)

# Create a file handler and set its log level
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
app_logger.addHandler(file_handler)