from config import settings
from kombu import Exchange, Queue

# Load configuration settings and define Celery queues
proxy_list = settings.QUEUES_NAMES
queues = [Queue(name=i, exchange=Exchange(i), routing_key=i) for i in proxy_list]

# Convert the list of queues to a tuple
task_queues = tuple(queues)

# Specify the number of worker processes (concurrency)
worker_concurrency = 1  # Assuming you want to set it as a single integer

# Use Redis as the broker and result backend
broker_url = settings.REDIS_BROKER
result_backend = settings.REDIS_BACKEND

# Specify the module(s) that contain Celery tasks
include = ['src.tasks']

# You may specify a result_expires setting to control the time results are kept in the backend
result_expires = 3600  # Results expire after 1 hour (adjust this value as needed)

# Use JSON as the task and result serializer
task_serializer = 'json'
result_serializer = 'json'

# Specify accepted content types
accept_content = ['json']

# Enable UTC for scheduling tasks
enable_utc = True

# Set the Celery timezone to 'Asia/Tehran'
timezone = 'Asia/Tehran'

# Set broker_connection_retry setting to True on startup
broker_connection_retry = True
broker_connection_retry_on_startup = True
