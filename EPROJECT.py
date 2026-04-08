# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_data.csv")

# Preview
print("Employee Data Preview:")
print(df.head())

# Info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Basic stats
print("\nStatistical Summary:")
print(df.describe())

# Average Salary
avg_salary = df['Salary'].mean()
print("\nAverage Salary:", avg_salary)

# Highest Paid Employee
top_employee = df.loc[df['Salary'].idxmax()]
print("\nTop Paid Employee:")
print(top_employee)

# Department-wise average salary
dept_avg = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(dept_avg)

# ------------------- GRAPHS -------------------

# Bar Chart
plt.figure()
plt.bar(dept_avg.index, dept_avg.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.savefig("salary_bar_chart.png")
plt.show()

# Histogram
plt.figure()
plt.hist(df['Salary'], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.savefig("salary_histogram.png")
plt.show()

# Salary Trend by Year (if Year column exists)
if 'Year' in df.columns:
    year_avg = df.groupby('Year')['Salary'].mean()

    plt.figure()
    plt.plot(year_avg.index, year_avg.values, marker='o')
    plt.title("Salary Trend Over Years")
    plt.xlabel("Year")
    plt.ylabel("Salary")
    plt.savefig("salary_trend.png")
    plt.show()