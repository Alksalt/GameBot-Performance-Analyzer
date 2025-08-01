"""
Problem: 0028. Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Description:
    Return the index of the first occurrence of needle in haystack, or -1 if not found.

Approach:
    Use two pointers to scan for substring match in the main string.

Time Complexity: O(N * M)
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i1 = i2 = 0
        n = len(needle)
        while i1 < len(haystack):
            if haystack[i1] == needle[i2]:
                i1 += 1
                i2 += 1
                if i2 == n:
                    return i1 - i2
            else:
                i1 = i1 + 1 - i2
                i2 = 0
        return -1

haystack = "mississippi"
needle = "issip"

s = Solution()
print(s.strStr(haystack,needle))