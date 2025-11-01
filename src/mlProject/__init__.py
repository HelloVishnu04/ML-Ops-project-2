import os
import sys
import logging

logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")    
os.makedirs(log_dir, exist_ok=True)

# Create logger
logger = logging.getLogger("mlproject")
logger.setLevel(logging.INFO)

# Create formatters
formatter = logging.Formatter(logging_str)

# Create handlers
file_handler = logging.FileHandler(log_filepath)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)