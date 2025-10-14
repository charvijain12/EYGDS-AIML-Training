import multiprocessing
import time

def producer(a):
    for i in range(10):
        message = f"Message {i} from Producer"
        print(f"Producer is sending: {message}")
        a.put(message)
        time.sleep(1)
    a.put("EXIT") # Signal for the consumer to stop the process