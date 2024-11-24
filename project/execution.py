from src import *
import threading
import subprocess
from src.celeryconfig import queues
import shlex

def start_celery_worker(worker_name, queue):
    """
    Start a Celery worker for a specific queue.

    Args:
        worker_name (str): The name of the Celery worker.
        queue (str): The name of the queue for the worker.
    """
    # Ensure that both worker_name and queue are strings
    if not isinstance(worker_name, str):
        worker_name = str(worker_name)
    
    if not isinstance(queue, str):
        queue = str(queue)

    # Enclose worker_name and queue in double quotes and properly escape them
    worker_name = shlex.quote(worker_name)
    queue = shlex.quote(queue)

    command = f'celery -A src worker -n {worker_name} -Q {queue}'
    subprocess.run(command, shell=True)

def run_workers(queues):
    """
    Start Celery workers for multiple queues using multiple threads.
    """
    threads = []
    for index, queue in enumerate(queues):
        queue_name = shlex.quote(queue.name)
        temp_name = f"{1+index}-{queue_name}-"
        worker_name = f'worker{temp_name}@%h'
        # Create a thread for each worker setup and execution
        worker_thread = threading.Thread(target=start_celery_worker, args=(worker_name, queue.name))
        worker_thread.start()
        threads.append(worker_thread)

    # Wait for all worker threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_workers(queues)
