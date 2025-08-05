"""
Problem: 0180. Consecutive Numbers
Link: https://leetcode.com/problems/consecutive-numbers/

Description:
    Find all numbers that appear at least three times consecutively in a log table.

Approach:
    Use pandas to detect runs of consecutive numbers and filter by count.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    mask = ((logs['num'] == logs['num'].shift(-1)) &
            (logs['num'] == logs['num'].shift(-2)))
    unique_numbers = logs.loc[mask]['num'].unique()
    return pd.DataFrame({'ConsecutiveNums':unique_numbers})
def consecutive_numbers_two(logs: pd.DataFrame, n) -> pd.DataFrame:
    logs = logs.copy()
    logs['groups'] = (logs['num'] != logs['num'].shift()).cumsum()
    runs = logs.groupby(['groups', 'num']).size().reset_index(name='count')
    result = runs.query(f'count >= {n}')['num'].unique()
    return pd.DataFrame({'ConsecutiveNums': result})



# Example data as given in the problem
data = {
    "id": [1, 2, 3, 4, 5, 6, 7,8,9],
    "num": [1, 1, 1, 2, 1, 2, 2,2,2]
}

# Create DataFrame
logs = pd.DataFrame(data)

print(consecutive_numbers_two(logs, 4))