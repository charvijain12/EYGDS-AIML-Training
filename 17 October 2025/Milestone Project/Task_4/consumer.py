import pandas as pd
import queue
import time
import logging
import os

                            # -------------------------
                                     # Paths (absolute)
                            # -------------------------
csv_file = "../marks.csv"
log_file = "../task_5_logs/etl.log"
output_file = "student_results.csv"

                            # -------------------------
                                 # Setup logging
                            # -------------------------
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Consumer started")

                        # -------------------------
                                # Setup queue
                        # -------------------------
csv_queue = queue.Queue()
csv_queue.put(csv_file)
logging.info(f"[Producer] Added {csv_file} to queue")
print(f"[Producer] Added {csv_file} to queue")

                                # -------------------------
                                    # Process queue
                                # -------------------------
while not csv_queue.empty():
    csv_path = csv_queue.get()
    logging.info(f"[Consumer] Started processing {csv_path}")
    print(f"[Consumer] Processing {csv_path}")

    try:
        # Read CSV
        df = pd.read_csv(csv_path)

        # ETL: TotalMarks, Percentage, Result
        df['TotalMarks'] = df[['Maths','Python','ML']].sum(axis=1)
        df['Percentage'] = df['TotalMarks'] / 3
        df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

        # Save processed results
        df.to_csv(output_file, index=False)

        logging.info(f"[Consumer] Finished processing {csv_path}, saved to {output_file}")
        print(f"[Consumer] Saved results to {output_file}")

    except Exception as e:
        logging.error(f"[Consumer] Error processing {csv_path}: {e}")
        print(f"[Consumer] Error: {e}")

    time.sleep(1)