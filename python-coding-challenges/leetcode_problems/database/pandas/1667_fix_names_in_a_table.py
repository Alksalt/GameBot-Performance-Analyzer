"""
Problem: 1667. Fix Names in a Table
Link: https://leetcode.com/problems/fix-names-in-a-table/

Description:
    Standardize the 'name' column so only the first letter is uppercase and the rest are lowercase,
    then return the result ordered by 'name' ascending.

Approach:
    Use pandas string methods for transformation and sorting.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users = users.copy()
    users['name'] = users["name"].str.lower().str.capitalize()
    return users.sort_values(by='user_id').reset_index(drop=True)
    
# Example 1
data1 = {
    "user_id": [1, 2, 3],
    "name": ["aLice", "bOB", "JoHn"],
    "email": ["alice@example.com", "bob@example.com", "john@example.com"]
}
users1 = pd.DataFrame(data1)

# Example 2
data2 = {
    "user_id": [5, 4, 6],
    "name": ["MARy", "toNY", "jane"],
    "email": ["mary@example.com", "tony@example.com", "jane@example.com"]
}
users2 = pd.DataFrame(data2)

# Example 3
data3 = {
    "user_id": [9, 7, 8],
    "name": ["ALICE", "eve", "bOB"],
    "email": ["alice@x.com", "eve@x.com", "bob@x.com"]
}
users3 = pd.DataFrame(data3)

if __name__ == "__main__":
    print(fix_names(users1.copy()))
    print()  # Empty line for readability
    print(fix_names(users2.copy()))
    print()
    print(fix_names(users3.copy()))
