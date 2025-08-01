"""
Problem: 0184. Department Highest Salary
Link: https://leetcode.com/problems/department-highest-salary/

Description:
    Find employees with the highest salary in each department using employee and department tables.

Approach:
    Merge tables, group by department, and filter for max salary per group.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd
import matplotlib.pyplot as plt
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged  = pd.merge(employee, department, left_on="departmentId",
                       right_on="id", suffixes=(None, '_dep'))
    max_salary = merged.groupby('name_dep')['salary'].transform('max')
    merged = merged.loc[merged['salary'] == max_salary]
    new_merged = merged.rename(columns={
        'name_dep':'Department','name':'Employee', 'salary':'Salary'})[['Department', 'Employee', 'Salary']]
    return new_merged


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, department, left_on="departmentId",
                       right_on="id", suffixes=(None, '_dep'))
    grouped = merged.groupby('name_dep')[['name', 'salary', 'name_dep']].apply(rank_salary).reset_index(drop=True)
    grouped_filt = grouped.query('salary_rank <= 3').sort_values(by=['name_dep','salary'], ascending=[True, False])
    grouped_filt_renamed = grouped_filt.rename(columns={
        'name':'Employee','name_dep':'Department','salary':'Salary'})[['Department','Employee','Salary']]
    result = grouped_filt_renamed[['Department','Employee','Salary']]
    return result
def rank_salary(group):
    group['salary_rank'] = group['salary'].rank(
        method='dense', ascending=False).astype(int)
    return group



def sum_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged  = pd.merge(employee, department, left_on="departmentId",
                       right_on="id", suffixes=(None, '_dep'))
    summed = merged.groupby('name_dep')[['salary', 'name_dep']].sum()

    return summed
# Employee table
employee_data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
    "salary": [70000, 90000, 80000, 60000, 90000],
    "departmentId": [1, 1, 2, 2, 1]
}
employee = pd.DataFrame(employee_data)

# Department table
department_data = {
    "id": [1, 2],
    "name": ["IT", "Sales"]
}
department = pd.DataFrame(department_data)

employee_data = {
    "id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Joe", "Henry", "Sam", "Max", "Janet", "Randy", "Will"],
    "salary": [85000, 80000, 60000, 90000, 69000, 85000, 70000],
    "departmentId": [1, 2, 2, 1, 1, 1, 1]
}

employee2 = pd.DataFrame(employee_data)
print(top_three_salaries(employee2,department))

"""#ploting
data = department_highest_salary(employee,department)
data2 = sum_salaries(employee,department)

fig, ax = plt.subplots(1,2, figsize=(14,8))
#first plot
plt1 = ax[0]
plt1.bar(data['Employee'], data['Salary'])
plt1.set_title('Highest salaries in departments')
plt1.set_xlabel('Employee')
plt1.set_ylabel('Salary')
plt1.set_ylim(0,100_000)

#second plot
plt2 = ax[1]
plt2.pie(data2['salary'], labels=['IT','Sales'])
plt2.set_title('Top summed salaries in dep.')


plt.tight_layout()
plt.show()"""
