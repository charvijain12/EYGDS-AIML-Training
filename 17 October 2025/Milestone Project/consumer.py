import pandas as pd
import queue
import time
import logging
import os

# Setup logs in task_5_logs
log_folder = "task_5_logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logging.basicConfig(
    filename=os.path.join(log_folder, "etl.log"),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Queue setup
csv_queue = queue.Queue()
csv_queue.put("marks.csv")

while not csv_queue.empty():
    csv_file = csv_queue.get()
    logging.info(f"[Consumer] Started processing {csv_file}")
    print(f"[Consumer] Processing {csv_file}")

    try:
        df = pd.read_csv(csv_file)
        df['TotalMarks'] = df[['Maths','Python','ML']].sum(axis=1)
        df['Percentage'] = df['TotalMarks'] / 3
        df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

        output_file = "student_results.csv"
        df.to_csv(output_file, index=False)

        logging.info(f"[Consumer] Finished processing {csv_file}, saved to {output_file}")
        print(f"[Consumer] Saved results to {output_file}")

    except Exception as e:
        logging.error(f"[Consumer] Error processing {csv_file}: {e}")
        print(f"[Consumer] Error: {e}")

    time.sleep(1)