"""
Problem: 1683. Invalid Tweets (Pandas)
Link: https://leetcode.com/problems/invalid-tweets/

Description:
    Write a solution to find the IDs of tweets that are invalid.
    A tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Approach:
    Use the .str.len() accessor to get the length of each tweet's content.
    Filter for rows where the length is greater than 15, and select only the 'tweet_id' column.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return (tweets
    .loc[tweets["content"].str.len() > 15][["tweet_id"]]
    )

if __name__ == "__main__":
    # Example setup for the Tweets table
    data = {
        "tweet_id": [1, 2, 3, 4],
        "content": ["Vote for Biden", "Let us make America great again!", "H", ""]
    }
    df = pd.DataFrame(data)
    print(invalid_tweets(df))
