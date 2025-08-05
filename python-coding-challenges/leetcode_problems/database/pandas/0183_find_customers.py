"""
Problem: 0183. Customers Who Never Order (Pandas)
Link: https://leetcode.com/problems/customers-who-never-order/

Description:
    Write a solution to find all customers who never ordered anything.
    Output the names of such customers with the column labeled 'Customers'.

Approach:
    Perform a left merge of the 'customers' table with the 'orders' table
    using 'id' and 'customerId'. Filter for rows where 'customerId' is missing
    (i.e., customers who have no corresponding order). Select and rename the 'name' column.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        customers, orders, left_on=['id'], right_on=["customerId"],how='left').rename(columns={'name':'Customers'})
    return merged.loc[merged['customerId'].isna()][['Customers']]


if __name__ == "__main__":
    # Example setup
    customers_data = {
        "id": [1, 2, 3],
        "name": ["Joe", "Henry", "Sam"]
    }
    orders_data = {
        "id": [1, 2],
        "customerId": [1, 2]
    }
    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)
    print(find_customers(customers_df, orders_df))
