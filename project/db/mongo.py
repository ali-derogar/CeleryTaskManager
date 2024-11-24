from pymongo import MongoClient
from src.exceptions import DbExceptions
from config import settings

def mongo_connect():
    """
    Establish a connection to a MongoDB database using the URI specified in the application settings.

    This function attempts to create a connection to a MongoDB database using the URI defined
    in the application settings. If the connection fails, it raises a `DbExceptions` exception.

    Raises:
        DbExceptions: If the connection to the MongoDB database cannot be established.
    """
    try:
        client = MongoClient(settings.MONGODB_URI)
    except:
        raise DbExceptions
