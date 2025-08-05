"""
Problem: 1757. Recyclable and Low Fat Products (Pandas)
Link: https://leetcode.com/problems/recyclable-and-low-fat-products/

Description:
    Write a solution to find the ids of products that are both recyclable and low fat.

Approach:
    Use boolean indexing to filter rows where 'low_fats' == 'Y' and 'recyclable' == 'Y'.
    Return only the 'product_id' column.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[["product_id"]].loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]

if __name__ == "__main__":
    # Example setup for the Products table
    data = {
        "product_id": [0, 1, 2, 3, 4],
        "low_fats": ["N", "Y", "N", "Y", "Y"],
        "recyclable": ["N", "Y", "Y", "Y", "N"]
    }
    df = pd.DataFrame(data)
    print(find_products(df))
