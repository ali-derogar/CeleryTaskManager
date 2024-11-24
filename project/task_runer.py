import pytest
from src.celery import app

def test_single_runner():
    result = app.send_task("tasks.single_runner",queue="boom")
    assert result.get(timeout=10*60) is not None

def test_multi_runner():
    result = app.send_task("tasks.single_runner",queue="main")
    assert result.get(timeout=10*60) is not None

if __name__ == "__main__":
    pytest.main([__file__])
