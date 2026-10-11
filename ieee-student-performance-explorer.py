import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")
df = df.drop_duplicates()    

scores = ["quiz_score", "assignment_score", "exam_score"]
for col in scores:
    df[col] = pd.to_numeric(df[col], errors="coerce") 
    df[col] = df[col].fillna(df[col].mean())          

df["final_mark"] = df["quiz_score"] * 0.2 + df["assignment_score"] * 0.3 + df["exam_score"] * 0.5

marks = df["final_mark"].to_numpy()     
mean = np.mean(marks)
std = np.std(marks)
median = np.median(marks)
low = np.min(marks)
high = np.max(marks)

# 3. FILTER AND GROUP
high_exam = df[df["exam_score"] >= 80]
by_subject = df.groupby("subject")["final_mark"].mean().sort_values(ascending=False)
by_section = df.groupby("section")["final_mark"].mean()
top_students = df.groupby("name")["final_mark"].mean().sort_values(ascending=False).head(3)

print("=" * 40)
print("   STUDENT PERFORMANCE REPORT")
print("=" * 40)
print(f"Records after cleaning : {len(df)}")
print(f"Class Mean             : {mean:.2f}")
print(f"Standard Deviation     : {std:.2f}")
print(f"Median                 : {median:.2f}")
print(f"Minimum Number         : {low:.2f} ")
print(f"Maximum Number         : {high:.2f}")    

print("Subject Ranking Average Final Marks:")
print("-"*50)
for rank, (subject, avg) in enumerate(by_subject.items(), start=1):
    print(f" {rank}. {subject:<18} {avg:.2f}")
print(f"Strongest subject: {by_subject.index[0]}")
print(f"Weakest subject  : {by_subject.index[-1]}")
print("-"*50)

print("-"*20)
print("Section Averages:")
print(by_section.round(2).to_string())
print("-"*20)

print(f"Students with exam score >= 80: {high_exam['name'].nunique()}")
print(", ".join(sorted(high_exam["name"].unique())))

print("\nTop 3 Students:")
for rank, (name, avg) in enumerate(top_students.items(), start=1):
    print(f"  {rank}. {name:<8} {avg:.2f}")
print("=" * 40)
