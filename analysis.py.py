import pandas as pd

#load csv file 
df = pd.read_csv("StudentsPerformance.csv")

# 1st 5 rows of the dataset
print(df.head())

print("\n--------------------------------")
# Dataset size
print("shape:", df.shape)

print("\n--------------------------------")

# column Names of the dataset
print("columns", df.columns)

print("\n--------------------------------")

#Dataset information
print("Dataset Information:")
print(df.info())

#=========================
# step 3 : Average Marks
#=========================

print("\n--------------------------------")
print("Average Marks:")

math_avg = df['math score'].mean()
reading_avg = df['reading score'].mean()
writing_avg = df['writing score'].mean()

print("Average Math Score:", math_avg)
print("Average Reading Score:", reading_avg)
print("Average Writing Score:", writing_avg)

overall_avg = df[['math score', 'reading score', 'writing score']].mean().mean()

print("Overall Average Score:",  overall_avg)

#=========================
# step 4 : Highest & Lowest Marks.
#=========================

print("\n---------------------------------")
print("Highest & Lowest Marks:")
print("\n---------------------------------")

# Highest Marks
math_highest = df["math score"].max()
reading_highest = df["reading score"].max()
writing_highest = df["writing score"].max()

# Lowest Marks
math_lowest = df["math score"].min()
reading_lowest = df["reading score"].min()
writing_lowest = df["writing score"].min()

print("Highest Math Score:", math_highest)
print("Highest Reading Score:", reading_highest)
print("Highest Writing Score:", writing_highest)

print("Lowest Math Score:", math_lowest)
print("Lowest Reading Score:", reading_lowest)
print("Lowest Writing Score:", writing_lowest)

#=========================
# step 5 : TOPPER DETAILS
#=========================

print("\n---------------------------------")
print("Topper Details:")
print("\n---------------------------------")

# Total marks of each student
df["Total Marks"] = (
    df["math score"] + df["reading score"] + df["writing score"]
    )
# Highest total marks and topper details
highest_total = df['Total Marks'].max()
print("Highest Total Marks:", highest_total)

#Topper details
topper = df[df["Total Marks"] == highest_total]

print(topper)

#=========================
# step 6 : Pass/Fail Analysis
#=========================

print("\n---------------------------------")
print("Pass/Fail Analysis:")
print("\n---------------------------------")

#Percentage of students passed in each subject
df["percentage"] = (df["Total Marks"] / 300) *100

#Pass and Fail Criteria
pass_students = df[df["percentage"] >= 35]
fail_students = df[df["percentage"] < 35]

print("Total Students:", len(df))
print("Pass Students:", len(pass_students))
print("Fail Students:", len(fail_students))

#Pass Percentage
pass_percentage = (len(pass_students) / len(df)) * 100

print("Pass Percentage:", round(pass_percentage, 2), "%")

#=========================
# step 7  : Grade Analysis
#=========================

print("\n---------------------------------")
print("Grade Analysis:")
print("\n---------------------------------")

# Grade Criteria/Function
def Calculate_Grade(percentage):
    if percentage >= 95:
        return "A+"
    elif percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B+"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"
    
# Grade Column
df["Grade"] = df["percentage"].apply(Calculate_Grade)

# Grade Count
grade_count = df["Grade"].value_counts()

print(grade_count)

#===============================
# step 8  : Data Visualization
#===============================

import matplotlib.pyplot as plt

print("\n----------------------------")
print("Data Visualization:")
print("Grade Bar Chart")
print("\n----------------------------")

# Bar Chart 
grade_count.plot(kind="bar")

plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()

print("\n----------------------------")
print("Saving Final Result...")

# Save updated dataset
df.to_csv("Student_Result_Analysis.csv", index=False)

print("File Saved Successfully!")