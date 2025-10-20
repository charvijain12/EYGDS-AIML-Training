import pika
import pandas as pd
import logging
import os
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData

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
# Database setup (MySQL)
# -------------------------
db_user = "your_user"
db_pass = "your_password"
db_host = "localhost"
db_name = "your_database"

engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}")
metadata = MetaData(bind=engine)

students_table = Table("students", metadata, autoload_with=engine)
marks_table = Table("marks", metadata, autoload_with=engine)

# -------------------------
# RabbitMQ setup
# -------------------------
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='marks_queue')

# -------------------------
# Process CSV and update DB
# -------------------------
def process_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        df['TotalMarks'] = df[['Maths','Python','ML']].sum(axis=1)
        df['Percentage'] = df['TotalMarks'] / 3
        df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

        # Insert or update marks table
        for _, row in df.iterrows():
            stmt = marks_table.insert().values(
                StudentID=row['StudentID'],
                Maths=row['Maths'],
                Python=row['Python'],
                ML=row['ML'],
                TotalMarks=row['TotalMarks'],
                Percentage=row['Percentage'],
                Result=row['Result']
            )
            # For MySQL, use 'ON DUPLICATE KEY UPDATE' to update existing records
            stmt = stmt.on_duplicate_key_update(
                Maths=row['Maths'],
                Python=row['Python'],
                ML=row['ML'],
                TotalMarks=row['TotalMarks'],
                Percentage=row['Percentage'],
                Result=row['Result']
            )
            engine.execute(stmt)

        # Save processed CSV (optional)
        today = datetime.now().strftime("%Y%m%d")
        output_file = os.path.join(os.getcwd(), f"processed_{today}_{os.path.basename(file_path)}")
        df.to_csv(output_file, index=False)

        logging.info(f"Processed {file_path} → DB updated and saved {output_file}")
        print(f"Processed {file_path} → DB updated and saved {output_file}")

    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
        print(f"Error processing {file_path}: {e}")

# -------------------------
# RabbitMQ callback
# -------------------------
def callback(ch, method, properties, body):
    file_path = body.decode()
    logging.info(f"Received {file_path} from queue")
    process_csv(file_path)

channel.basic_consume(queue='marks_queue', on_message_callback=callback, auto_ack=True)

logging.info("Consumer waiting for messages. Press CTRL+C to exit.")
print("Consumer waiting for messages. Press CTRL+C to exit.")
channel.start_consuming()