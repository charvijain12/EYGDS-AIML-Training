import pandas as pd
import logging
import os
from datetime import datetime


csv_file = "../marks.csv"
log_file = "../task_5_logs/etl.log"
output_folder = "."

# Setup logging

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Task 6 ETL started")
print("Task 6 ETL started")

try:
    # Read CSV
    df = pd.read_csv(csv_file)

    # ETL: TotalMarks, Percentage, Result
    df['TotalMarks'] = df[['Maths','Python','ML']].sum(axis=1)
    df['Percentage'] = df['TotalMarks'] / 3
    df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

    # Timestamped output file
    today = datetime.now().strftime("%Y%m%d")
    output_file = os.path.join(output_folder, f"daily_report_{today}.csv")
    df.to_csv(output_file, index=False)

    logging.info(f"ETL completed successfully, saved to {output_file}")
    print(f"ETL completed successfully, saved to {output_file}")

except Exception as e:
    logging.error(f"ETL failed: {e}")
    print(f"ETL failed: {e}")