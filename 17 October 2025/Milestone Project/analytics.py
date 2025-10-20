import pandas as pd
import os

# -------------------------
# File paths
# -------------------------
parent_folder = os.path.abspath("..")
students_file = os.path.join(parent_folder, "students.csv")      # original student data
results_file = os.path.join(parent_folder, "Task_7", "student_results.csv")  # processed marks from Task_7

# -------------------------
# Read CSVs
# -------------------------
students_df = pd.read_csv(students_file)
results_df = pd.read_csv(results_file)

# -------------------------
# Merge students + results
# -------------------------
merged_df = pd.merge(students_df, results_df, on="StudentID", how="inner")

# -------------------------
# Top 3 students by Percentage
# -------------------------
top3 = merged_df.sort_values(by="Percentage", ascending=False).head(3)
print("Top 3 students by Percentage:")
print(top3[['StudentID','Name','Course','Percentage']])

# -------------------------
# Average marks per course
# -------------------------
avg_marks = merged_df.groupby("Course")[['Maths','Python','ML','TotalMarks','Percentage']].mean()
print("\nAverage marks per Course:")
print(avg_marks)

# -------------------------
# Optional: save analytics report
# -------------------------
output_file = os.path.join(parent_folder, "Task_7", "analytics_report.csv")
merged_df.to_csv(output_file, index=False)
print(f"\nMerged data saved to {output_file}")