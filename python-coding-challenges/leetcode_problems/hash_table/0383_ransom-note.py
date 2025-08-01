"""
Problem: 0383. Ransom Note
Link: https://leetcode.com/problems/ransom-note/

Description:
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
    Each letter in magazine can only be used once in ransomNote.

Approach:
    Use Counter to count characters in both strings and compare counts.

Time Complexity: O(N + M), where N and M are the lengths of ransomNote and magazine.
Space Complexity: O(1) (since only lowercase letters are used)
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Check if ransomNote can be constructed from magazine using counters."""
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)
        for item, val in ransom_dict.items():
            if val > magazine_dict.get(item, 0):
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        """One-liner using Counter comparison."""
        return Counter(ransomNote) <= Counter(magazine)

if __name__ == "__main__":
    sol = Solution()
    # Example usage
    print(sol.canConstruct("a", "b"))      # False ('a' not in magazine)
    print(sol.canConstruct("aa", "ab"))    # False (only one 'a' in magazine)
    print(sol.canConstruct("aa", "aab"))   # True  (two 'a's in magazine)