from fastapi import FastAPI, UploadFile
import shutil
import pika

app = FastAPI()

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='marks_queue')

@app.post("/upload_marks")
async def upload_marks(file: UploadFile):
    file_path = f"uploads/{file.filename}"  # Save uploaded file
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Send file path to RabbitMQ
    channel.basic_publish(
        exchange='',
        routing_key='marks_queue',
        body=file_path
    )

    return {"message": f"File {file.filename} uploaded and queued for processing"}