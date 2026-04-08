# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_data.csv")

# Preview
print("Dataset Preview:")
print(df.head())

# Info
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic stats
print("\nStatistical Summary:")
print(df.describe())

# Highest salary employee
top_emp = df.loc[df['Salary'].idxmax()]
print("\nTop Salary Employee:")
print(top_emp)

# Department-wise average salary
dept_avg = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(dept_avg)

# ---------------- GRAPHS ----------------

# 1. Bar Chart - Dept Avg Salary
plt.figure()
dept_avg.plot(kind='bar')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.savefig("dept_salary.png")
plt.show()

# 2. Experience vs Salary
plt.figure()
plt.scatter(df['Experience'], df['Salary'])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.savefig("exp_salary.png")
plt.show()

# 3. Education Distribution
plt.figure()
df['Education'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Education Distribution")
plt.ylabel("")
plt.savefig("education.png")
plt.show()

# Save top employee info
with open("top_employee.txt", "w") as f:
    f.write(f"Employee ID: {top_emp['EmployeeID']}\n")
    f.write(f"Department: {top_emp['Department']}\n")
    f.write(f"Salary: {top_emp['Salary']}\n")