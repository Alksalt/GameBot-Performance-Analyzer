"""
Problem: 0058. Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/

Description:
    Given a string s, return the length of the last word in the string.

Approach:
    Split the string by whitespace and return the length of the last element.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = 'hello world   ps sorry'
sol = Solution()
print(sol.lengthOfLastWord(s))
