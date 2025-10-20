from fastapi import FastAPI, UploadFile
import shutil
import os
import pika
import logging

app = FastAPI()

# Use the existing task_5_logs folder in parent folder
parent_folder = os.path.abspath("..")              # parent directory
log_folder = os.path.join(parent_folder, "task_5_logs")  # existing folder
log_file = os.path.join(log_folder, "producer7.log")      # new log file name

# Setup logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Producer started")
# -------------------------
# Setup RabbitMQ connection
# -------------------------
try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='marks_queue')
    logging.info("Connected to RabbitMQ successfully")
except Exception as e:
    logging.error(f"Failed to connect to RabbitMQ: {e}")
    raise e

# -------------------------
# Endpoint to upload CSV
# -------------------------
@app.post("/upload_marks")
async def upload_marks(file: UploadFile):
    try:
        # Create uploads folder if not exists
        upload_folder = "uploads"
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # Save uploaded file
        file_path = os.path.join(upload_folder, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Send file path to RabbitMQ
        channel.basic_publish(
            exchange='',
            routing_key='marks_queue',
            body=file_path
        )

        logging.info(f"Uploaded and queued file: {file_path}")
        return {"message": f"File {file.filename} uploaded and queued for processing"}

    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return {"error": str(e)}