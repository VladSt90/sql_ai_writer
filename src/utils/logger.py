import logging
import colorlog

# Create a logger object
logger = logging.getLogger("main_logger")
logger.setLevel(logging.DEBUG)  # Set the minimum log level

# Define log format
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Create a stream handler (or you can use FileHandler if you want to log to a file)
stream_handler = logging.StreamHandler()

# Set formatter to colorlog
formatter = colorlog.ColoredFormatter("%(log_color)s" + log_format)

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
