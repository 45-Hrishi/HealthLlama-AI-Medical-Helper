import logging
from datetime import datetime
import os

# create the folder to store the logs
LOG_PATH = os.path.join(os.getcwd(),'LOGS')
os.makedirs(LOG_PATH,exist_ok=True)

# create the file path for files present inside logs
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)


logger = logging.basicConfig(filename=LOG_FILE_PATH,level=logging.INFO,format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s')
