import json

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#2. ensure the queue exists
channel.queue_declare(queue="student_tasks")

task={
    "student_id":1,
    "action":"generate_certificate",
    "email":"abc@example.com"
}

channel.basic_publish(
    exchange='',
    routing_key='student_tasks',
    body=json.dumps(task)
)

print("Task sent to queue:",task)

connection.close

