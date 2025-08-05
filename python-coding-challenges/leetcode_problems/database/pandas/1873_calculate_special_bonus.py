"""
Problem: 1873. Calculate Special Bonus (Pandas)
Link: https://leetcode.com/problems/calculate-special-bonus/

Description:
    Write a solution to calculate the bonus of each employee.
    The bonus is the employee's salary if:
      - The employee's ID is odd, and
      - The employee's name does not start with 'M'.
    Otherwise, the bonus is 0.
    Return the result table ordered by 'employee_id'.

Approach:
    Use numpy's np.where to vectorize the assignment of the 'bonus' column.
    Filter using .str.startswith('M') and modulo for odd IDs.
    Sort the output by 'employee_id' and reset the index for a clean result.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd
import numpy as np


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.copy()
    employees['bonus'] = np.where(
        (~employees["name"].str.startswith("M")) & (employees["employee_id"] % 2 != 0),
        employees["salary"],
        0
    )
    return employees[["employee_id", "bonus"]].sort_values(by="employee_id").reset_index(drop=True)

def calculate_special_bonus2(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.loc[(~employees["name"].str.startswith("M") & (employees["employee_id"] % 2 != 0))]["salary"]
    employees['bonus'] = employees['bonus'].fillna(0).astype(int)
    return employees[["employee_id", "bonus"]]

if __name__ == "__main__":
    # Example setup for the Employees table
    data = {
        "employee_id": [2, 3, 7, 8],
        "name": ["Meir", "Michael", "Addilyn", "Juan"],
        "salary": [3000, 3800, 7400, 6100]
    }
    df = pd.DataFrame(data)
    print(calculate_special_bonus(df))
