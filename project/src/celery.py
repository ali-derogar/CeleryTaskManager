from __future__ import absolute_import, unicode_literals
from celery import Celery
from db.mongo import mongo_connect
from config.config_file import settings

"""
This script initializes a Celery app with default configuration settings.

It connects to a MongoDB database and configures the Celery app using the
default configuration specified in 'src.celeryconfig'.

Usage:
    Ensure that the MongoDB connection is established and the Celery app is
    properly configured before running this script.
"""

mongo_connect()
app = Celery('src')
if settings.QUEUES_NAMES:
    default_config = 'src.celeryconfig'
    app.config_from_object(default_config)
else:
    app.conf.update(
        broker_connection_retry_on_startup=True,
    )
