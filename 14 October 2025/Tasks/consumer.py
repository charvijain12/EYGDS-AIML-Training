import multiprocessing
import time

def consumer(a):
    while True:
        message = a.get()
        if message == "EXIT":
            print("Consumer has received the EXIT signal. Exiting.")
            break
        print(f"Consumer received: {message}")
        time.sleep(1)