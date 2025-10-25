from datetime import datetime
import logging
import os

# Directory for log files
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logger
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def logger_info(msg: str):
    """
    Log an INFO level message to file.
    """
    logging.info(msg)

def logger_error(msg: str):

    """
    Log an ERROR level message to file.
    """
    logging.error(msg)
