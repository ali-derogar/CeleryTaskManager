from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Settings(BaseSettings):
    """
    Application settings and configurations.

    This class defines settings and configurations for various aspects of the application,
    including proxy, database, RedBeat, and Redis for Celery. These settings are loaded
    from environment variables defined in the '.env' file.

    Attributes:
        MONGODB_URI (str): MongoDB connection URI.
        MONGODB_NAME (str): MongoDB database name.
        REDBEAT_REDIS_URL (str): URL for RedBeat's Redis broker.
        REDIS_BROKER (str): Redis broker URL for Celery.
        REDIS_BACKEND (str): Redis backend URL for Celery.

    """

    MONGODB_URI: str
    MONGODB_NAME: str
    REDBEAT_REDIS_URL: str
    REDIS_BROKER: str
    REDIS_BACKEND: str
    QUEUES_NAMES: list

    class Config:
        env_file = "project/config/.env"

settings = Settings()
