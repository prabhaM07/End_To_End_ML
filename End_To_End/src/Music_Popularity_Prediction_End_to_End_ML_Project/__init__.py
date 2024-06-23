import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s : %(module)s : %(message)s]"
"""
asctime = used to set the current time like time stamp
levelname = used to provide the level of the folder like root folder
module = module name in which module we r running the code
message = what king of log message you want to set 

"""
log_dir = "logs" # log folder

log_filepath = os.path.join(log_dir, "running_log.log") # creating log file into log folder

os.makedirs(log_dir,exist_ok= True)
logging.basicConfig(
    level = logging.INFO,
    format= logging_str,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Music_popularity_prediction_Logger")

"""
The FileHandler directs log messages to a file. 
The StreamHandler directs log messages to an output stream, such as sys.stdout. like console.
"""