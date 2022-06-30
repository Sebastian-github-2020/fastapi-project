import logging

_LOG_FORMATE = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=_LOG_FORMATE)

logging.error("xxx")



