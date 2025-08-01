"""
Problem: 0014. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Description:
    Find the longest common prefix string among an array of strings.

Approach:
    Compare characters of each string with the current prefix and shorten as needed.

Time Complexity: O(N * M)
Space Complexity: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:

            i = 0

            while i < len(word) and i < len(prefix) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]

            if not prefix:
                return ""

        return prefix



strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))