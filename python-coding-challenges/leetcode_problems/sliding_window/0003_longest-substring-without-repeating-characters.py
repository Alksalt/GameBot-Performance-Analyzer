
"""
Problem: 0003. Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Description:
    Given a string, find the length of the longest substring without repeating characters.

Approach:
    Use a sliding window and a set to track unique characters in the current window.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        check_set = set()
        length = 0
        end = 0
        for start in range(n):

            while end < n and s[end] not in check_set:
                check_set.add(s[end])
                length = max(end + 1 - start, length)
                end += 1
            check_set.remove(s[start])

        return length

sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))