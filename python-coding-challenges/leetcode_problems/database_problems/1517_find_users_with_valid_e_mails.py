import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users = users.copy()
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    users = users.loc[users['mail'].str.match(pattern)]
    return users

# Example 1
data1 = {
    "user_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "mail": ["alice@example.com", "bob_at_example.com", "charlie@leetcode.com"]
}
users1 = pd.DataFrame(data1)

# Example 2
data2 = {
    "user_id": [4, 5, 6],
    "name": ["Diana", "Eve", "Frank"],
    "mail": ["diana@mail-server.com", "eve@mailserver", "frank.o'reilly@example.co.uk"]
}
users2 = pd.DataFrame(data2)

# Example 3
data3 = {
    "user_id": [7, 8, 9],
    "name": ["Grace", "Heidi", "Ivan"],
    "mail": ["grace.smith@company.com", "heidi@company..com", "ivan-company.com"]
}
users3 = pd.DataFrame(data3)

if __name__ == "__main__":
    print(valid_emails(users1.copy()))
    print()
    print(valid_emails(users2.copy()))
    print()
    print(valid_emails(users3.copy()))