import pandas as pd
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].dropna().drop_duplicates().sort_values(ascending=False)
    return pd.DataFrame({'SecondHighestSalary':[unique_salaries.iloc[1] if len(unique_salaries) > 1 else None]})

def second_highest_salary_two(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates()
    count = employee['salary'].notna().sum() > 1
    if count:
        employee = employee.loc[
            employee['salary'] != employee['salary'].max()]
        return employee.loc[employee['salary'] == employee[
            'salary'].max()].rename(columns={'salary':'SecondHighestSalary'})[['SecondHighestSalary']]
    else:
        df = pd.DataFrame({'SecondHighestSalary':[None]})
        return df

# Example 1
data1 = {
    "id": [1, 2, 3],
    "salary": [100, 200, 300]
}
df1 = pd.DataFrame(data1)

# Example 2
data2 = {
    "id": [1],
    "salary": [100]
}
df2 = pd.DataFrame(data2)

print(second_highest_salary(df2))