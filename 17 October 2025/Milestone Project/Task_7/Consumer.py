import pika
import pandas as pd
import logging
import os
from datetime import datetime

# -------------------------
# Logging setup
# -------------------------
parent_folder = os.path.abspath("..")
log_folder = os.path.join(parent_folder, "task_5_logs")
log_file = os.path.join(log_folder, "consumer.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Consumer started")

# -------------------------
# RabbitMQ setup
# -------------------------
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='marks_queue')

# Function to process CSV

def process_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        # Compute TotalMarks, Percentage, Result
        df['TotalMarks'] = df[['Maths', 'Python', 'ML']].sum(axis=1)
        df['Percentage'] = df['TotalMarks'] / 3
        df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

        df['TotalMarks'] = df['TotalMarks'].round(2)
        df['Percentage'] = df['Percentage'].round(2)

        # Save processed results in Task_7 folder
        task7_folder = os.getcwd()  # current folder = Task_7
        processed_file = os.path.join(task7_folder, "student_results.csv")

        if os.path.exists(processed_file):
            results_df = pd.read_csv(processed_file)
            # Merge new data (overwrite existing StudentID rows)
            results_df = results_df[~results_df['StudentID'].isin(df['StudentID'])]
            results_df = pd.concat([results_df, df], ignore_index=True)
        else:
            results_df = df

        results_df.to_csv(processed_file, index=False)

        logging.info(f"Processed {file_path} → saved to {processed_file}")
        print(f"Processed {file_path} → saved to {processed_file}")

    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
        print(f"Error processing {file_path}: {e}")

# RabbitMQ callback

def callback(ch, method, properties, body):
    file_path = body.decode()
    logging.info(f"Received {file_path} from queue")
    process_csv(file_path)

# Start consuming messages
channel.basic_consume(queue='marks_queue', on_message_callback=callback, auto_ack=True)

logging.info("Consumer waiting for messages. Press CTRL+C to exit.")
print("Consumer waiting for messages. Press CTRL+C to exit.")
channel.start_consuming()