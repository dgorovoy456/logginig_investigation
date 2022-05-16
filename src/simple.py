import logging
import sys
from simple2 import CustomFormatter

formater = CustomFormatter()
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
root_logger = logging.getLogger('My_app')
root_logger.setLevel(level='DEBUG')
fileHandler = logging.FileHandler(filename="logs.log", mode='w')
fileHandler.setFormatter(logFormatter)
root_logger.addHandler(fileHandler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formater)
root_logger.addHandler(console_handler)

root_logger.debug('This is debug level')
# logging.debug('This is debug level')
root_logger.error('This is error level')
# logging.error('This is error level')
root_logger.warning('This is warning level')
# logging.warning('This is warning level')
root_logger.info('This is info level')
# logging.info('This is info level')
