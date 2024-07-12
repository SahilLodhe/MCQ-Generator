import logging
import os
from datetime import datetime

# Define log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
log_path = os.path.join(os.getcwd(), "logs")  # Make a folder named "logs" in the current working directory
os.makedirs(log_path, exist_ok=True)  # Create the directory if it doesn't exist

# Define the full log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,  # Use LOG_FILEPATH here
    format="[%(asctime)s] %(lineno)d %(name)s - %(message)s"
)

# Example log message
logging.info("Logging setup complete.")
