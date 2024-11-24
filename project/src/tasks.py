from __future__ import absolute_import, unicode_literals
from time import sleep
from src.celery import app
from src.log import app_logger


def get_queue_with_least_work(app):
    """
    Get the name of the queue with the least amount of work in a Celery application.

    Args:
        app (Celery): The Celery application instance.

    Returns:
        str: The name of the queue with the least amount of pending tasks.

    Example:
        >>> app = Celery('myapp', broker='pyamqp://guest@localhost//')
        >>> get_queue_with_least_work(app)
        'default'

    Raises:
        AttributeError: If the Celery application instance does not have task_queues configured.
    """
    try:
        if app.conf.task_queues:
            queue_names = [queue.name for queue in app.conf.task_queues]
            pending_task_counts = [len(app.control.inspect().active() or []) for _ in queue_names]
            
            if queue_names and pending_task_counts:
                # Combine queue names with their respective pending task counts.
                queue_with_task_counts = list(zip(queue_names, pending_task_counts))
                # Find the queue with the least number of pending tasks.
                queue_with_least_work = min(queue_with_task_counts, key=lambda x: x[1])
                
                if queue_with_least_work[0] == "main":
                    return min(queue_with_task_counts[1:], key=lambda x: x[1])[0]
                else:
                    return queue_with_least_work[0]
            else:
                raise AttributeError("No pending tasks found in any queue.")
        else:
            raise AttributeError("No task_queues configured in the Celery application.")
    except AttributeError as e:
        raise e


def text(text):
    """
    Perform a task that includes generating logging.

    Args:
        text (str): The text to include in the log message.
    """
    sleep(1)
    app_logger.info(f"{text}, sleep time {1}")

@app.task()
def current_process_proxy_queue(_):
    """
    Log information about the worker processing tasks from a specific queue.

    Args:
        _: A placeholder parameter.
    """
    queue_name = app.current_task.request.delivery_info.get('routing_key', 'unknown')
    text(f"{_} - {queue_name} - ")
    app_logger.info(f"Worker for queue '{queue_name}' is processing tasks from its queue")

@app.task()
def multi_runner():
    """
    Perform multiple tasks in different queues for a specified number of iterations.
    """
    queues = list(app.conf.task_queues)
    queues = [queue.name for queue in queues if queue.name != "main"]
    app_logger.info(f"cached queues : {queues}")
    for _ in range(10):
        for queue in queues:
            app_logger.info(f"Before apply_async: {_} {queue}")
            result = current_process_proxy_queue.apply_async((str(_),), queue=queue)
            app_logger.info(f"After apply_async: {_} {queue}, result: {result}")
        x = get_queue_with_least_work(app)
        print(f"******************************** {x} *****************************************")

@app.task(name="tasks.single_runner")
def single_runner():
    """
    Perform tasks in a single queue for a specified number of iterations.
    """
    queues = list(app.conf.task_queues)
    queues = [queue.name for queue in queues if queue.name != "main"] if len(queues) > 1 else [queues[0].name]
    app_logger.info(f"cached queues : {queues}")
    for _ in range(2):
        queue = queues[0]
        app_logger.info(f"Before apply_async: {_} {queue}")
        result = current_process_proxy_queue.apply_async((str(_),), queue=queue)
        app_logger.info(f"After apply_async: {_} {queue}, result: {result}")
