"""
Problem: 1148. Article Views I (Pandas)
Link: https://leetcode.com/problems/article-views-i/

Description:
    Write a solution to find all the authors that viewed at least one of their own articles.
    Return the result table with the column 'id' containing unique author IDs.

Approach:
    Use boolean indexing to filter rows where 'author_id' == 'viewer_id'.
    Select and rename the 'author_id' column as 'id'. Return unique values if required.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return (
        views
        .loc[views["author_id"] == views["viewer_id"]]
        .rename(columns={"author_id": 'id'})[['id']]
        .sort_values(by='id')
        .drop_duplicates()
        .reset_index(drop=True)
    )
if __name__ == "__main__":
    # Example setup for the Views table
    data = {
        "article_id": [1, 1, 2, 2],
        "author_id": [3, 3, 7, 7],
        "viewer_id": [3, 4, 7, 8],
        "view_date": ["2019-08-01", "2019-08-01", "2019-08-01", "2019-08-02"]
    }
    df = pd.DataFrame(data)
    print(article_views(df))
