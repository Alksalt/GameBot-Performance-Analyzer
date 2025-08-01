"""
Problem: 0076. Minimum Window Substring
Link: https://leetcode.com/problems/minimum-window-substring/

Description:
    Find the minimum window substring of s that contains all the characters of t.

Approach:
    Use a sliding window and hash maps to track character counts and window validity.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dict = Counter(t)
        window_count = Counter() # length: str
        have, need = 0, len(t_dict)
        res, res_len = [-1, -1], float('inf')
        start = 0

        for end in range(len(s)):
            window_count[s[end]] += 1

            if s[end] in t_dict and window_count[s[end]] == t_dict[s[end]]:
                have += 1

            while have == need:
                if (end + 1 - start) < res_len:
                    res[0], res[1] = start, end + 1
                    res_len = end + 1 - start

                window_count[s[start]] -= 1

                if s[start] in t_dict and window_count[s[start]] < t_dict[s[start]]:
                    have -= 1
                start += 1

        return s[res[0]:res[1]] if not res_len == float('inf') else ""

# Example test cases to try:
sol = Solution()

print(sol.minWindow("ADOBECODEBANC", "ABC"))    # Expected: "BANC"
print(sol.minWindow("a", "a"))                  # Expected: "a"
print(sol.minWindow("a", "aa"))                 # Expected: ""
print(sol.minWindow("aaflslflsldkalskaaa", "aaa"))  # Expected: "aaa"
print(sol.minWindow("abdecfab", "abc"))         # Expected: "cab"
print(sol.minWindow("abbcac", "abc"))           # Expected: "bca"
print(sol.minWindow("abbbbbc", "abc"))          # Expected: "abbbbbc"
print(sol.minWindow("abc", "d"))                # Expected: ""