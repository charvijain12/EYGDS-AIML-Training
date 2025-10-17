from queue import Queue

q = Queue()

def producer():
    q.put('marks.csv')
    print("CSV path pushed to queue")

def consumer():
    csv_path = q.get()
    df = pd.read_csv(csv_path)
    # Perform ETL same as above
    df['TotalMarks'] = df[['Maths', 'Python', 'ML']].sum(axis=1)
    df['Percentage'] = df['TotalMarks'] / 3
    df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')
    df.to_csv('student_results_processed.csv', index=False)
    print("ETL complete and saved")

producer()
consumer()
