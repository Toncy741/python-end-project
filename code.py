import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('employee_data.csv')
df.info()
# 1. Distribution of employees across teams and percentage split
team_counts = df['Team'].value_counts()
total_employees = len(df)
team_percentages = (team_counts / total_employees) * 100

print("Distribution of employees across teams:")
print(team_counts)
print("\nPercentage split:")
print(team_percentages)

# Visualization: Bar chart for team distribution
team_counts.plot(kind='bar', figsize=(8, 6))
plt.title("Distribution of Employees Across Teams")
plt.xlabel("Team")
plt.ylabel("Number of Employees")
plt.show()


# 2. Segregate employees based on positions
position_counts = df['Position'].value_counts()
print("\nEmployees segregated based on positions:")
print(position_counts)

# Visualization: Pie chart for position distribution
position_counts.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%')
plt.title("Distribution of Employees by Position")
plt.axis('equal')
plt.show()

# 3. Identify the predominant age group
age_groups = pd.cut(df['Age'], bins=[20, 24, 29, 34, 39, 44], labels=['20-24', '25-29', '30-34', '35-39', '40-44'])
predominant_age_group = age_groups.value_counts().idxmax()
print("\nPredominant age group:", predominant_age_group)

# Visualization: Histogram for age distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=10, edgecolor='black')
plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


# 4. Team and position with highest salary expenditure
team_salaries = df.groupby('Team')['Salary'].sum()
team_with_highest_expenditure = team_salaries.idxmax()
print("\nTeam with highest salary expenditure:", team_with_highest_expenditure)

position_salaries = df.groupby('Position')['Salary'].sum()
position_with_highest_expenditure = position_salaries.idxmax()
print("Position with highest salary expenditure:", position_with_highest_expenditure)

# Visualization: Bar chart for team salary expenditure
team_salaries.plot(kind='bar', figsize=(8, 6))
plt.title("Salary Expenditure by Team")
plt.xlabel("Team")
plt.ylabel("Total Salary (in millions)")
plt.show()

# Visualization: Bar chart for position salary expenditure
position_salaries.plot(kind='bar', figsize=(8, 6))
plt.title("Salary Expenditure by Position")
plt.xlabel("Position")
plt.ylabel("Total Salary (in millions)")
plt.show()


# 5. Correlation between age and salary
import seaborn as sns

# Visualization: Scatterplot for age vs. salary
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title("Age vs. Salary")
plt.xlabel("Age")
plt.ylabel("Salary (in millions)")
plt.show()



# INSIGHTS 



print("\nKey Insights:")
print("- The Brooklyn Nets have slightly more players (53.12%) compared to the Boston Celtics (46.88%).")
print("- Both teams have a balanced mix of players across different positions, with SG being the most populated and SF having the least representation.")
print("- The predominant age group is 25-29 years old, representing the prime years for professional basketball players.")
print("- The center (C) position has the highest total salary expenditure, followed by point guards (PG) and power forwards (PF).")
print("- The scatter plot reveals a general positive correlation between age and salary, with some exceptions for younger players earning higher salaries.")
print("- The age distribution and predominant age group suggest a good balance of experienced veterans and promising young talent for both teams.")
print("- The higher salary expenditure for certain positions (C, PG, PF) may influence team strategies and roster compositions.")
print("- The age-salary correlation highlights the importance of developing young talent and retaining star players as they enter their prime years.")


