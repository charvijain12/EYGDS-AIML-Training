import logging

#logging configuration
logging.basicConfig(
    filename='app.log', #log file name
    level=logging.ERROR,  #log levels
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

#example logsss
logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Low memory warning")
logging.error("File not found error")
logging.critical("Critical system failure")