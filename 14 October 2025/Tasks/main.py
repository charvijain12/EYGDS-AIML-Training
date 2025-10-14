import multiprocessing
from producer import producer
from consumer import consumer

if __name__ == "__main__":
    shared_queue = multiprocessing.Queue()

    # Creating producer and consumer processes
    producer_process = multiprocessing.Process(target=producer,args=(shared_queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(shared_queue,))

    # starting the processes
    producer_process.start()
    consumer_process.start()

    #waiting for processes to finish
    producer_process.join()
    consumer_process.join()

    print("Producer and Consumer processes are finished.")