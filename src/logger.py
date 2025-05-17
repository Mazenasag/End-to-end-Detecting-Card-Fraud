import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"
logs_path = "logs"
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] File Name: %(filename)s - Line No:  %(lineno)d - %(levelname)s - %(message)s',
    level=logging.INFO,
)


logging.info("This is an info message.")
