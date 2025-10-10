import pika
import json
import time
#1. connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#2. ensure the queue exists
channel.queue_declare(queue="student_tasks")

#3. define message handling func
def callback(ch, method, properties, body):
    task=json.loads(body)
    print("Received:",task)
    #simulate some work
    time.sleep(2)
    print("Task processed for student:",task["student_id"])

#4 start consuming messages from the queue
channel.basic_consume(queue="student_tasks", on_message_callback=callback, auto_ack=True)

print("waiting for message. Press CTRL+C to exit")
channel.start_consuming()