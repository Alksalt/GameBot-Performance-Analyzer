"""
Problem: 0242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Description:
    Determine if two strings are anagrams of each other.

Approach:
    Use a hash map (Counter) or sorting to compare character counts.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import  Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)
        return s_dict == t_dict

    def isAnagram2(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)





s = "anagram"
t = "nagaram"

s2 = "rat"
t2 = "car"
sol = Solution()
print(sol.isAnagram(s,t))