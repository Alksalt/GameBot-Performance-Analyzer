"""
Problem: 0692. Top K Frequent Words
Link: https://leetcode.com/problems/top-k-frequent-words/

Description:
    Find the k most frequent words in a list, sorted by frequency and lexicographical order.

Approach:
    Use Counter to count frequencies, then sort by frequency and word.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from collections import Counter
def dif_betw_two_str(a,b):
    c_a = Counter(a)
    c_b = Counter(b)
    return list((c_b - c_a).keys())


def top_frequent_words(words,k):
    c = Counter(words)
    sorted_words = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    result = [word for word, freq in sorted_words[:k]]
    return result


print(top_frequent_words(
    ["banana", "apple", "orange", "banana", "apple",
     "bad", "juice", "apple", ],
    2))