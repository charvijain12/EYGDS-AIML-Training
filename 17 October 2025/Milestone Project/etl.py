import pandas as pd

df = pd.read_csv('marks.csv')
df['TotalMarks'] = df[['Maths', 'Python', 'ML']].sum(axis=1)
df['Percentage'] = df['TotalMarks'] / 3
df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')
df.to_csv('student_results.csv', index=False)
