"""
Problem: 0290. Word Pattern
Link: https://leetcode.com/problems/word-pattern/

Description:
    Given a pattern and a string s, find if s follows the same pattern.
    Each letter in the pattern must map to a word in s, and no two letters may map to the same word.

Approach:
    Use two hash maps to track the mapping from pattern to words and words to pattern.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s_list)):
            if s_list[i] not in d1:
                d1[s_list[i]] = pattern[i]
            elif d1[s_list[i]] != pattern[i]:
                return False
            if pattern[i] not in d2:
                d2[pattern[i]] = s_list[i]
            elif d2[pattern[i]] != s_list[i]:
                return False
        return True

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    sol = Solution()
    print(sol.wordPattern(pattern, s))  # Output: True
