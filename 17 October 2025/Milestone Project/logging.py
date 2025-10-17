import logging
import time

logging.basicConfig(filename='project.log', level=logging.INFO)

try:
    start = time.time()
    # ETL code here
    logging.info("ETL started")
    # ETL process
    logging.info("ETL finished successfully in %s seconds", time.time() - start)
except Exception as e:
    logging.error("Error in ETL: %s", e)
