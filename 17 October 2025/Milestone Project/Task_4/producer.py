import queue

# Create a queue
csv_queue = queue.Queue()

# CSV files to process
csv_files = ["marks.csv"]  # You can add more CSVs if needed

# Push CSV paths into queue
for file in csv_files:
    csv_queue.put(file)
    print(f"[Producer] Added {file} to queue")