
"""
Problem: 0151. Reverse Words in a String
Link: https://leetcode.com/problems/reverse-words-in-a-string/

Description:
    Given an input string s, reverse the order of the words.
    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Approach:
    Use split to break the string into words, reverse the list, and join with a single space.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the order of words in a string, removing extra spaces."""
        return " ".join(s.strip().split()[::-1])

if __name__ == "__main__":
    s = "a good   example"
    sol = Solution()
    print(sol.reverseWords(s))  # Output: "example good a"